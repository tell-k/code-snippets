package gyuque.gmap
{
	public class SpinResetAnimation extends Animation
	{
		private var mView:GMapView;
		private var mStart:Number;
		private var STEPS:int = 6;
		private var mCount:int = 0;
		
		public function SpinResetAnimation(v:GMapView, start:Number)
		{
			mView = v;
			if (start > Math.PI)
				start -= Math.PI*2;
			mStart = start;
		}
		
		public override function next():Boolean
		{
			if (++mCount == STEPS)
			{
				mView.setViewRotation(0);
				return false;
			}
			
			mView.setViewRotation(mStart / Math.pow(1.9, mCount));
			
			return true;
		}
		
		public override function skip():void
		{
			mView.setViewRotation(0);
		}
	}
}
