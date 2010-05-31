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
package org.libspark.eseclock
{
	import flash.display.DisplayObject;
	import flash.display.Shape;
	import flash.display.Sprite;
	import flash.display.StageAlign;
	import flash.display.StageScaleMode;
	import flash.events.Event;
	import flash.text.TextField;
	import org.libspark.eseclock.object.ClockSprite;
	import org.libspark.eseclock.object.ContentSprite;
	import org.libspark.eseclock.object.TweenMaskSprite;
	
	/**
	 * Eseclockアニメーション付きバージョン
	 * 
	 ******************************************
	 * 
	 * これはなに？
	 *  - UNIQLOCKっぽい何かが作れるライブラリです
	 *  - yossy:beinteractive氏によるオリジナルバージョンを改造しています
	 * 
	 * @author	yossy:beinteractive
	 * @link	http://www.libspark.org/wiki/Eseclock
	 * @link	http://www.libspark.org/
	 * 
	 ******************************************
	 * 
	 * 改造してるひと
	 *  - alumican.net
	 * 
	 * @author	alumican.net
	 * @link	http://alumican.net
	 * 
	 ******************************************
	 * 
	 * つかいかた
	 *  - ステージにaddChildして使います
	 *  - コンストラクタには以下のパラメータを渡せます
	 *      第1引数  color1:uint = 0x000000				色1
	 *      第2引数  color2:uint = 0xffffff				色2
	 *      第3引数  w:Number = 640						Eseclockの幅
	 *      第4引数  h:Number = 320						Eseclockの高さ
	 *      第5引数  autoScaleToStage:Boolean = true	trueの場合は自動でステージにフィットする
	 *      第6引数  autoPlay:Boolean = true			trueの場合はaddChildと同時にスタートする. falseの場合はstartメソッドを呼び出すことスタートする
	 *      第7引数  leading:Number = 0					時計と下のテキストとの間隔
	 *      第7引数  leading:Number = 0					時計と下のテキストとの間隔
	 *      第8引数  textFieldAsset1:String = ""		時計表示用に用いるクラス名(IEseclockTextFieldを実装する必要がある)
	 *      第9引数  textFieldAsset2:String = ""		時計の下のテキストに用いるクラス名(IEseclockTextFieldを実装する必要がある)
	 * 
	 *  - こんな感じのコードになります
	 *  - MyEseclockはEseclockを継承し, createContentメソッド及びresizeContentメソッドを適宜オーバーライドしています
	 * 
	 * var clock:MyEseclock = new MyEseclock();
	 * addChild(clock);
	 * 
	 * clock.w = 800;
	 * clock.h = 600;
	 * clock.description = "TOKYO / JAPAN";
	 * 
	 ******************************************
	 * 
	 * ライセンス
	 *  - MITライセンスです
	 */
	
	public class Eseclock extends Sprite
	{
		//--------------------------------------------------------------------------
		// COLORS
		//
		// 色を取得/設定します
		//--------------------------------------------------------------------------
		
		private var _color1:uint;
		private var _color2:uint;
		
		public function get color1():uint { return _color1; }
		public function get color2():uint { return _color2; }
		public function set color1(value:uint):void { _color1 = value; _coloring1(); }
		public function set color2(value:uint):void { _color2 = value; _coloring2(); }
		
		
		
		
		
		//--------------------------------------------------------------------------
		// SIZE
		//
		// Eseclockのサイズを取得/設定します
		//--------------------------------------------------------------------------
		
		private var _w:Number;
		private var _h:Number;
		
		public function get w():Number { return _w; }
		public function get h():Number { return _h; }
		public function set w(value:Number):void { if (value != _w) { _w = value; _resize(); } }
		public function set h(value:Number):void { if (value != _h) { _h = value; _resize(); } }
		
		
		
		
		
		//--------------------------------------------------------------------------
		// SCALE TO STAGE
		//
		// trueの場合, Eseclockのサイズをステージにフィットさせます
		//--------------------------------------------------------------------------
		
		private var _autoScaleToStage:Boolean;
		
		public function get autoScaleToStage():Boolean { return _autoScaleToStage; }
		public function set autoScaleToStage(value:Boolean):void {
			if (value != _autoScaleToStage) {
				_autoScaleToStage = value;
				_resize();
			}
		}
		
		
		
		
		
		//--------------------------------------------------------------------------
		// CLOCK DESCRIPTION
		//
		// 時計の下に表示するテキストを取得/設定します
		//--------------------------------------------------------------------------
		
		public function get description():String { return _description; }
		public function set description(value:String):void
		{
			_description = value;
			_clock1.updateDescription(value);
			_clock2.updateDescription(value);
		}
		
		private var _description:String = "TOKYO / JAPAN";
		
		
	
		
		
		//--------------------------------------------------------------------------
		// GET SHOWING CONTENT
		//
		// 表示中のコンテンツを取得します
		//--------------------------------------------------------------------------
		
		public function get content():DisplayObject { return _contentContainer.content; }
		
		
		
		
		
		//--------------------------------------------------------------------------
		// CREATE CONTENT METHOD
		//
		// 時計の合間に表示するコンテンツを設定します
		// 
		// _createContentメソッドをオーバーライドするか, createContentに関数を代入します. 
		//--------------------------------------------------------------------------
		
		private var __createContent:Function;
		
		//Setter経由で設定している場合は, オーバーライドされた関数を実行しません
		public function get createContent():Function { return __createContent || _createContent; }
		public function set createContent(value:Function):void { __createContent = value; }
		
		/**
		 * 時計の合間に表示するコンテンツのインスタンスを生成する関数(オーバーライド用)
		 * @param	w	Eseclockの幅
		 * @param	h	Eseclockの高さ
		 * @return	時計の合間に表示するコンテンツ
		 */
		protected function _createContent(w:Number, h:Number):DisplayObject
		{
			var sprite:Sprite = new Sprite();
			sprite.graphics.clear();
			for (var i:uint = 0; i < 40; ++i) {
				sprite.graphics.beginFill(Math.floor(Math.random() * 256), Math.random() * 100);
				sprite.graphics.drawCircle(Math.random() * w, Math.random() * h, Math.random() * 20 + 30);
				sprite.graphics.endFill();
			}
			return sprite;
		}
		
		
		
		
		
		//--------------------------------------------------------------------------
		// REMOVE CONTENT METHOD
		//
		// 時計の合間に表示するコンテンツが削除される直前に呼び出されます
		// 
		// _removeContentメソッドをオーバーライドするか, removeContentに関数を代入します. 
		//--------------------------------------------------------------------------
		
		private var __removeContent:Function;
		
		//Setter経由で設定している場合は, オーバーライドされた関数を実行しません
		public function get removeContent():Function { return __removeContent || _removeContent; }
		public function set removeContent(value:Function):void { __removeContent = value; }
		
		/**
		 * 時計の合間に表示するコンテンツが削除される直前に呼び出される関数(オーバーライド用)
		 * @param	content	表示中のコンテンツ
		 */
		protected function _removeContent(content:DisplayObject):void
		{
		}
		
		
		
		
		
		//--------------------------------------------------------------------------
		// RESIZE CONTENT METHOD
		//
		// Eseclockのリサイズに合わせてコンテンツをリサイズする関数を設定します
		// 
		// _resizeContentメソッドをオーバーライドするか, resizeContentに関数を代入します. 
		//--------------------------------------------------------------------------
		
		private var __resizeContent:Function;
		
		//Setter経由で設定している場合は, オーバーライドされた関数を実行しません
		public function get resizeContent():Function { return __resizeContent || _resizeContent; }
		public function set resizeContent(value:Function):void { __resizeContent = value; }
		
		
		/**
		 * Eseclockのリサイズに合わせてコンテンツをリサイズする関数(オーバーライド用)
		 * @param	content	コンテンツ
		 * @param	w		Eseclockの幅
		 * @param	h		Eseclockの高さ
		 */
		protected function _resizeContent(content:DisplayObject, w:Number, h:Number):void
		{
			content.width  = w;
			content.height = h;
		}
		
		
		
		
		
		//--------------------------------------------------------------------------
		// TICK METHOD
		//
		// 毎秒呼び出されます
		// 
		// _tickメソッドをオーバーライドするか, tickに関数を代入します. 
		//--------------------------------------------------------------------------
		
		private var __tick:Function;
		
		//Setter経由で設定している場合は, オーバーライドされた関数を実行しません
		public function get tick():Function { return __tick || _tick; }
		public function set tick(value:Function):void { __tick = value; }
		
		/**
		 * 毎秒呼び出される関数(オーバーライド用)
		 * @param	h	時
		 * @param	m	分
		 * @param	s	秒
		 */
		protected function _tick(h:uint, m:uint, s:uint):void
		{
			//trace(h + ":" + m + ":" + s);
		}
		
		
		
		
		
		//-------------------------------------
		// VARIABLES
		//-------------------------------------
		
		private var _autoPlay:Boolean;
		private var _isPlaying:Boolean;
		
		private var _leading:Number;
		
		private var _clock1:ClockSprite;
		private var _clock2:ClockSprite;
		private var _contentContainer:ContentSprite;
		
		private var _prevDate:Date;
		
		/* 時計/コンテンツの表示/非表示アニメーションの方向
		 * 
		 * (0, 1, 2, 3) = (↓, ←, ↑, →)
		 * 
		 * 表示するとき     ･･･ 矢印の方向へマスクが拡大する
		 * 非表示にするとき ･･･ 矢印の方向へマスクが縮小する
		 */
		private var _direction:uint;
		
		private var _textFieldAsset1:String;
		private var _textFieldAsset2:String;
		
		
		
		
		
		//-------------------------------------
		// CONSTRUCTOR
		//-------------------------------------
		
		/**
		 * コンストラクタ
		 * @param	color1	色1
		 * @param	color2	色2
		 * @param	w	Eseclockの幅  (0でステージにフィットする)
		 * @param	h	Eseclockの高さ(0でステージにフィットする)
		 * @param	autoPlay	自動再生
		 * @param	textField1	時計部分のTextField
		 * @param	textField2	文字部分のTextField
		 */
		public function Eseclock(color1:uint = 0x000000,
		                         color2:uint = 0xffffff,
		                         w:Number = 640,
		                         h:Number = 320,
		                         autoScaleToStage:Boolean = true,
		                         autoPlay:Boolean = true,
		                         leading:Number = 0,
		                         textFieldAsset1:String = "",
		                         textFieldAsset2:String = "")
		{
			_color1 = color1;
			_color2 = color2;
			
			_w = w;
			_h = h;
			
			_autoScaleToStage = autoScaleToStage;
			
			_autoPlay = autoPlay;
			_isPlaying = false;
			
			_leading = leading;
			
			_textFieldAsset1 = textFieldAsset1;
			_textFieldAsset2 = textFieldAsset2;
			
			addEventListener(Event.ADDED_TO_STAGE, _addedToStageHandler);
		}
		
		
		
		
		
		//-------------------------------------
		// METHODS
		//-------------------------------------
		
		/**
		 * 現在の_wと_hに合わせてEseclockをリサイズする関数
		 * @param	coercively	強制
		 */
		private function _resize(coercively:Boolean = false):void
		{
			if (!coercively && _autoScaleToStage) return;
			
			var w:Number = (_autoScaleToStage) ? stage.stageWidth  : _w;
			var h:Number = (_autoScaleToStage) ? stage.stageHeight : _h;
			
			_clock1.resize(w, h);
			_clock2.resize(w, h);
			_contentContainer.resize(w, h);
			
			if (_contentContainer.content != null) {
				resizeContent(_contentContainer.content, w, h);
			}
		}
		
		/**
		 * 現在の_color1と_color2に合わせて色づけをおこなう関数
		 */
		private function _coloring1():void
		{
			_clock1.textColor       = _color1;
			_clock2.backgroundColor = _color1;
		}
		
		private function _coloring2():void
		{
			_clock2.textColor       = _color2;
			_clock1.backgroundColor = _color2;
		}
		
		/**
		 * 数値を2桁に桁揃えするstaticな関数
		 * @param	n		桁揃え前の数値
		 * @param	digit	桁数
		 * @return	桁揃え後のString
		 */
		public static function toDigitString(n:uint, digit:uint = 2):String
		{
			var s:String = n.toString();
			while (s.length < digit) s = "0" + n;
			return s;
		}
		
		
		
		
		
		//-------------------------------------
		// EVENT HANDLER
		//-------------------------------------
		
		/**
		 * ステージに配置されたときに呼び出されるイベントハンドラ(初期化用)
		 * @param	e
		 */
		private function _addedToStageHandler(e:Event):void
		{
			removeEventListener(Event.ADDED_TO_STAGE, _addedToStageHandler);
			
			var w:Number = (_w == 0) ? stage.stageWidth  : _w;
			var h:Number = (_h == 0) ? stage.stageHeight : _h;
			
			var clock1:ClockSprite = new ClockSprite(_color1, _color2, w, h, _leading, _textFieldAsset1, _textFieldAsset2);
			var clock2:ClockSprite = new ClockSprite(_color2, _color1, w, h, _leading, _textFieldAsset1, _textFieldAsset2);
			var contentContainer:ContentSprite = new ContentSprite(w, h);
			
			_clock1 = clock1;
			_clock2 = clock2;
			_contentContainer = contentContainer;
			
			addChild(clock1);
			addChild(clock2);
			addChild(contentContainer);
			
			//stageの設定
			if (_autoScaleToStage) {
				stage.align = StageAlign.TOP_LEFT;
				stage.scaleMode = StageScaleMode.NO_SCALE;
				trace("INFO: autoScaleToStage=true : Eseclock has changed the Stage scale mode.");
			}
			
			//最初は左から右へアニメーションさせる
			_direction = 3;
			
			//最初に表示する時刻
			var date:Date = new Date();
			_clock1.updateField(date.hours, date.minutes, date.seconds);
			_clock2.updateField(date.hours, date.minutes, date.seconds);
			
			//最初に表示するテキスト
			_clock1.updateDescription(_description);
			_clock2.updateDescription(_description);
			
			//自動開始
			if (_autoPlay) {
				start();
			}
			
			_resize(true);
			stage.addEventListener(Event.RESIZE, _resizeHandler);
		}
		
		/**
		 * 開始
		 */
		public function start():void {
			if (_isPlaying) return;
			_isPlaying = true;
			
			_prevDate = new Date();
			_update();
			addEventListener(Event.ENTER_FRAME, _update);
		}
		
		/**
		 * 毎フレーム時計が切り替わるタイミングをチェックするイベントハンドラ関数
		 * @param	e
		 */
		private function _update(e:Event = null):void
		{
			var date:Date = new Date();
			
			var h:uint = date.hours;
			var m:uint = date.minutes;
			var s:uint = date.seconds;
			
			//前回の更新から1秒経っていれば
			if (s != _prevDate.seconds) {
				
				//1秒の時点でコンテンツを非表示にするアニメーションを開始する
				if (s % 10 == 1) {
					_contentContainer.hide(_direction,
						function():void {
							//アニメーション完了時にコンテンツを削除する
							if (_contentContainer.content != null) {
								removeContent(_contentContainer.content);
								_contentContainer.removeContent();
							}
						}
					);
				}
				
				//6秒の時点でコンテンツをステージ上に配置し, 表示アニメーションを開始する
				if (s % 10 == 6) {
					_contentContainer.addContent( createContent(stage.stageWidth, stage.stageHeight) );
					_contentContainer.show(_direction);
				}
				
				//コンテンツが表示されていない状態なら
				if (_contentContainer.content == null) {
					
					//1秒ごとに時計を入れ替える(アクティブな方を上に重ねていく)
					//if (s % 2 == 0) {
					if (_clock1.visible) {
						_clock2.visible = true;
						
						_clock2.show(_direction,
							function():void {
								_clock1.visible = false;
							}
						);
						
						addChildAt(_clock2, 1);
					}
					else {
						_clock1.visible = true;
						
						_clock1.show(_direction,
							function():void {
								_clock2.visible = false;
							}
						);
						
						addChildAt(_clock1, 1);
					}
				}
				
				//文字盤の更新
				_clock1.updateField(h, m, s);
				_clock2.updateField(h, m, s);
				
				tick(h, m, s);
				
				//アニメーション方向の更新
				_direction = (++_direction % 4 == 0) ? 0 : _direction;
			}
			
			_prevDate = date;
		}
		
		/**
		 * ステージがリサイズされたときに呼び出されるイベントハンドラ
		 * @param	e
		 */
		private function _resizeHandler(e:Event):void {
			if (_autoScaleToStage) _resize(true);
		}
	}
}
