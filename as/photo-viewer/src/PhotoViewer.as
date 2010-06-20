package {
    import flash.display.Sprite;
    import photo.Photo;
    import flash.display.StageAlign;
    import flash.display.StageScaleMode;
    import flash.events.FocusEvent;
    import flash.display.DisplayObject;
    import flash.events.KeyboardEvent;
    import flash.display.InteractiveObject;
    import flash.ui.Keyboard;

    public class PhotoViewer extends Sprite {
        public const IMAGES:XML = <images>
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070718/20070718180931.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070719/20070719172803.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070720/20070720145354.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070721/20070721154931.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070723/20070723145925.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070723/20070723173541.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070723/20070723185513.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070721/20070721203341.jpg" />
            <image src="http://f.hatena.ne.jp/images/fotolife/s/secondlife/20070721/20070721153621.jpg" />
            </images>;

        public function PhotoViewer():void {
            stage.align = StageAlign.TOP_LEFT;
            stage.scaleMode = StageScaleMode.NO_SCALE;
            stage.stageFocusRect = false;
            createPhotosFromXML(IMAGES);
            stage.addEventListener(KeyboardEvent.KEY_DOWN, keyDownHandler);
        }

        public function createPhotosFromXML(images:XML):void {
            for each(var src:String in images.image.@src ) {
                createPhoto(src);
            }
        }

        public function createPhoto(url:String):void {
            var p:Photo = new Photo();
            addChild(p);
            p.loadImage(url);
            p.addEventListener(FocusEvent.FOCUS_IN, focusInHandler);
        }

        private function focusInHandler(e:FocusEvent):void {
            setChildIndex(e.currentTarget as DisplayObject, numChildren - 1);
        }

        private var focusIndex:uint = 0;
        private function keyDownHandler(e:KeyboardEvent):void {
            if (e.keyCode == Keyboard.TAB) {
                stage.focus = getChildAt(focusIndex) as Sprite;
                if (++focusIndex >= numChildren-1) focusIndex = 0;
            }
        }

    }
}
