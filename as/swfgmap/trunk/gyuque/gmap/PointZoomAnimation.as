package gyuque.gmap
{
	public class PointZoomAnimation extends Animation
	{
		import flash.geom.Point;
		
		private var mOldLayer:Layer;
		private var mViewEvent:GMapViewEvent;
		private var mLayerMan:LayerManager;
		private var mFloatingIndex:int;
		private var mDZoom:int;
		private var STEPS:int = 6;
		private var mCount:int = 0;
		
		private var mOrgX:Number;
		private var mOrgY:Number;
		private var mShift:Point;
		
		public function PointZoomAnimation(oldLayer:Layer, e:GMapViewEvent, man:LayerManager)
		{
			mOldLayer  = oldLayer;
			
			mDZoom = e.dZoom;
			e.dZoom = 0;
			
			mViewEvent = e;
			mLayerMan = man;
			mOrgX = oldLayer.x;
			mOrgY = oldLayer.y;
			
			mShift = new Point(e.screenDX, e.screenDY);
			e.screenDX = 0;
			e.screenDY = 0;
			
		}
		
		private function relayAndFloat():void
		{
			mOldLayer.terminate();
			
			var cidx:int = mOldLayer.layerIndex*2;
			mFloatingIndex = cidx+1;
			if (cidx < (mLayerMan.numChildren-1) && mLayerMan.getChildAt(mFloatingIndex))
				mLayerMan.removeChildAt(mFloatingIndex);
					
			mLayerMan.removeChildAt(cidx);
			var newLayer:Layer = mOldLayer.clone();
			mLayerMan.addChildAt(newLayer, cidx);
			mLayerMan.addChildAt(mOldLayer, mFloatingIndex);
					
			newLayer.onViewportChanged(mViewEvent);
		}
		
		public override function next():Boolean
		{
			if (mCount == 0)
				relayAndFloat();

			if (++mCount >= STEPS)
			{
				skip();
				return false;
			}
			
			var rt:Number = 0.17 * mCount;
			var pz:Number = (mDZoom > 0) ? (rt + 1.0) : (1.0 - rt/2);
			
			mLayerMan.postZoom = pz;	
			mOldLayer.x = mOrgX - rt * mShift.x/pz;
			mOldLayer.y = mOrgY - rt * mShift.y/pz;
			
			return true;
		}
		
		public override function skip():void
		{
			mLayerMan.postZoom = 1;
			if (mFloatingIndex < mLayerMan.numChildren && mLayerMan.getChildAt(mFloatingIndex) == mOldLayer)
				mLayerMan.removeChildAt(mFloatingIndex);
		}
	}
}
