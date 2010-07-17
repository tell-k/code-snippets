package gyuque.gmap.googlemaps
{
	import flash.events.*;
	import flash.display.*;
	import flash.geom.Point;
	import flash.net.URLRequest;
	import gyuque.gmap.*;
	
	public class GMapMapLayer extends Layer implements IMeshMap
	{
		protected var mVPobs:ViewportUpdater;
		protected var mCenterTX:int;
		protected var mCenterTY:int;
		protected var mLoadedTiles:GridHash = new GridHash();
		protected var mTileClass:Class = GMapMapTile;
		
		public function set debug_out(d:IDebugOut):void
		{
			mVPobs.dout = d;
		}
		
		public function GMapMapLayer(eventSrc:EventDispatcher, parent:Layer)
		{
			super(eventSrc, parent);
			mouseChildren = false;
			mVPobs = new ViewportUpdater(this);
			
			var g:Graphics = graphics;
		}
		
		public override function onViewportChanged(e:GMapViewEvent):void
		{
			var firstset:Boolean = false;
			if (!mViewport)
				firstset = true;
				
			if (e.dZoom)
			{
				if (mParent is LayerManager)
				{
					var a:PointZoomAnimation = new PointZoomAnimation(this, e, LayerManager(mParent));
					addAnimation(a);
				}
				
				return;
			}				
			
			var v:GMapViewport = e.viewport;
			mViewport = v;		
			mVPobs.currentViewport = mViewport;
			
			if (e.screenDX || e.screenDY)
			{
				var p:Point = new Point();
				mViewport.transformVectorScreenToView(e.screenDX, e.screenDY, p);
				x -= p.x;
				y -= p.y;
			}
		}

		public override function clone():Layer
		{
			var newLayer:GMapMapLayer = new GMapMapLayer(mEventSource, mParent);
			newLayer.layerIndex = layerIndex;
			newLayer.doubleClickEnabled = doubleClickEnabled;
			newLayer.debug_out = mVPobs.dout; //
			
			return newLayer
		}
		
		public override function terminate():void
		{
			mVPobs.terminate();
			mEventSource.removeEventListener(GMapViewEvent.VIEWPORT_CHANGED, onViewportChanged);
		}
		
		public function setTileOffset(ox:int, oy:int):void
		{
			var c:int = GMapCalc.TILE_SIZE/2;
			x = -(ox-c);
			y = -(oy-c);
		}
		
		public function loadTile(tx:int, ty:int):void
		{
			var tile:GMapMapTile = new mTileClass(tx, ty, mViewport.zoom);
//mVPobs.dout.puts(tile.url);
			addChild(tile.loadTile());
				
			var c:int = GMapCalc.TILE_SIZE/2;
			
			var otx:int = tx - mCenterTX;
			var oty:int = ty - mCenterTY;
			
			tile.x = -c + otx*GMapCalc.TILE_SIZE;
			tile.y = -c + oty*GMapCalc.TILE_SIZE;
			
			mLoadedTiles.poke(tx, ty, tile);
		}
		
		public function unloadTile(tx:int, ty:int):void
		{
			var o:Object = mLoadedTiles.peek(tx, ty);
			if (o)
			{
				removeChild( DisplayObject(o) );
			}
		}
		
		public function resetOffset(tx:int, ty:int):void
		{
			mCenterTX = tx;
			mCenterTY = ty;
		}
		
		public function getCurrentPanning(out:Point):void
		{
			if (parent && parent is IPanningLayer)
			{
				IPanningLayer(parent).getCurrentPanning(out);
			}
			else
			{
				out.x = 0;
				out.y = 0;
			}

			out.x -= x;
			out.y -= y;
			
		}
		
		public function get centerTileX():int
		{
			return mCenterTX;
		}
		
		public function get centerTileY():int		
		{
			return mCenterTY;
		}
	}
}
