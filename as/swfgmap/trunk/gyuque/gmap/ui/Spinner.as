package gyuque.gmap.ui
{
	import flash.display.*;
	import flash.events.*;
	import flash.geom.Matrix;
	import mx.events.SliderEvent;
	
	public class Spinner extends Sprite
	{
		private var mSize:int;
		private var mBaseRing:Sprite;
		private var mCaptureRing:Sprite;
		private var mCursor:Sprite;
		
		private var mResetBtn:SpinResetButton;
		
		private var mRGradColors:Array;
		private var mRGradAlphas:Array;
		private var mRGradRatios:Array;
		private var mRGradMatrix:Matrix;
		
		private var mValue:Number;
		
		private var mDrag:DragData = new DragData();
		
		public function Spinner(sz:int)
		{
			mRGradColors = [0xe0e0e0, 0xf5f5f5, 0xffffff, 0xe4e4e4];
			mRGradAlphas = [1  , 1   , 1  , 1];
			mRGradRatios = [150, 180 , 200, 255];
			mRGradMatrix = new Matrix();
			mRGradMatrix.createGradientBox(sz*1.05, sz*1.05, 0, -sz*0.06, -sz*0.06);
			
			mSize = sz;
			mBaseRing = new Sprite();
			mCursor = new Sprite();
			drawBaseRing(mBaseRing.graphics, mCursor.graphics, graphics);
			
			mCaptureRing = new Sprite();
			mCaptureRing.graphics.beginFill(0);
			mCaptureRing.graphics.drawCircle(sz/2, sz/2, sz);
			mCaptureRing.mouseEnabled = false;
			mCaptureRing.visible = false;
			addChild(mCaptureRing);
			
			mBaseRing.addChild(mCursor);
			mCursor.x = sz/2;
			mCursor.y = sz/2;
			mCursor.mouseEnabled = false;
			
			mBaseRing.addEventListener(MouseEvent.MOUSE_MOVE , onRingMouseMove);
			mBaseRing.addEventListener(MouseEvent.MOUSE_DOWN , onRingMouseDown);
			mBaseRing.addEventListener(MouseEvent.MOUSE_UP   , onRingMouseUp);
			mBaseRing.addEventListener(MouseEvent.MOUSE_OUT  , onRingMouseOut);
			
			mResetBtn = new SpinResetButton();
			mResetBtn.x = sz/2;
			mResetBtn.y = sz/2;
			addChild(mResetBtn);
			mBaseRing.buttonMode = true;
			mBaseRing.useHandCursor = true;
			
			addChild(mBaseRing);
			
			mValue = 0;
		}
		
		public function get centerButton():SimpleButton
		{
			return mResetBtn;
		}
		
		protected function onRingMouseMove(e:MouseEvent):void
		{
			e.stopPropagation();
			
			if (mDrag.dragging) {
				mDrag.update(e.localX - mSize/2, e.localY - mSize/2);
				
				mValue += mDrag.dRad;
				var se:SliderEvent = new SliderEvent(SliderEvent.THUMB_DRAG, false, false, -1, mValue);
				dispatchEvent(se);
				updateCursor(mValue);
			}
		}
		
		public function set value(v:Number):void
		{
			mValue = v;
			updateCursor(mValue);
		}

		public function get value():Number
		{
			return mValue;
		}
		
		protected function updateCursor(r:Number):void
		{
			mCursor.rotation = r * 180 / Math.PI;
		}

		protected function onRingMouseDown(e:MouseEvent):void
		{
			e.stopPropagation();
			
			mDrag.dragging = true;
			mBaseRing.hitArea = mCaptureRing;
			mDrag.update(e.localX - mSize/2, e.localY - mSize/2);
		}
		
		protected function onRingMouseUp(e:MouseEvent):void
		{
			e.stopPropagation();
			endDrag();
		}

		protected function onRingMouseOut(e:MouseEvent):void
		{
			e.stopPropagation();
			endDrag();
		}
		
		protected function endDrag():void
		{
			mDrag.dragging = false;
			mBaseRing.hitArea = null;
		}
		
		private function drawBaseRing(g:Graphics, c_g:Graphics, sh_g:Graphics):void
		{
			var c:int = mSize/2;
			var i:int;

			sh_g.lineStyle();
			for (i = 0;i < 2;i++)
			{
				sh_g.beginFill(0, 0.05);
				sh_g.drawCircle(c+1, c+2, mSize/2   +1-i);
				sh_g.drawCircle(c+1, c+2, mSize/3.6 -1+i);
				sh_g.endFill();
			}
			
			g.beginGradientFill(GradientType.RADIAL, mRGradColors, mRGradAlphas, mRGradRatios, mRGradMatrix);
			g.lineStyle(1, 0x666666);
			g.drawCircle(c, c, mSize/2);
			g.drawCircle(c, c, mSize/3.6);
			g.endFill();

			for (i = 0;i < 2;i++)
			{
				if (!i) {
					c_g.beginFill(0, 0.2);
					c_g.lineStyle(2, 0xcccccc, 0.4);
				} else {
					c_g.beginFill(0xffffff, 0.26);
					c_g.lineStyle();
				}
				
				c_g.moveTo(0         , -mSize*0.44 );
				c_g.lineTo( mSize*0.07,-mSize*0.44 + mSize*0.06);
				c_g.lineTo(-mSize*0.07,-mSize*0.44 + mSize*0.06);
				c_g.endFill();
			}
			
			var a:Number;
			var R1:Number = c*0.75;
			var R2:Number = c*0.88;
			for (var k:int = 0;k < 2;k++)
			{
				c_g.lineStyle(1, k ? 0xffffff : 0xcccccc, 0.5);
				for (i = 0;i < 41;i++)
				{
					a = (Number(i)/40.0 * 0.9 + 0.05)*Math.PI*2.0;
					var C:Number = Math.cos(a);
					var S:Number = Math.sin(a);
					
					c_g.moveTo(S*R1, -C*R1);
					c_g.lineTo(S*R2, -C*R2);
				}
				
				R2 *= 0.95;
			}
		}
	}
}

