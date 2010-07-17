package {
    import flash.display.*;
    import flash.text.*;

    public class HelloWorld extends Sprite {

           public myXML:XML ="
            <order>
                <item id='1'>
                    <menuName>burger</menuName>
                    <price>3.95</price>
                </item>
                <item id='2'>
                    <menuName>fries</menuName>
                    <price>1.45</price>
                </item>
            </order>";

            public function HelloWorld() {
                   //テキストフィールドの生成
                   var textField:TextField=new TextField();
                   textField.text="Hello World!";
                   addChild(textField);
                  log('test');
            }
    }
}
