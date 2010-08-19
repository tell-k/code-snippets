package com.github.tell_k.naviqlock
{
    import flash.display.DisplayObject;
    import flash.display.Sprite;
    import flash.display.BitmapData;
    import flash.events.Event;
    import flash.display.Loader;
    import flash.filters.DropShadowFilter;
    import flash.net.URLRequest;
    import mx.formatters.DateFormatter;
    import org.libspark.eseclock.Eseclock;

    public class Naviqlock extends Eseclock
    {
        private var sprite:Sprite;

        public function Naviqlock()
        {
            super(uint(Math.random() * 0xffffff), 0xffffff);
            //super(0xd10000, 0xffffff);
        }

        override protected function _createContent(w:Number, h:Number):DisplayObject
        {
            sprite = new Sprite();

            sprite.graphics.beginFill(0xffffff);
            sprite.graphics.drawRect(0, 0, w, h);
            sprite.graphics.endFill();

            for (var i:uint = 0; i < 20; ++i) {
                sprite.graphics.beginFill(0xd10000, Math.random());
                sprite.graphics.drawCircle(Math.random() * w, Math.random() * h, Math.random() * 20 + 30);
                sprite.graphics.endFill();
            }

            //var baseURL:String = './images/';
            var baseURL:String = 'http://localhost/~tell_k/images/';

            var now:Date = new Date()
            var formatter:DateFormatter = new DateFormatter();
            formatter.formatString = 'KK00';
            
            var timeStr:String = formatter.format(now);
            var numStr:Number = uint(Math.random() * 4) + 1;
            var loader:Loader = new Loader();
            var request:URLRequest = new URLRequest(baseURL + timeStr + '-' + numStr + '.JPG');
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, resize);
            loader.load(request);
            sprite.addChild(loader);
            return sprite;
            
        }

        public function resize(e:Event) :void
        {
              var img_yx:Number = e.target.loader.height / e.target.loader.width;

              e.target.loader.width  = stage.stageWidth / 2; 
              e.target.loader.height = e.target.loader.width * img_yx; 
              e.target.loader.x = e.target.loader.width / 2;
              e.target.loader.y = (stage.stageHeight - e.target.loader.height) / 2; 

              var drawRectClosure:Function = function(color:uint):void {
                sprite.graphics.beginFill(color);
                sprite.graphics.drawRect(e.target.loader.x-10, e.target.loader.y-10, e.target.loader.width +20, e.target.loader.height+20);
                sprite.graphics.endFill();
              };
              drawRectClosure(0xEFEFEF);
              sprite.filters = [new DropShadowFilter];

        }

    }
}
