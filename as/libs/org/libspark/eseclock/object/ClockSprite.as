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
	
	import org.libspark.eseclock.textfield.EseclockDefaultClockTextField;
	import org.libspark.eseclock.textfield.EseclockDefaultDescriptionTextField;
	import org.libspark.eseclock.textfield.IEseclockTextField;
	
	/**
	 * ClockSprite.as
	 * 時計とその下のテキスト
	 * 
	 * @author	alumican.net<Yukiya Okuda>
	 * @link	http://alumican.net/
	 * @link	http://www.libspark.org/
	 */
	
	public class ClockSprite extends TweenMaskSprite
	{
		//-------------------------------------
		// VARIABLES
		//-------------------------------------
		
		//時計のテキストフィールド
		private var _field:IEseclockTextField;
		
		//時計の下に表示するテキストフィールド
		private var _sub:IEseclockTextField;
		
		//行間
		private var _leading:Number;
		
		//テキストが空文字列以外の場合はtrue
		private var _hasDescription:Boolean;
		
		
		
		
		
		//-------------------------------------
		// GETTER/SETTER
		//-------------------------------------
		
		//テキスト色
		public function set textColor(value:uint):void {
			_changeTextColor(_field, value);
			_changeTextColor(_sub  , value);
		}
		
		//背景色
		public function set backgroundColor(value:uint):void { _drawBackground(value); }
		
		
		
		
		
		//-------------------------------------
		// CONSTRUCTOR
		//-------------------------------------
		
		/**
		 * コンストラクタ
		 * @param	textColor		テキスト色
		 * @param	backgroundColor	背景色
		 * @param	w				幅
		 * @param	h				高さ
		 */
		public function ClockSprite(textColor:uint,
									backgroundColor:uint,
									w:Number,
									h:Number,
									leading:Number,
									clockAsset:String = "",
									subAsset:String = "")
		{
			super(w, h, backgroundColor);
			
			_leading = leading;
			
			_createFields(textColor, clockAsset, subAsset);
		}
		
		
		
		
		
		//-------------------------------------
		// METHODS
		//-------------------------------------
		
		/**
		 * テキストフィールドを生成する関数
		 * @param	color	テキスト色
		 */
		private function _createFields(color:uint, clockAsset:String = "", subAsset:String = ""):void
		{
			_field = _createField(clockAsset, EseclockDefaultClockTextField);
			_field.setColor(color);
			_field.updateClock(99, 99, 99);
			
			_masked.addChild(_field as DisplayObject);
			
			
			_sub = _createField(subAsset, EseclockDefaultDescriptionTextField);
			_sub.setColor(color);
			_sub.updateDescription("TOKYO / JAPAN");
			
			_masked.addChild(_sub as DisplayObject);
			
			
			//中央揃え
			resize(_w, _h);
		}
		
		/**
		 * 各テキストフィールドを生成する関数
		 * @param	asset
		 * @param	defaultClass
		 */
		private function _createField(asset:String, defaultClass:Class):IEseclockTextField {
			var tf:IEseclockTextField;
			
			if (asset == "") {
				tf = new defaultClass() as IEseclockTextField;
			} else {
				var fieldClass:Class = getDefinitionByName(asset) as Class;
				tf = new fieldClass() as IEseclockTextField;
			}
			
			return tf;
		}
		
		/**
		 * 時計の下に表示するテキストを更新する関数
		 * @param	description	テキスト
		 */
		public function updateDescription(description:String):void
		{
			_hasDescription = (description != "") ? true : false;
			
			_sub.updateDescription(description);
			
			//中央揃え
			resize(_w, _h);
		}
		
		/**
		 * 文字盤の表示を更新する関数
		 * @param	h	時
		 * @param	m	分
		 * @param	s	秒
		 */
		public function updateField(h:uint, m:uint, s:uint):void
		{
			_field.updateClock(h, m, s);
		}
		
		/**
		 * テキストフィールドの色を変更する関数
		 * @param	tf	ターゲット
		 * @param	color		色
		 */
		private function _changeTextColor(tf:IEseclockTextField, color:uint):void
		{
			tf.setColor(color);
		}
		
		/**
		 * 現在の_wと_hに合わせてEseclockをリサイズする関数
		 * @param	w	幅
		 * @param	h	高さ
		 */
		override public function resize(w:Number, h:Number):void
		{
			super.resize(w, h);
			
			//テキストフィールドの中央揃え
			var margin:int = (_hasDescription) ? _leading : 0;
			var totalHeight:uint = _field.objectHeight + _sub.objectHeight;
			
			_field.x = (_w - _field.objectWidth) / 2;
			_field.y = (_h - totalHeight       ) / 2;
			
			_sub.x = (_w - _sub.objectWidth) / 2;
			_sub.y = (_h - totalHeight     ) / 2 + _field.objectHeight + margin;
		}
	}
}