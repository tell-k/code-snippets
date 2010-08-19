package gyuque.gmap.ui
{
	import flash.display.*;
	
	public class RoundRectMinusButtonSprite extends RoundRectPlusButtonSprite
	{
		public function RoundRectMinusButtonSprite(explicitWidth:Number, explicitHeight:Number, leftr:Boolean, rightr:Boolean, rclose:Boolean = true, pushed:Boolean = false)
		{
			super(explicitWidth, explicitHeight, leftr, rightr, rclose, pushed);
		}
		
		protected override function drawPlusSign(g:Graphics, cx:Number, cy:Number):void
		{
			g.moveTo(cx-4, cy-1);
			g.lineTo(cx+4, cy-1);
			g.lineTo(cx+4, cy+1);
			g.lineTo(cx-4, cy+1);
		}
	}
}
