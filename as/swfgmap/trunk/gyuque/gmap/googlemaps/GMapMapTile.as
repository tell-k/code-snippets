package gyuque.gmap.googlemaps
{
	import flash.display.*;
	import flash.events.*;
	import flash.net.URLRequest;
	import gyuque.gmap.GMapCalc;
	
	public class GMapMapTile extends Loader
	{
		public var mTileURL:String = null;
		public function GMapMapTile(tx:int, ty:int, z:int)
		{
			var cols:int = GMapCalc.calcMapTileCols(z);
			if (ty < 0 || ty >= cols)
				return;
			if (tx < 0)
				tx += cols * 100;
			
			var server_index:int = tx%4;
			tx %= cols;
			ty %= cols;
			mTileURL = "http://mt"+server_index+".google.com/mt?n=404&v=ap.63&x="+tx+"&y="+ty+"&zoom="+GMapCalc.calcMapsZoomIndex(z);
			addEventListener(IOErrorEvent.IO_ERROR, onIOError, true);
		}
		
		public function get url():String
		{
			return mTileURL;
		}
		
		public function loadTile():Loader
		{
			if (!mTileURL)
				return this;
			
			var req:URLRequest = new URLRequest(mTileURL);
			load(req);
			
			return this;
		}
		
		protected function onIOError(e:IOErrorEvent):void
		{
			e.preventDefault();
			e.stopPropagation();
		}		
	}
}
