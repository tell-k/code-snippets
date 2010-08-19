package gyuque.gmap.googlemaps
{
	public class GMapSatelliteLayer extends GMapMapLayer
	{
		import flash.events.*;
		import gyuque.gmap.Layer;
		public function GMapSatelliteLayer(eventSrc:EventDispatcher, parent:Layer)
		{
			super(eventSrc, parent);
			mTileClass = GMapSatelliteTile;
		}
		
		public override function clone():Layer
		{
			var newLayer:GMapSatelliteLayer = new GMapSatelliteLayer(mEventSource, mParent);
			newLayer.layerIndex = layerIndex;
			newLayer.doubleClickEnabled = doubleClickEnabled;
			newLayer.debug_out = mVPobs.dout; //
			
			return newLayer
		}
	}
}
