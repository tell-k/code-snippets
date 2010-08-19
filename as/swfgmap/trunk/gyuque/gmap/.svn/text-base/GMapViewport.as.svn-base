package gyuque.gmap
{
	import flash.geom.Point;
	import flash.geom.Matrix;
	
	public class GMapViewport
	{
		private var mLatlng:LatLng  = new LatLng();
		private var mNrmXY:Point    = new Point();
		private var mBitmapXY:Point = new Point();
		private var mViewSize:Point = new Point();
		
		private var mZoom:int;
		private var mMapSize:Number;
		
		private var mViewToScreen:Matrix    = new Matrix();
		private var mInvViewToScreen:Matrix = new Matrix();
		
		public function GMapViewport(lat:Number, lng:Number, vw:Number, vh:Number, zm:int, useDeg:Boolean = true)
		{
			resetTransform();
			
			if (useDeg)
			{
				lat *= Math.PI / 180.0;
				lng *= Math.PI / 180.0;
			}
			
			mLatlng.lat = lat;
			mLatlng.lng = lng;
			zoom = zm;
			
			mViewSize.x = vw;
			mViewSize.y = vh;
			
			calcXY();
		}
		
		public function transformVectorScreenToView(x:Number, y:Number, out:Point):void
		{
			out.x = x;
			out.y = y;
			
			Math2D.transformNoMove(out, mInvViewToScreen);
		}
		
		public function transformVectorViewToScreen(x:Number, y:Number, out:Point):void
		{
			out.x = x;
			out.y = y;
			
			Math2D.transformNoMove(out, mViewToScreen);
		}
		
		private function resetTransform():void
		{
			mViewToScreen.identity();
			mInvViewToScreen.identity();
		}
		
		public function setTransform(M:Matrix):void
		{
			mViewToScreen    = M;
			
			mInvViewToScreen = M.clone();
			mInvViewToScreen.invert();
		}
		
		public function setNewRotation(r:Number):void
		{
			var T:Matrix = new Matrix();
			T.rotate(r);
			setTransform(T);			
		}
		
		public function set zoom(z:int):void
		{
			mZoom = z;
			mMapSize = Number( GMapCalc.calcMapSize(z) );

			calcXY();
		}
		
		public function get zoom():int
		{
			return mZoom;
		}
		
		
		public function moveByPixel(dx:Number, dy:Number):void
		{
			var v:Point = new Point();
			transformVectorScreenToView(dx, dy, v);
			
			mBitmapXY.x += v.x;
			mBitmapXY.y += v.y;
			
			mNrmXY.x = mBitmapXY.x / mMapSize;
			mNrmXY.y = mBitmapXY.y / mMapSize;
			
			GMapCalc.XYtoLatLng(mNrmXY.x, mNrmXY.y, mLatlng);
		}
		
		private function calcXY():void
		{
			GMapCalc.LatLngToXY(mLatlng.lat, mLatlng.lng, mNrmXY);
			
			mBitmapXY.x = mNrmXY.x * mMapSize;
			mBitmapXY.y = mNrmXY.y * mMapSize;
		}
		
		public function get width():Number
		{
			return mViewSize.x;
		}
		
		public function get height():Number
		{
			return mViewSize.y;
		}
		
		public function get lat():Number
		{
			return mLatlng.lat;
		}
		
		public function get lng():Number
		{
			return mLatlng.lng;
		}

		public function get to_screen_transform():Matrix
		{
			return mViewToScreen;
		}
		
		public function get centerBitmapX():Number
		{
			return mBitmapXY.x;
		}
	
		public function get centerBitmapY():Number
		{
			return mBitmapXY.y;
		}
		
		public function get centerNX():Number
		{
			return mNrmXY.x;
		}
	
		public function get centerNY():Number
		{
			return mNrmXY.y;
		}
		
	}
}
