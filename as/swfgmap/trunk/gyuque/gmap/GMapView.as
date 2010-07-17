package gyuque.gmap
{
	import flash.display.*;
	import flash.geom.Point;
	import flash.text.TextField;
	import flash.text.TextFormat;
	import flash.events.*;
	import gyuque.gmap.googlemaps.*;
	
	public class GMapView extends MovieClip implements IDebugOut, IAnimationDispatcher
	{
		private static const GOOGLE_LOGO_URL:String = "http://www.google.com/intl/ja_jp/mapfiles/poweredby.png";
		
		private var txDebugOut:TextField = null;
		private var fmtDebugOut:TextFormat;
		private var mDrag:DragInfo = new DragInfo();
		private var mBaseSprite:Sprite;
		private var mSuperLayer:LayerManager;
		private var mAnimMan:AnimationManager;
		private var mZoomLock:Boolean;
		protected var mCurrentViewport:GMapViewport;
		
		public function GMapView(options:*)
		{
			mZoomLock = false;
			if (options.double_click)
				doubleClickEnabled = true;
			
			mBaseSprite = putBaseSprite();
			if (options.initial_size)
				clearBase(options.initial_size[0], options.initial_size[1]);
			
			mAnimMan = new AnimationManager();
			mSuperLayer = new LayerManager(this);
			mSuperLayer.doubleClickEnabled = doubleClickEnabled;
			addChild(mSuperLayer);
			mSuperLayer.animationDispatcher = this;

			if (options.debug_box)
			{
				txDebugOut = new TextField();
				addChild(txDebugOut);
				
				txDebugOut.selectable = false;
				txDebugOut.mouseEnabled = false;
				fmtDebugOut = new TextFormat();
				fmtDebugOut.size = 9;
				txDebugOut.y = 110;
				txDebugOut.height = height-110;
				txDebugOut.width = 600;
			}

			addGoogleMapLayer();

			if (options.initial_viewport)
			{
				setViewport(options.initial_viewport);
			}
			hookStdEvents();
		}
		
		protected function setViewport(v:GMapViewport):void
		{
			mCurrentViewport = v;
			fireViewportChange();
		}
		
		public function setViewRotation(rad:Number):void
		{
			mCurrentViewport.setNewRotation(rad);
			fireViewportChange();
		}
		
		protected function fireViewportChange(dx:Number = 0, dy:Number = 0, dzm:int = 0, zoomAnimation:Boolean = true):void
		{
			var e:GMapViewEvent = new GMapViewEvent(mCurrentViewport, GMapViewEvent.VIEWPORT_CHANGED);
			e.screenDX = dx;
			e.screenDY = dy;
			e.dZoom = dzm;
			e.zoomAnimation = zoomAnimation;
			dispatchEvent(e);
		}
		
		protected function putBaseSprite():Sprite
		{
			var s:Sprite = new Sprite();
			addChild(s);
			s.doubleClickEnabled = doubleClickEnabled;
			
			return s;
		}
		
		protected function addGoogleMapLayer():Boolean
		{
			var lyr:GMapMapLayer = new GMapMapLayer(this, mSuperLayer);
			lyr.debug_out = this;
			lyr.doubleClickEnabled = doubleClickEnabled;
			mSuperLayer.putLayer(0, lyr);
			
			return true;
		}
		
		protected function clearBase(w:int, h:int):void
		{
			var g:Graphics = mBaseSprite.graphics;
			g.beginFill(0xe5e0d5);
			g.drawRect(0,0, w, h);
			g.endFill();
		}
		
		protected function hookStdEvents():void
		{
			addEventListener(MouseEvent.MOUSE_MOVE ,  onMouseMove);
			addEventListener(MouseEvent.MOUSE_DOWN ,  onMouseDown);
			addEventListener(MouseEvent.MOUSE_UP   ,  onMouseUp);
			addEventListener(MouseEvent.MOUSE_OUT  ,  onMouseOut);
			addEventListener(MouseEvent.MOUSE_WHEEL,  onMouseWheel);
			addEventListener(MouseEvent.DOUBLE_CLICK, onDblClick);
			
			addEventListener(Event.ENTER_FRAME, onEnterFrame);
		}
		
		
		protected function onDblClick(e:MouseEvent):void
		{
		}

		protected function onMouseWheel(e:MouseEvent):void
		{
			zoom((e.delta > 0) ? 1 : -1, e.stageX, e.stageY);
		}
		
		public function zoom(d:int, px:Number = -1, py:Number = -1, animation:Boolean = true):void
		{
			if (mZoomLock)
				return;
			mZoomLock = true;
			
			var z:int = mCurrentViewport.zoom;
			var oldz:int = z;
			z += d;
			if (z < 0)  z = 0;
			if (z > 17) z = 17;
			
			var oldZ:int = mCurrentViewport.zoom;
			mCurrentViewport.zoom = z;
			
			if (mCurrentViewport.zoom == oldZ)
				return;
			
			var mv:Point;
			if (px >= 0 || py >= 0) {
				mv = calcFixedPointZoom(px, py, (d>0) ? 2 : 0.5, mCurrentViewport);
				mCurrentViewport.moveByPixel(mv.x, mv.y);
			}
			
			if (!mv)
				mv = new Point(0, 0)
			
			fireViewportChange(mv.x, mv.y, z - oldz, animation);
		}
		
		protected function calcFixedPointZoom(sx:Number, sy:Number, zoomRatio:Number, vpAfter:GMapViewport):Point
		{
			sx -= vpAfter.width *0.5;
			sy -= vpAfter.height*0.5;
			
			var sx2:Number = sx * zoomRatio;
			var sy2:Number = sy * zoomRatio;
			
			var dx:Number = sx2 - sx;
			var dy:Number = sy2 - sy;
		
			return new Point(dx, dy);
		}

		protected function onMouseOut(e:MouseEvent):void
		{
			if (e.stageX < 0 || e.stageY < 0 || 
				e.stageX >= width || e.stageY >= height)
				mDrag.dragging = false;
		}
		
		protected function onMouseMove(e:MouseEvent):void
		{
			if (mDrag.dragging)
			{
				mDrag.update(e.stageX, e.stageY);
				
				//cls();
				//puts((mCurrentViewport.lat/0.0174533)+"  "+(mCurrentViewport.lng/0.0174533));
				moveByPixel(-mDrag.dx, -mDrag.dy);
				//puts(e.stageX.toString()+","+e.stageY.toString()+"   "+mDrag.dx.toString()+","+mDrag.dy.toString());
			}
		}
		
		protected function onMouseDown(e:MouseEvent):void
		{
			mDrag.dragging = true;
			mDrag.update(e.stageX, e.stageY);
		}
		
		protected function onMouseUp(e:MouseEvent):void
		{
			mDrag.dragging = false;
		}

		protected function onEnterFrame(e:Event):void
		{
			mAnimMan.next();
			mZoomLock = false;
		}
		
		public function moveByPixel(dx:Number, dy:Number):void
		{
			if (mCurrentViewport)
			{
				mCurrentViewport.moveByPixel(dx, dy);
				fireViewportChange(dx, dy);
			}
		}
		
		public function addAnimation(a:Animation):void
		{
			mAnimMan.addAnimation(a);
		}
		
		public function puts(s:String):void
		{
			if (!txDebugOut)
				return;
			
			txDebugOut.appendText(s);
			txDebugOut.appendText("\r\n");
			txDebugOut.setTextFormat(fmtDebugOut);
		}
		
		public function cls():void
		{
			txDebugOut.text = "";
		}
		
		public function d_outMetrics():void
		{
			puts("w: "+ width.toString());
			puts("h: "+ height.toString());
		}
	}
}

class DragInfo
{
	public function DragInfo (){dragging=false;}
	public var prevX:Number;
	public var prevY:Number;
	public var dx:Number;
	public var dy:Number;
	public var dragging:Boolean;
	
	public function update(x:Number, y:Number):void
	{
		dx = x - prevX;
		dy = y - prevY;
		
		prevX = x;
		prevY = y;
	}
}

