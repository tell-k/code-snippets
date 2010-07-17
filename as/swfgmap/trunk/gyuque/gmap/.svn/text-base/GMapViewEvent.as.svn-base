package gyuque.gmap
{
	import flash.events.Event;

	public class GMapViewEvent extends Event
	{
		public static const VIEWPORT_CHANGED:String = "ViewportChanged";

		private var mViewport:GMapViewport;
		private var mScrDX:Number;
		private var mScrDY:Number;
		private var mDZ:int;
		private var mZoomAnimation:Boolean;
		
		public function GMapViewEvent(vp:GMapViewport, t:String)
		{
			super(t);
			mViewport = vp;
		}
		
		public function get viewport():GMapViewport
		{
			return mViewport;
		}
		
		public function set screenDX(d:Number):void
		{
			mScrDX = d;
		}
		public function get screenDX():Number
		{
			return mScrDX;
		}

		public function set screenDY(d:Number):void
		{
			mScrDY = d;
		}
		public function get screenDY():Number
		{
			return mScrDY;
		}

		public function get dZoom():int
		{
			return mDZ;
		}
		public function set dZoom(d:int):void
		{
			mDZ = d;
		}
		
		public function set zoomAnimation(b:Boolean):void
		{
			mZoomAnimation = b;
		}
		
		public function get zoomAnimation():Boolean
		{
			return mZoomAnimation;
		}
		
	}
}
