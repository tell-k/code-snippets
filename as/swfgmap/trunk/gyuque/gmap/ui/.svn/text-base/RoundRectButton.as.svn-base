package gyuque.gmap.ui
{
	import flash.display.*;
	import flash.events.*;
	
	public class RoundRectButton extends SimpleButton
	{
		public function RoundRectButton(spriteClass:Class, explicitWidth:Number, explicitHeight:Number, leftr:Boolean, rightr:Boolean, rclose:Boolean = true)
		{
			var sup:RoundRectButtonSprite = new spriteClass(explicitWidth, explicitHeight, leftr, rightr, rclose);
			var sdown:RoundRectButtonSprite = new spriteClass(explicitWidth, explicitHeight, leftr, rightr, rclose, true);
			upState = sup;
			hitTestState = sup;
			overState = sup;
			downState = sdown;
			
			useHandCursor = true;
			addEventListener(MouseEvent.MOUSE_DOWN , onMouseDown);
		}
		
		protected function onMouseDown(e:MouseEvent):void
		{
			e.stopPropagation();
		}
	}
}

