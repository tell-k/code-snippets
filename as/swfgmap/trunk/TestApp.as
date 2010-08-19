package
{
	import flash.display.*;
	import flash.geom.*;
	import gyuque.gmap.*;
	import gyuque.gmap.ui.*;
	import mx.events.SliderEvent;
	/*
	import mx.controls.RadioButtonGroup;
	import mx.controls.RadioButton;*/
	import flash.events.*;

	public class TestApp extends GMapView
	{
		private var mSpnr:Spinner;
		/*
		private var mLayerToggle:ToggleButton;
		private var mLayerRadioGroup:RadioButtonGroup;
		*/
		public function TestApp()
		{
			super({
					debug_box   : true,
					initial_size: [640, 480],
					double_click: true
				});
			
			stage.align = StageAlign.TOP_LEFT;
			stage.scaleMode = StageScaleMode.NO_SCALE;
			
			
			var vp:GMapViewport = new GMapViewport(36.09992, 139.65497, 640, 480, 15);
			setViewport(vp);

			var spnr:Spinner = new Spinner(64);
			addChild(spnr);
			
			spnr.x = 8;
			spnr.y = 8;
			
			spnr.centerButton.addEventListener(MouseEvent.CLICK, onSpinReset);
			spnr.centerButton.addEventListener(MouseEvent.MOUSE_DOWN, onSpinResetDown);
			spnr.addEventListener(SliderEvent.THUMB_DRAG , onSpinner);
			mSpnr = spnr;
/*			
			mLayerRadioGroup = new RadioButtonGroup();
			mLayerToggle = new ToggleButton();
			mLayerToggle.group = mLayerRadioGroup;
			mLayerToggle.explicitWidth = 100;
			mLayerToggle.explicitHeight = 100;
			addChild(mLayerToggle);
		*/	
			var rbZIn:RoundRectButton = new RoundRectButton(RoundRectPlusButtonSprite, 24, 24, false, true);
			addChild(rbZIn);
			rbZIn.x = 48;
			rbZIn.y = 80;
			
			var rbZOut:RoundRectButton = new RoundRectButton(RoundRectMinusButtonSprite, 40, 24, true, false);
			addChild(rbZOut);
			rbZOut.x = 9;
			rbZOut.y = 80;

			rbZIn.addEventListener(MouseEvent.CLICK, onZoomInButton);
			rbZOut.addEventListener(MouseEvent.CLICK, onZoomOutButton);
		}
		
		protected override function onDblClick(e:MouseEvent):void
		{
			zoom(1, e.stageX, e.stageY);
		}
		
		protected function onSpinner(e:SliderEvent):void
		{
			setViewRotation(mSpnr.value);
		}
		
		protected function onSpinReset(e:MouseEvent):void
		{
			var a:SpinResetAnimation = new SpinResetAnimation(this, mSpnr.value);
			addAnimation(a);
		}

		protected function onSpinResetDown(e:MouseEvent):void
		{
			e.stopPropagation();
		}

		protected function onZoomInButton(e:MouseEvent):void
		{
			zoom(1);
		}

		protected function onZoomOutButton(e:MouseEvent):void
		{
			zoom(-1);
		}
		
		public override function setViewRotation(rad:Number):void
		{
			mSpnr.value = rad;
			super.setViewRotation(rad);
		}		
		
	}
}
