import java.io.IOException;
public class Test {
	
	// Create a static String array to test the generator method
	public static String ds[][] = new String[5001][101];
	Test()
	{
		
	}
	public static void main (String args[])throws IOException
	{	
		//Creating a dummy string array
		String S[][] = new String[2][4];
		 
		S[0][0] = "hello";
		S[0][1] = "MyName";
		S[0][2] = "is";
		S[0][3] = "Generator";
		S[1][0] = "1";
		S[1][1] = "2";
		S[1][2] = "3";
		S[1][3] = "4";
		//Creating object of generator class 
		Generator Gen = new Generator();

		//Testing the export to excel function
		Gen.exportDataToExcel("F:/Dummy.csv", S);

		//Testing the generator function
		Gen.gen();
		
		                                               
	}
}
