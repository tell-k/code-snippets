package gyuque.gmap.googlemaps
{
	import gyuque.gmap.GMapCalc;
	
	public class GMapSatelliteTile extends GMapMapTile
	{
		public function GMapSatelliteTile(tx:int, ty:int, z:int)
		{
			super(tx, ty, z);
			
			var cols:int = GMapCalc.calcMapTileCols(z);
			if (ty < 0 || ty >= cols)
				return;
			if (tx < 0)
				tx += cols * 100;
			
			var server_index:int = tx%4;
			tx %= cols;
			ty %= cols;
			mTileURL = "http://kh"+server_index+".google.com/kh?n=404&v=23&t=" + GMapCalc.calcTilePath(tx, ty, z);
		}
	}
}
