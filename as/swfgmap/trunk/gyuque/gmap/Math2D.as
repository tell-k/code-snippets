package gyuque.gmap
{
	import flash.geom.Point;
	import flash.geom.Matrix;
	
	public class Math2D
	{
		public static function transformNoMove(v:Point, M:Matrix):void
		{
			var m:Matrix = M.clone();
			m.tx = 0;
			m.ty = 0;

			var res:Point = m.transformPoint(v);
			v.x = res.x;
			v.y = res.y;
		}
	}
}