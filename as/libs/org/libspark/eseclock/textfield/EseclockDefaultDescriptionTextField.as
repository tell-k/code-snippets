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
package org.libspark.eseclock.textfield
{
	import flash.display.Sprite;
	import flash.text.TextField;
	import flash.text.TextFieldAutoSize;
	import flash.text.TextFormat;
	
	import org.libspark.eseclock.Eseclock;
	
	/**
	 * EseclockDefaultTextField.as
	 * デフォルトで表示するテキスト
	 *
	 * @author	alumican.net<Yukiya Okuda>
	 * @link	http://alumican.net/
	 * @link	http://www.libspark.org/
	 */
	
	public class EseclockDefaultDescriptionTextField extends Sprite implements IEseclockTextField
	{
		
		//-------------------------------------
		// CLASS CONSTANTS
		//-------------------------------------
		
		
		
		
		
		//-------------------------------------
		// VARIABLES
		//-------------------------------------
		
		protected var _field:TextField;
		
		
		
		
		
		//-------------------------------------
		// GETTER/SETTER
		//-------------------------------------
		
		
		
		
		
		//-------------------------------------
		// STAGE INSTANCES
		//-------------------------------------
		
		
		
		
		
		//-------------------------------------
		// GETTER/SETTER
		//-------------------------------------
		
		public function get objectWidth():Number { return _field.textWidth; }
		public function get objectHeight():Number { return _field.textHeight; }
		
		
		
		
		
		//-------------------------------------
		// CONSTRUCTOR
		//-------------------------------------
		
		/**
		 * コンストラクタ
		 */
		public function EseclockDefaultDescriptionTextField()
		{
			_field = new TextField();
			
			_field.defaultTextFormat = new TextFormat("Arial Black", 36, null, true);
			_field.selectable = false;
			_field.autoSize = TextFieldAutoSize.LEFT;
			
			addChild(_field);
		}
		
		
		
		
		
		//-------------------------------------
		// METHODS
		//-------------------------------------
		
		/**
		 * 色を設定する関数
		 * @param	h	時
		 * @param	m	分
		 * @param	s	秒
		 */
		public function setColor(color:uint):void
		{
			var fmt:TextFormat = _field.defaultTextFormat;
			fmt.color = color;
			_field.defaultTextFormat = fmt;
		}
		
		/**
		 * 時計表示を更新する関数
		 * @param	h	時
		 * @param	m	分
		 * @param	s	秒
		 */
		public function updateClock(h:uint, m:uint, s:uint):void
		{
		}
		
		/**
		 * テキストを更新する関数
		 * @param	message	表示文字列
		 */
		public function updateDescription(message:String):void
		{
			_field.text = message;
		}
		
		
		
		
		
		//-------------------------------------
		// EVENT HANDLER
		//-------------------------------------
	}
}