
object HelloWorld {
    def main( arg:Array[String] ):Unit = {
        val now = new java.util.Date 
        println( "Hello,world! %s" format now ) 
    }
}
