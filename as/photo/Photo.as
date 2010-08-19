package photo{
    import caurina.transitions.Tweener;
    import flash.display.Sprite;
    import flash.display.Loader;
    import flash.display.LoaderInfo;
    import flash.events.FocusEvent;
    import flash.events.Event;
    import flash.events.TimerEvent;
    import flash.events.MouseEvent;
    import flash.net.URLRequest;
    import flash.utils.*;
    import flash.filters.DropShadowFilter;


    public class Photo extends Sprite{
        private var vx:int=2;     //x速度
        private var vy:int=2;
        private var eobj:Event=null;
        private var drawRectClosure:Function;

        public function loadImage(url:String):void{
            var loader:Loader = new Loader();
            loader.contentLoaderInfo.addEventListener(Event.COMPLETE, loadCompleteHandler);
            loader.load(new URLRequest(url));
        }

        /*
            テスト
        */
        private function loadCompleteHandler(e:Event):void{
            addChild(e.target.loader);
            x = (stage.stageWidth - e.target.width) * Math.random();
            y = (stage.stageHeight - e.target.width) * Math.random();
            e.target.loader.x = 10;
            e.target.loader.y = 10;
            drawRectClosure = function(color:uint):void{
                graphics.beginFill(color);
                graphics.drawRect(0,0, e.target.width + 20, e.target.height + 20);
                graphics.endFill();
            }
            drawRectClosure(0xFFFFFF);
            filters=[new DropShadowFilter()];
            alpha = 0;
            rotation=Math.random() * 20 -10;
            Tweener.addTween(this,{
                transition:'Linear',
                alpha:0.8,
                delay:Math.random() * 3,
                time:1
            });
            addEventListener(MouseEvent.MOUSE_OVER, mouseOverHandler);
            addEventListener(MouseEvent.MOUSE_OUT, mouseOutHandler);
            addEventListener(MouseEvent.MOUSE_DOWN, mouseDownHandler);
            addEventListener(FocusEvent.FOCUS_IN, focusInHandler);
            addEventListener(FocusEvent.FOCUS_OUT, focusOutHandler);
        }

        private function mouseOutHandler(e:MouseEvent):void{
            drawRectClosure(0xFFFFFF);
        }

        private function mouseOverHandler(e:MouseEvent):void{
            drawRectClosure(0x0088FF);
        }

        private function mouseDownHandler(e:MouseEvent):void{
            stage.focus = this;
        }

        private function focusInHandler(e:FocusEvent):void{
            drawRectClosure(0x0088FF);
            Tweener.addTween(this,{
                transition:'Linear',
                alpha:1,
                time:1
            });
        }

        private function focusOutHandler(e:FocusEvent):void{
            drawRectClosure(0xFFFFFF);
            Tweener.addTween(this,{
                transition:'Linear',
                alpha:0.8,
                time:3
            });
        }
    }

}
