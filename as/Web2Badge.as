package {
  import flash.display.Sprite;                  
  import flash.geom.Matrix;                     
  import flash.geom.Point;                      
  import flash.filters.DropShadowFilter;        
  import flash.text.TextField;                  

  public class Web2Badge extends Sprite {       
    // インスタンス変数を宣言
    private const LINE_COLOR:uint = 0xffffff;   
    private const BODY_COLOR1:uint = 0xffff66;  
    private const BODY_COLOR2:uint = 0xffcc00;  
    private const CORNER:int = 30;              
    private const RADIUS1:Number = 26;           
    private const RADIUS2:Number = 22;           
    private const TEXT:String = "PEX";          

    // コンストラクタ
    public function Web2Badge() {
      // バッジの小さいほうの直径
      var d:Number = Math.min(RADIUS1, RADIUS2) * 2;

      // Spriteを作成
      var s:Sprite = new Sprite();
      s.graphics.lineStyle(1, LINE_COLOR);

      // グラデーションの範囲と方向をMatrixオブジェクトに格納
      // (d×dの範囲を-45°の方向に)
      var matrix:Matrix = new Matrix();
      matrix.createGradientBox(d, d, -Math.PI / 4);

      // グラデーションの情報を指定
      s.graphics.beginGradientFill(
        "linear",                    // 線状のグラデーション
        [BODY_COLOR1, BODY_COLOR2],  // 色
        [1, 1],                      // 透明度
        [0, 255],                    // 色の位置
        matrix);                     // 範囲と角度

      // 星型の描画
      var angle:Number = 2 * Math.PI / CORNER;
      var p1:Point, p2:Point;
      s.graphics.moveTo(RADIUS1, 0);
      for(var i:int = 0; i < CORNER; i++) {
        p1 = Point.polar(RADIUS2, angle * (i + 0.5));
        p2 = Point.polar(RADIUS1, angle * (i + 1));
        s.graphics.lineTo(p1.x, p1.y);
        s.graphics.lineTo(p2.x, p2.y);
      }
      s.graphics.endFill();

      // 影をつける
      s.filters = [new DropShadowFilter(4, 45, 0, 0.5)];

      // 中に表示するテキストを作成
      var size:int = d / TEXT.length;
      var text:TextField = new TextField();
      text.htmlText = '<font size="' + size + '" color="#ffffff">'
        + '<b>' + TEXT + '</font></b>';
      text.x = -text.textWidth / 2;
      text.y = -text.textHeight / 2;
      text.filters = [new DropShadowFilter(1, 45, 0, 0.8)];
      s.addChild(text);

      // (100, 100) に表示
      s.x = s.y = 100;
      addChild(s);
    }
  }
}
