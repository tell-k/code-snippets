package gyuque.gmap
{
	public class AnimationManager implements IAnimationDispatcher
	{
		private var mCurrent:Animation = null;
		public function addAnimation(a:Animation):void
		{
			skipAndClear();
			mCurrent = a;
		}
		
		public function next():void
		{
			if (mCurrent)
			{
				if (!mCurrent.next())
					mCurrent = null;
			}
		}
		
		public function skipAndClear():void
		{
			if (mCurrent)
			{
				mCurrent.skip();
				mCurrent = null;
			}
		}
	}
}
