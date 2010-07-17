package gyuque.gmap
{
	import flash.events.*;
	import flash.utils.Timer;
	import flash.geom.*;
	
	public class ViewportUpdater
	{
public var dout:IDebugOut;
	
		private var mCurViewport:GMapViewport = null;
		private var mListener:IMeshMap;
		private var mGHash:GridHash;
		
		private var mReqQueue:XYQueue;
		private var mUpdateTimer:Timer;

		private var mLoadedTiles:XYQueue;
		
		public function ViewportUpdater(listener:IMeshMap)
		{
			mListener = listener;
			mGHash = new GridHash();
			mReqQueue = new XYQueue();
			mLoadedTiles = new XYQueue();
			
			mUpdateTimer = new Timer(500); 
			mUpdateTimer.addEventListener(TimerEvent.TIMER, onTimer);
			mUpdateTimer.start();
		}
		
		public function terminate():void
		{
			mUpdateTimer.stop();
		}
		
		public function set currentViewport(v:GMapViewport):void
		{
			var prev:GMapViewport = mCurViewport;
			mCurViewport = v;
			if (mCurViewport)
			{
				if (prev == null)
					refresh();
				else
					update();
			}
		}
		
		public function onTimer(e:Event):void
		{
			update();
				
			for (var i:int = 0;i < 3;i++)
			{
				if (mReqQueue.empty)
					return;
//dout.puts("tiles:"+ mLoadedTiles.length +"  queue:"+mReqQueue.length);
				
				var j:Object = {};
				mReqQueue.consume(j);
				switch(j.v)
				{
				case 1: // load
					checkAndLoad(j.x, j.y);
					break;
				case 2: // load
					checkAndUnload(j.x, j.y);
					break;
				}
			}
		}
		
		private function refresh():void
		{
			loadCenterTile();
			onTimer(null);
		}
		
		private static const AROUND_POS:Array = [0, 1, 0, -1];
		private function spread(tx:int, ty:int, nest:int = -1):Boolean
		{
			if (nest == -1)
			{
				for (var n:int = 0;n < 5;n++)
				{
					if (!spread(tx, ty, n))
						break;
				}
				return false;
			}
			
			var retval:Boolean = false;
			for (var i:int = 0;i < 4;i++)
			{
				var x:int = tx + AROUND_POS[i];
				var y:int = ty + AROUND_POS[(i+3)%4];
				
				if (nest == 0)
				{
					if (isTileVisible(x, y) == T_VISIBLE)
					{
						retval = true;
						addLoadJob(x, y);
					}
				}
				else
					retval = spread(x, y, nest-1) || retval;
			}
			
			return retval;
		}
		
		private function isGoneOut(tx:int, ty:int):Boolean
		{
			return (isTileVisible(tx, ty) == T_INVISIBLE);
		}
		
		private function checkAndLoad(tx:int, ty:int):void
		{
			if (mGHash.peek(tx, ty))
			{
				mListener.loadTile(tx, ty);
				mLoadedTiles.push(tx, ty, 1);
			}
		}

		private function checkAndUnload(tx:int, ty:int):void
		{
			if (!mGHash.peek(tx, ty))
				mListener.unloadTile(tx, ty);
		}

		private function addLoadJob(tx:int, ty:int):void
		{
			if (!mGHash.peek(tx, ty))
			{
				mGHash.poke(tx, ty, 1);
				mReqQueue.push(tx, ty, 1);
			}
		}

		private function addUnloadJob(tx:int, ty:int):void
		{
			if (mGHash.peek(tx, ty))
			{
				mGHash.poke(tx, ty, 0);
				mReqQueue.push(tx, ty, 2);
			}
		}
		
		private function update():void
		{
	
			var j:Object = {};
			var nextArr:XYQueue = new XYQueue();
			var len:int = mLoadedTiles.length;

			for (;!mLoadedTiles.empty;)
			{
				mLoadedTiles.consume(j);
				if (isGoneOut(j.x, j.y))
					addUnloadJob(j.x, j.y);
				else
				{
					nextArr.push(j.x, j.y, j.v);
					spread(j.x, j.y, 0);
				}
			}
			
			mLoadedTiles = nextArr;
		}
		
		private function loadCenterTile():void
		{
			var v:GMapViewport = mCurViewport;
			var tiledata:Object = GMapCalc.calcTileData(v.centerNX, v.centerNY, v.zoom, 0);

			mListener.resetOffset(tiledata.tile_index.x, tiledata.tile_index.y);
			mListener.setTileOffset(tiledata.offset.x, tiledata.offset.y);
			
			addLoadJob(tiledata.tile_index.x, tiledata.tile_index.y);
			spread(tiledata.tile_index.x, tiledata.tile_index.y);
		}
		
		private static const T_INVISIBLE :int = 0;
		private static const T_CLOSELY   :int = 1;
		private static const T_VISIBLE   :int = 2;
		private function isTileVisible(tx:int, ty:int):int
		{
			if (!mListener)
				return T_INVISIBLE;
				
			var bx:Number = (tx - mListener.centerTileX) * GMapCalc.TILE_SIZE;
			var by:Number = (ty - mListener.centerTileY) * GMapCalc.TILE_SIZE;
			
			var p:Point = new Point();

			mListener.getCurrentPanning(p);
			bx -= p.x;
			by -= p.y;

			mCurViewport.transformVectorViewToScreen(bx, by, p);
			
			var padding:Number = GMapCalc.TILE_SIZE*1.2;
			for (var i:int = 0;i < 2;i++) {
			if (p.x >= (-mCurViewport.width*0.5 - padding) && p.y >= (-mCurViewport.height*0.5 - padding) && p.x < (mCurViewport.width*0.5 + padding) && p.y < (mCurViewport.height*0.5 + padding))
				return T_VISIBLE-i;
				
				padding *= 1.5;
			}
			
			return T_INVISIBLE;
		}
	}
}

class XYQueue
{
	private var Xs:Array = new Array();
	private var Ys:Array = new Array();
	private var Vs:Array = new Array();
	
	public function consume(out:Object):Boolean
	{
		if (Xs.length < 1) return false;
		
		out.x = Xs.shift();
		out.y = Ys.shift();
		out.v = Vs.shift();
		return true;
	}
	
	public function get length():int
	{
		return Xs.length;
	}

	public function at(out:Object, i:int):void
	{
		out.x = Xs[i];
		out.y = Ys[i];
		out.v = Vs[i];
	}
	
	public function get empty():Boolean
	{
		return Xs.length < 1;
	}
	
	public function push(x:int, y:int, v:int):void
	{
		Xs.push(x);
		Ys.push(y);
		Vs.push(v);
	}
}
