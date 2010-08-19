package gyuque.gmap.ui
{
	import flash.display.*;
	
	public class RoundRectPlusButtonSprite extends RoundRectButtonSprite
	{
		public function RoundRectPlusButtonSprite(explicitWidth:Number, explicitHeight:Number, leftr:Boolean, rightr:Boolean, rclose:Boolean = true, pushed:Boolean = false)
		{
			super(explicitWidth, explicitHeight, leftr, rightr, rclose, pushed);
		}
		
		protected override function drawLabel(g:Graphics, w:Number, h:Number, shift_y:Number):void
		{
			var cx:int = w/2;
			var cy:int = h/2 + shift_y;

			g.lineStyle(undefined, 0, 0, true);
			g.beginFill(0xffffff);
			drawPlusSign(g, cx, cy+1);
			g.endFill();

			g.beginFill(0x444444);
			drawPlusSign(g, cx, cy);
			g.endFill();
		}
		
		protected function drawPlusSign(g:Graphics, cx:Number, cy:Number):void
		{
			g.moveTo(cx-4, cy-1);
			g.lineTo(cx-1, cy-1);
			g.lineTo(cx-1, cy-4);
			g.lineTo(cx+1, cy-4);
			g.lineTo(cx+1, cy-1);
			g.lineTo(cx+4, cy-1);
			g.lineTo(cx+4, cy+1);
			g.lineTo(cx+1, cy+1);
			g.lineTo(cx+1, cy+4);
			g.lineTo(cx-1, cy+4);
			g.lineTo(cx-1, cy+1);
			g.lineTo(cx-4, cy+1);
		}
	}
}