class DragData
{
	public var dragging:Boolean = false;
	public var prevAngle:Number;
	public var dRad:Number;
	public var prevRad:Number;
	public function update(x:Number, y:Number):void {
		var r:Number = Math.atan2(y, x);
		dRad = r - prevRad;
		prevRad = r;
	}
}

class SpinResetButton extends flash.display.SimpleButton
{
	import flash.display.*;
	
	public function SpinResetButton()
	{
		var s:Sprite = new SpinResetButtonSprite(16, true);
		upState = s;
		hitTestState = upState;
		overState = s;
		downState = new SpinResetButtonSprite(16);
		downState.y = 1;
	}
}

class SpinResetButtonSprite extends flash.display.Sprite
{
	import flash.display.*;
	
	protected var mBGradColors:Array;
	protected var mBGradAlphas:Array;
	protected var mBGradRatios:Array;
	protected var mBGradMatrix:flash.geom.Matrix;
	protected var mBorderColor:uint = 0x999999;

	protected var mHGradColors:Array;
	protected var mHGradAlphas:Array;
	protected var mHGradRatios:Array;
	protected var mHGradMatrix:flash.geom.Matrix;
	
	protected var mSize:Number;
	
	public function SpinResetButtonSprite(sz:Number, shadowing:Boolean = false)
	{
		mSize = sz;
		createGradientData(sz);
		var g:Graphics = graphics;

		if (shadowing)
			drawShadow(g, sz);
		
		g.beginGradientFill(GradientType.RADIAL, mBGradColors, mBGradAlphas, mBGradRatios, mBGradMatrix);
		g.lineStyle(1, mBorderColor);
		g.drawCircle(0, 0, sz);
		g.endFill();
		drawHighlight(g, sz);
	}

	protected function drawShadow(g:Graphics, sz:Number):void
	{
		g.beginFill(0, 0.1);
		g.lineStyle(1, 0, 0.1);
		g.drawCircle(1, 2, sz);
		g.endFill();
	}
	
	protected function drawHighlight(g:Graphics, sz:Number):void
	{
		g.beginGradientFill(GradientType.RADIAL, mHGradColors, mHGradAlphas, mHGradRatios, mHGradMatrix);
		g.lineStyle();
		g.drawCircle(0, 0, sz*0.9);
	}
	
	protected function createGradientData(sz:Number):void
	{
		mBGradColors = [0xf0f0f0, 0xe3e3e3, 0xeeeeee, 0xffffff, 0xd0d0d0];
		mBGradAlphas = [1,1,1,1,1];
		mBGradRatios = [0, 190, 200, 218, 255];
		mBGradMatrix = new flash.geom.Matrix();
		mBGradMatrix.createGradientBox(sz*2, sz*2, 0, -sz, -sz*1.1);

		mHGradColors = [0xffffff, 0xffffff, 0xffffff];
		mHGradAlphas = [0,0.4,1];
		mHGradRatios = [70, 80, 240];
		mHGradMatrix = new flash.geom.Matrix();
		mHGradMatrix.createGradientBox(sz*8, sz*4, 0, -sz*3.9, -sz*1.4);
	
	}
}
