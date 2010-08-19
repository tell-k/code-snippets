package gyuque.gmap
{
	public class GridHash
	{
		private var mHash:Object;
		private var mItCursor:int;
		
		public function GridHash()
		{
			mHash = {};
		}
		
		private function makeKey(x:int, y:int):String
		{
			return "_"+x+"_"+y;
		}
		
		public function poke(x:int, y:int, dat:*):void
		{
			mHash[makeKey(x, y)] = dat;
		}

		public function peek(x:int, y:int):Object
		{
			return mHash[makeKey(x, y)] || 0;
		}
		
		public function clear():void
		{
			mHash = {};
		}
		
		public function map(proc:Function, _this:Object):void
		{
			for each(var v:int in mHash)
				proc.apply(_this, [v]);
		}
	}
}