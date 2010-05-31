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
	 * ContentSprite.as
	 * 時計の合間に表示するコンテンツ
	 *
	 * @author	alumican.net<Yukiya Okuda>
	 * @link	http://alumican.net/
	 * @link	http://www.libspark.org/
	 */
	
	public class ContentSprite extends TweenMaskSprite
	{
		//-------------------------------------
		// VARIABLES
		//-------------------------------------
		
		//コンテンツ
		private var _content:DisplayObject;
		
		
		
		
		
		//-------------------------------------
		// GETTER/SETTER
		//-------------------------------------
		
		//コンテンツ
		public function get content():DisplayObject { return _content; }
		
		
		
		
		
		//-------------------------------------
		// CONSTRUCTOR
		//-------------------------------------
		
		/**
		 * コンストラクタ
		 * @param	w	幅
		 * @param	h	高さ
		 */
		public function ContentSprite(w:Number, h:Number)
		{
			//背景はベタ塗りで真っ白
			super(w, h, 0xffffff);
			
			//背景を非表示にしておく
			_background.visible = false;
		}
		
		
		
		
		
		//-------------------------------------
		// METHODS
		//-------------------------------------
		
		/**
		 * コンテンツをステージに配置関数
		 * @param	content	コンテンツ
		 */
		public function addContent(content:DisplayObject):void
		{
			removeContent();
			
			_content = content;
			_masked.addChild(_content);
			
			_background.visible = true;
		}
		
		/**
		 * コンテンツをステージから削除する関数
		 */
		public function removeContent():void
		{
			if (_content == null) return;
			
			_masked.removeChild(_content);
			_content = null;
			
			_background.visible = false;
		}
	}
}