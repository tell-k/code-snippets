package 
{
    import flash.display.Sprite;
    import flash.events.Event;
    import org.libspark.eseclock.Eseclock;
    import com.github.tell_k.naviqlock.Naviqlock;

    /**
     * ...
     * @author yossy:beinteractive
     */
    public class Main extends Sprite 
    {
        public function Main():void 
        {
            if (stage) init();

            else addEventListener(Event.ADDED_TO_STAGE, init);
        }

        private function init(e:Event = null):void 
        {
            removeEventListener(Event.ADDED_TO_STAGE, init);
            // entry point

            var clock:Naviqlock = new Naviqlock();
            addChild(clock);

            clock.w = 800;
            clock.h = 600;
            clock.description = "NAVIQLOCK";
        }
    }
}
