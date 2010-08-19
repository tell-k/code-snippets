package gyuque.gmap
{
	import flash.events.EventDispatcher;
	import flash.display.*;
	import flash.geom.Point;
	
	public class Layer extends Sprite implements IAnimationDispatcher
	{
		protected var mViewport:GMapViewport;
		protected var mIndex:int;
		
		protected var mLastDX:Number;
		protected var mLastDY:Number;
		protected var mParent:Layer;
		protected var mEventSource:EventDispatcher;
		
		public function Layer(eventSrc:EventDispatcher, parent:Layer)
		{
			eventSrc.addEventListener(GMapViewEvent.VIEWPORT_CHANGED, onViewportChanged);
			mEventSource = eventSrc;
			mParent = parent;
		}
		
		public function get layerIndex():int
		{
			return mIndex;
		}
		
		public function set layerIndex(i:int):void
		{
			mIndex = i;
		}
		
		public function onViewportChanged(e:GMapViewEvent):void
		{}
		
		public function addAnimation(a:Animation):void
		{
			if (mParent is IAnimationDispatcher)
				IAnimationDispatcher(mParent).addAnimation(a);
		}
		
		public function terminate():void
		{
		}		
		
		public function clone():Layer
		{
			return new Layer(mEventSource, mParent);
		}
	}
}
