import java.io.IOException;
public class Test {

	public static String ds[][] = new String[5001][101];
	Test()
	{
		
	}
	public static void main (String args[])throws IOException
	{
		String S[][] = new String[2][4];
		 
		S[0][0] = "hello";
		S[0][1] = "MyName";
		S[0][2] = "is";
		S[0][3] = "Generator";
		S[1][0] = "1";
		S[1][1] = "2";
		S[1][2] = "3";
		S[1][3] = "4";
		
		Generator Gen = new Generator();
		Gen.exportDataToExcel("F:/Dummy.csv", S);
		
		Gen.gen();
		
		                                               
	}
}
