/**
 * Licensed under the MIT License
 * 
 * Copyright (c) 2008 BeInteractive! (www.be-interactive.org) and 
 *               2009 alumican.net (www.alumican.net) and 
 *               Spark project (www.libspark.org)
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package org.libspark.eseclock.object
{
	import caurina.transitions.Tweener;
	import flash.display.DisplayObject;
	import flash.display.Graphics;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	import flash.utils.getDefinitionByName;
	
	/**
	 * TweenMaskSprite.as
	 * マスクアニメーション付きSpriteのための基本クラス
	 * 
	 * @author	alumican.net<Yukiya Okuda>
	 * @link	http://alumican.net/
	 * @link	http://www.libspark.org/
	 */
	
	public class TweenMaskSprite extends Sprite
	{
		//-------------------------------------
		// VARIABLES
		//-------------------------------------
		
		//マスクのサイズ
		protected var _w:Number;
		protected var _h:Number;
		
		//マスクされるコンテンツや時計をaddChildしていく
		protected var _masked:Sprite;
		
		//マスク(アニメーションの方向を制御)
		private var _maskContainer:Sprite;
		
		//マスク(アニメーションの伸縮を制御)
		private var _mask:Sprite;
		
		//背景
		protected var _background:Shape;
		
		//背景色
		protected var _backgroundColor:uint;
		
		
		
		
		
		//-------------------------------------
		// CONSTRUCTOR
		//-------------------------------------
		
		/**
		 * コンストラクタ
		 * @param	w	幅
		 * @param	h	高さ
		 */
		public function TweenMaskSprite(w:Number, h:Number, backgroundColor:uint)
		{
			_w = w;
			_h = h;
			
			_masked = new Sprite();
			addChild(_masked);
			
			_createMask();
			
			//背景の生成
			_createBackground(backgroundColor);
		}
		
		
		
		
		
		//-------------------------------------
		// METHODS
		//-------------------------------------
		
		/**
		 * マスクのインスタンスを生成する関数
		 */
		private function _createMask():void
		{
			_maskContainer = new Sprite();
			_mask = new Sprite();
			
			addChild(_maskContainer);
			
			_maskContainer.addChild(_mask);
			
			_drawMask();
			
			_masked.mask = _maskContainer;
		}
		
		/**
		 * マスクを描画する関数
		 */
		private function _drawMask():void
		{
			_maskContainer.x = _w / 2;
			_maskContainer.y = _h / 2;
			
			_mask.x = -_w / 2;
			_mask.y = -_h / 2;
			
			_mask.graphics.clear();
			_mask.graphics.beginFill(0x0);
			_mask.graphics.drawRect(0, 0, _w, _h);
			_mask.graphics.endFill();
		}
		
		/**
		 * 背景ベタのシェイプを生成する関数
		 * @param	color	背景色
		 */
		private function _createBackground(color:uint):void
		{
			_background = new Shape();
			
			_drawBackground(color);
			
			_masked.addChild(_background);
		}
		
		/**
		 * 背景を描画する関数
		 * @param	color	背景色
		 */
		protected function _drawBackground(color:uint):void
		{
			_backgroundColor = color;
			
			var g:Graphics = _background.graphics;
			g.clear();
			g.beginFill(color);
			g.drawRect(0, 0, _w, _h);
			g.endFill();
		}
		
		/**
		 * 表示アニメーションを開始する関数
		 * @param	direction	アニメーションの方向[0, 3]
		 * @param	onComplete	アニメーション完了時に実行されるコールバック関数
		 */
		public function show(direction:uint, onComplete:Function = null):void
		{
			switch(direction) {
				
				//↓
				case 0:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = 1;
					_mask.scaleX = 1;
					_mask.scaleY = 0;
					break;
				
				//←
				case 1:
					_maskContainer.scaleX = -1;
					_maskContainer.scaleY = 1;
					_mask.scaleX = 0;
					_mask.scaleY = 1;
					break;
				
				//↑
				case 2:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = -1;
					_mask.scaleX = 1;
					_mask.scaleY = 0;
					break;
				
				//→
				case 3:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = 1;
					_mask.scaleX = 0;
					_mask.scaleY = 1;
					break;
			}
			
			Tweener.removeTweens(_mask);
			Tweener.addTween(_mask, {
				scaleX:1,
				scaleY:1,
				time:.5,
				transition:"easeOutExpo",
				onComplete:function():void {
					if (onComplete != null) onComplete();
				}
			});
		}
		
		/**
		 * 非表示アニメーションを開始する関数
		 * @param	direction	アニメーションの方向[0, 3]
		 * @param	onComplete	アニメーション完了時に実行されるコールバック関数
		 */
		public function hide(direction:uint, onComplete:Function = null):void
		{
			switch(direction) {
				
				//↓
				case 0:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = -1;
					break;
				
				//←
				case 1:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = 1;
					break;
				
				//↑
				case 2:
					_maskContainer.scaleX = 1;
					_maskContainer.scaleY = 1;
					break;
				
				//→
				case 3:
					_maskContainer.scaleX = -1;
					_maskContainer.scaleY = 1;
					break;
			}
			
			Tweener.removeTweens(_mask);
			Tweener.addTween(_mask, {
				scaleX:(direction % 2 == 0) ? 1 : 0,
				scaleY:(direction % 2 == 1) ? 1 : 0,
				time:.5,
				transition:"easeOutExpo",
				onComplete:function():void {
					if (onComplete != null) onComplete();
				}
			});
		}
		
		/**
		 * 現在の_wと_hに合わせてEseclockをリサイズする関数
		 * @param	w	幅
		 * @param	h	高さ
		 */
		public function resize(w:Number, h:Number):void
		{
			_w = w;
			_h = h;
			
			//マスクの再描画
			_drawMask();
			
			//背景のリサイズ
			_background.width  = _w;
			_background.height = _h;
		}
	}
}