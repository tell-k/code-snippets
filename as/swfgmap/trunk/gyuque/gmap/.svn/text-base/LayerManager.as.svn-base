package gyuque.gmap
{
	public class LayerManager extends Layer implements IPanningLayer, IAnimationDispatcher
	{
		import flash.display.*;
		import flash.geom.*;
		
		private var mAnimDisp:IAnimationDispatcher;
		private var mTransformMat:Matrix = new Matrix();
		
		public function LayerManager(c:DisplayObjectContainer)
		{
			super(c, null);
		}
		
		public function set animationDispatcher(a:IAnimationDispatcher):void
		{
			mAnimDisp = a;
		}
		
		
		public function removeLayer(idx:int, floatLayer:Boolean):void
		{
			var cidx:int = idx*2 + (floatLayer ? 1 : 0);
			if (cidx <= numChildren && getChildAt(cidx))
				removeChildAt(cidx);
		}

		public function putLayer(idx:int, lyr:Layer):void
		{
			var cidx:int = idx*2;
			addChildAt(lyr, cidx);
		}
		
		public override function onViewportChanged(e:GMapViewEvent):void
		{
			var firstset:Boolean = false;
			if (!mViewport)
				firstset = true;
			
			var v:GMapViewport = e.viewport;
			mViewport = v;
			
			if (firstset || e.dZoom)
			{
				mLastDX = 0;
				mLastDY = 0;
				updateContent(true, e);
			}
			else
			{
				mLastDX = e.screenDX;
				mLastDY = e.screenDY;
				updateContent(false, e);
			}
		}		
		
		protected function updateContent(refreshAll:Boolean, e:GMapViewEvent):void
		{
			var v:GMapViewport = mViewport;
			
			var M:Matrix = v.to_screen_transform;
			M.tx = transform.matrix.tx;
			M.ty = transform.matrix.ty;
			
			M.tx = v.width  * 0.5;
			M.ty = v.height * 0.5;
			
			mTransformMat = M;
			transform.matrix = M;
		}
		
		public function set postZoom(r:Number):void
		{
			var M:Matrix = mTransformMat.clone();
			M.a *= r;
			M.b *= r;
			M.c *= r;
			M.d *= r;
			transform.matrix = M;
		}
		
		public function getCurrentPanning(out:Point):void
		{
			out.x = 0;
			out.y = 0;
		}
		
		
		public override function addAnimation(a:Animation):void
		{
			if (mAnimDisp)
				mAnimDisp.addAnimation(a);
		}
	}
}
