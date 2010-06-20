package photo {
    import flash.display.Sprite;
    import flash.display.Loader;
    import flash.display.LoaderInfo;
    import flash.events.Event;
    import flash.net.URLRequest;
    import flash.filters.DropShadowFilter;
    import flash.events.MouseEvent;
    import flash.events.FocusEvent;
    import caurina.transitions.Tweener;

    public class Photo extends Sprite {
        public function loadImage(url:String):void {
            var loader:Loader = new Loader();
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, loadCompleteHandler);
            loader.load(new URLRequest(url));
        }

        private var drawRectClosure:Function;
        private function loadCompleteHandler(e:Event):void {
            addChild(e.target.loader);
            x = (stage.stageWidth - e.target.width) * Math.random();
            y = (stage.stageHeight - e.target.height) * Math.random();

            e.target.loader.x = 10;
            e.target.loader.y = 10;
            drawRectClosure = function(color:uint):void {
                graphics.beginFill(color);
                graphics.drawRect(0,0, e.target.width + 20, e.target.height + 20);
                graphics.endFill();
            }
            drawRectClosure(0xFFFFFF);
            filters = [new DropShadowFilter];

            alpha = 0;
            Tweener.addTween(this, {
                alpha: 0.8,
                delay: Math.random() * 3,
                rotation: Math.random() * 20 - 10,
                time:3
            });

            addEventListener(MouseEvent.MOUSE_OVER, mouseOverHandler);
            addEventListener(MouseEvent.MOUSE_OUT, mouseOutHandler);
            addEventListener(MouseEvent.MOUSE_DOWN, mouseDownHandler);
            addEventListener(FocusEvent.FOCUS_IN, focusInHandler);
            addEventListener(FocusEvent.FOCUS_OUT, focusOutHandler);
        }
        private function mouseOutHandler(e:MouseEvent):void {
            drawRectClosure(0xFFFFFF);
        }

        private function mouseOverHandler(e:MouseEvent):void {
            drawRectClosure(0x0088FF);
        }

        private function mouseDownHandler(e:MouseEvent):void {
            stage.focus = this;
        }

        private function focusInHandler(e:FocusEvent):void {
            Tweener.addTween(this, {
                alpha:1,
                transition: 'linear',
                time:1
            });
        }

        private function focusOutHandler(e:FocusEvent):void {
            Tweener.addTween(this, {
                alpha: 0.8,
                transition: 'linear',
                time:3
            });
        }
    }
}
