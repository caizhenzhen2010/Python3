package greet

object hello_worksheet {;import org.scalaide.worksheet.runtime.library.WorksheetSupport._; def main(args: Array[String])=$execute{;$skip(83); 
  println("Welcome to the Scala worksheet");$skip(10); 
  val x=1;System.out.println("""x  : Int = """ + $show(x ));$skip(29); 
  def increse( x:  Int)= x+1;System.out.println("""increse: (x: Int)Int""");$skip(14); val res$0 = 
  increse (x);System.out.println("""res0: Int = """ + $show(res$0))}
}
