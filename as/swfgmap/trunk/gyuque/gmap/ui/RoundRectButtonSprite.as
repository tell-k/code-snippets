package gyuque.gmap.ui
{
	import flash.display.*;
	import flash.geom.Matrix;
	
	public class RoundRectButtonSprite extends Sprite
	{
		protected var mBorderColor:uint = 0;
		protected var mLeftRounded:Boolean;
		protected var mRightRounded:Boolean;
		protected var mRightClosed:Boolean;
		protected var mR:Number = 6;
		protected const APOS:Number = 0.292893219;
		
		private var mGradColors:Array;
		private var mGradAlphas:Array;
		private var mGradRatios:Array;
		private var mGradMatrix:Matrix;	
		
		private var mHGradColors:Array;
		private var mHGradAlphas:Array;
		private var mHGradRatios:Array;
		private var mHGradMatrix:Matrix;	
		
		private var mHighlightBorderColor:uint = 0xffffff;
		private var mHighlightOutlineColor:uint = 0xffffff;
		
		public function RoundRectButtonSprite(explicitWidth:Number, explicitHeight:Number, leftr:Boolean, rightr:Boolean, rclose:Boolean = true, pushed:Boolean = false)
		{
			createGradients(explicitHeight, pushed);
			
			mLeftRounded  = leftr;
			mRightRounded = rightr;
			mRightClosed  = rclose;
			redraw(explicitWidth, explicitHeight, pushed);
			
		}
		
		protected function createGradients(h:Number, pushed:Boolean):void
		{
			mGradColors = [0xf0f0f0, 0xdddddd];
			mGradAlphas = [1  , 1   ];
			mGradRatios = [0, 255];
			mGradMatrix = new Matrix();
			mGradMatrix.createGradientBox(h, h, Math.PI / 2, 0, 0);

			if (!pushed)
			{
				mHGradColors = [0xffffff, 0xffffff, 0xffffff];
				mHGradAlphas = [0.5, 0.3, 0];
				mHGradRatios = [0, 110, 111];
			}
			else
			{
				mHGradColors = [0,0];
				mHGradAlphas = [0.2, 0];
				mHGradRatios = [0, 90];
			}
			mHGradMatrix = new Matrix();
			mHGradMatrix.createGradientBox(h, h, Math.PI / 2, 0, 0);
		}
		
		public function redraw(w:Number, h:Number, pushed:Boolean):void
		{
			var g:Graphics = graphics;
			
			g.lineStyle();
			g.beginGradientFill(GradientType.LINEAR, mGradColors, mGradAlphas, mGradRatios, mGradMatrix);
			drawBorder(g, w, h, 0, false);
			g.endFill();

			
			g.beginFill(0,0);
			g.lineStyle(1, mBorderColor, 0.5, true);
			drawBorder(g, w, h, 0, !mRightClosed);
			g.endFill();
			
			drawLabel(g, w, h, pushed ? 1 : 0);
			
			g.lineStyle();
			g.beginGradientFill(GradientType.LINEAR, mHGradColors, mHGradAlphas, mHGradRatios, mHGradMatrix);
			drawBorder(g, w, h, 1, false);
			g.endFill();

			g.lineStyle(1, mHighlightOutlineColor, 0.8, true);
			drawBottom(g, w, h, 0, 1);

			g.lineStyle(1, mHighlightBorderColor, 0.5, true);
			drawBorder(g, w, h, 1, false);
			
			g.lineStyle(1, mHighlightOutlineColor, 0.4, true);
			drawBottom(g, w, h, 0, 2);
			
			if (pushed)
			{
				g.lineStyle(2, 0, 0.1, true);
				drawBorder(g, w, h, 0.5, false);
			
				g.lineStyle(3, 0, 0.05, true);
				drawBorder(g, w, h, 1, false);
			}

		}

		protected function drawLabel(g:Graphics, w:Number, h:Number, shift_y:Number):void {}
		
		protected function drawBorder(g:Graphics, w:Number, h:Number, padding:Number, opened:Boolean):void
		{
			if (mLeftRounded && mRightRounded)
			{
				g.moveTo(mR+padding, h-1-padding);
				roundedLeft(w, h, padding);
				g.lineTo(w-1-mR-padding, padding);
				roundedRight(w, h, padding);
			}
			else if (mLeftRounded)
			{
				g.moveTo(w-1-padding, h-1-padding);
				g.lineTo(mR+padding, h-1-padding);
				roundedLeft(w, h, padding);
				g.lineTo(w-1-padding, padding);
				if (!opened)
					g.lineTo(w-1-padding, h-1-padding);
			}
			else if (mRightRounded)
			{
				g.moveTo(padding, padding);
				g.lineTo(w-1-mR-padding, padding);
				roundedRight(w, h, padding);
				g.lineTo(padding, h-1-padding);
				
				if (!opened)
					g.lineTo(padding, padding);
			}
		}
		
		protected function drawBottom(g:Graphics, w:Number, h:Number, padding:Number, ys:Number):void
		{
			var A:Number = APOS*mR;
			if (mLeftRounded)
			{
				g.moveTo(padding+A   , h-1-padding - A   +ys);
				g.curveTo(padding+A*2, h-1-padding       +ys, mR+padding, h-1-padding +ys);
			}
			else
			{
				g.moveTo(padding, h-1-padding +ys);
			}

			if (mRightRounded)
			{
				g.lineTo( w-1-padding -mR , h-1-padding +ys);
				g.curveTo(w-1-padding -A*2, h-1-padding +ys, w-1-padding-A, h-1-padding-A +ys);
			}
			else
			{
				g.lineTo(w-1-padding, h-1-padding +ys);
			}
		}
		
		protected function roundedLeft(w:Number, h:Number, padding:Number):void
		{
			var A:Number = APOS*mR;
			var g:Graphics = graphics;
			
			g.curveTo(padding+A*2, h-1-padding, padding+A, h-1-padding - A);
			g.curveTo(padding, h-1-padding - A*2, padding, h-1-padding - mR);
			g.lineTo(padding, padding+mR);
			g.curveTo(padding, padding+A*2, padding+A, padding+A);
			g.curveTo(padding+A*2, padding, padding+mR, padding);
		}

		protected function roundedRight(w:Number, h:Number, padding:Number):void
		{
			var A:Number = APOS*mR;
			var g:Graphics = graphics;
			
			g.curveTo(w-1-padding-A*2, padding    , w-1-padding-A, padding+A);
			g.curveTo(w-1-padding    , padding+A*2, w-1-padding  , padding+mR);
			g.lineTo(w-1-padding, h-1-padding-mR);
			g.curveTo(w-1-padding, h-1-padding-A*2, w-1-padding-A, h-1-padding-A);
			g.curveTo(w-1-padding-A*2, h-1-padding, w-1-padding-mR, h-1-padding);
		}

	}
}