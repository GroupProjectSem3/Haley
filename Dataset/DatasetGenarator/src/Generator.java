import java.io.*;

import au.com.bytecode.opencsv.CSVWriter;
public class Generator
{
		public static String ds[][] = new String[5001][101];
	public void gen()
	{
		int i;
		String s[] = {"Sneezing", 
								"Stuffy Nose", 
								"Sore Throat", 
								"Cough", 
								"Phlegm",	
								"Body Pain", 
								"Fatigue",
								"Headache",
								"Chills",
								"Fever",
								"Sweating",
								"Nosebleed",
								"Confusion",
								"Mucus",
								"Loss of Appetite",
								"Loss of Smell",
								"Loss of Taste",
								"Irregular Periods",
								"Excessive hair growth",
								"Chest Pain",
								"Weight Gain",
								"Chest Discomfort",
								"Shortness of Breath",
								"Hoarseness",
								"Puffy Face",
								"Constipation",
								"Muscle Weakness",
								"Increase sensitivity to cold",
								"Nausea",
								"Vomiting",
								"Diarrhea",
								"Low Body Temperature",
								"Wheezing",
								"Cold",
								"Trouble sleeping",
								"Allergy",
								"Swelling",
								"Muscle Ache",	
								"Rash",
								"Rashes",
								"Red Spots",
								"Itchy",
								"Eye pain",
								"Fluid accumulation",
								"Vision problems",
								"Weakness",
								"Unexplained Bleeding",
								"Unexplained Bruising",
								"Increase of sweating",
								"Itchy Eyes",
								"Itchy nose",
								"Itchy mouth",
								"itchy throat",
								"Running nose",
								"Unresponsiveness",
								"Unfocused",
								"Irritable",
								"Dandruff",
								"Night Sweats",
								"Mouth Ulcers",
								"Impulsiveness",
								"Fidgeting",
								"Easily Distracted",
								"Interrupting",
								"Avoiding activities",
								"Skin discoloration",
								"High blood pressure",
								"Oily Skin",
								"Muscle Pain",
								"Obesity",
								"Decrease range of Motion",
								"Short tempered",
								"Indigestion",
								"Abdominal pain",	
								"Dizziness",
								"Whiteheads",
								"Pain during urination",
								"Frequent Urination",
								"Blood in urin",
								"Difficulty Urinating",
								"Blackheads",
								"Cystic lesions",
								"Pimples",
								"Redness",
								"Infection",
								"Tiredness",
								"Sleeplessness",
								"Daytime sleepiness",
								"Irritable",
								"Depression",
								"Anxiety",
								"Forgetfulness",
								"Pain",
								"Low Blodd pressure",
								"Dry mouth",
								"Dry Skin",
								"Muscle Cramps",
								"Missed menstrual cycle",	
								"Dehydration",
								"Stiffness", 
								"Disease"};
		// des array
		String d[] = {"COMMON COLD",
				"VIRAL FEVER",
				"PNEUMONIA",
				"ASTHMA",
				"INFECTION",
				"DIABTIES",
				"GASTRITIS",
				"ACNE",
				"INSOMNIA",
				"PREGNANCY",
				"ARTHRITIS",
				"BACK PAIN",
				"BRONCHITIS",
				"POLYCYSTIC OVARY SYNDROME",
				"HIV/AIDS",
				"ADHD",
				"BLADDER STONES",
				"CHOLERA",
				"COVID-19",
				"DENGUE FEVER",
				"EBOLA",
				"HAY FEVER",
				"HYPERTENSION",
				"HYPOTHYROIDISM",
				"MEASLES"};
		
		//for 0th row containing the labels
		for(i=0;i<101;i++)
		{
			ds[0][i]= s[i];
		}
		//for 101th column containing the des name
			for(int j=1;j<201;j++)
			{
				
				ds[j][100] = d[0];
				ds[j+200][100]= d[1];
				ds[j+400][100]= d[2];
				ds[j+600][100]= d[3];
				ds[j+800][100]= d[4];
				ds[j+1000][100]= d[5];
				ds[j+1200][100]= d[6];
				ds[j+1400][100]= d[7];
				ds[j+1600][100]= d[8];
				ds[j+1800][100]= d[9];
				ds[j+2000][100]= d[10];
				ds[j+2200][100]= d[11];
				ds[j+2400][100]= d[12];
				ds[j+2600][100]= d[13];
				ds[j+2800][100]= d[14];
				ds[j+3000][100]= d[15];
				ds[j+3200][100]= d[16];
				ds[j+3400][100]= d[17];
				ds[j+3600][100]= d[18];
				ds[j+3800][100]= d[19];
				ds[j+4000][100]= d[20];
				ds[j+4200][100]= d[21];
				ds[j+4400][100]= d[22];
				ds[j+4600][100]= d[23];
				ds[j+4800][100]= d[24];
			}
			//to syntasize data set
		
		for(i=1;i<5001;i++)
		{
			
				if(ds[i][100]=="COMMON COLD")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Sneezing")
							||ds[0][j].equalsIgnoreCase("Stuffy Nose")
							||ds[0][j].equalsIgnoreCase("Sore Throat")
							||ds[0][j].equalsIgnoreCase("Cough")
							||ds[0][j].equalsIgnoreCase("Phlegm"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Body Pain")
								||ds[0][j].equalsIgnoreCase("Fatigue")
								||ds[0][j].equalsIgnoreCase("Headache")
								||ds[0][j].equalsIgnoreCase("Chills")
								||ds[0][j].equalsIgnoreCase("Fever"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}
				else if(ds[i][100]=="VIRAL FEVER")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Chills")
							||ds[0][j].equalsIgnoreCase("Body Pain")
							||ds[0][j].equalsIgnoreCase("Fatigue")
							||ds[0][j].equalsIgnoreCase("Headache"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Sneezing")
								||ds[0][j].equalsIgnoreCase("Sore Throat")
								||ds[0][j].equalsIgnoreCase("Cough")
								||ds[0][j].equalsIgnoreCase("Sweating")
								||ds[0][j].equalsIgnoreCase("Loss of Appetite"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}
				else if(ds[i][100]=="PNEUMONIA")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Chest Pain")
							||ds[0][j].equalsIgnoreCase("Cough")
							||ds[0][j].equalsIgnoreCase("Shortness of Breath")
							||ds[0][j].equalsIgnoreCase("Phlegm")
							||ds[0][j].equalsIgnoreCase("Nausea"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("chills")
								||ds[0][j].equalsIgnoreCase("Vomiting")
								||ds[0][j].equalsIgnoreCase("Diarrhea")
								||ds[0][j].equalsIgnoreCase("Low body temperature")
								||ds[0][j].equalsIgnoreCase("Fatigue"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}	
				else if(ds[i][100]=="ASTHMA")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Chest Pain")
							||ds[0][j].equalsIgnoreCase("Shortness of Breath")
							||ds[0][j].equalsIgnoreCase("Wheezing"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Cold")
								||ds[0][j].equalsIgnoreCase("Trouble sleeping")
								||ds[0][j].equalsIgnoreCase("Allergy"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}	
				else if(ds[i][100]=="INFECTION")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Fatigue")
							||ds[0][j].equalsIgnoreCase("Diarrhea")
							||ds[0][j].equalsIgnoreCase("Swelling")
							||ds[0][j].equalsIgnoreCase("Muscle ache"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Chill")
								||ds[0][j].equalsIgnoreCase("Cough")
								||ds[0][j].equalsIgnoreCase("Rash")
								||ds[0][j].equalsIgnoreCase("Shortness of breath")
								||ds[0][j].equalsIgnoreCase("Vision problems"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}		
				else if(ds[i][100]=="DIABTIES")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Shortness of breath")
							||ds[0][j].equalsIgnoreCase("Nausea")
							||ds[0][j].equalsIgnoreCase("Increase of sweating")
							||ds[0][j].equalsIgnoreCase("Unresponsiveness")
							||ds[0][j].equalsIgnoreCase("Fatigue"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Chest pain")
								||ds[0][j].equalsIgnoreCase("Vomiting")
								||ds[0][j].equalsIgnoreCase("Unfocused")
								||ds[0][j].equalsIgnoreCase("Irritable")
								||ds[0][j].equalsIgnoreCase("Short tempered"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}		
				else if(ds[i][100]=="GASTRITIS")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Indigestion")
							||ds[0][j].equalsIgnoreCase("Nausea")
							||ds[0][j].equalsIgnoreCase("Vomiting")
							||ds[0][j].equalsIgnoreCase("Abdominal pain"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Dizziness")
								||ds[0][j].equalsIgnoreCase("Loss of appetite"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}		
				else if(ds[i][100]=="ACNE")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Whiteheads")
							||ds[0][j].equalsIgnoreCase("Blackheads")
							||ds[0][j].equalsIgnoreCase("Cystic lesions")
							||ds[0][j].equalsIgnoreCase("Pimples"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Swelling"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}			
				else if(ds[i][100]=="INSOMNIA")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Tiredness")
							||ds[0][j].equalsIgnoreCase("Sleeplessness")
							||ds[0][j].equalsIgnoreCase("Daytime sleepiness")
							||ds[0][j].equalsIgnoreCase("Irritated")
							||ds[0][j].equalsIgnoreCase("unfocused"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Depression")
								||ds[0][j].equalsIgnoreCase("Anxiety")
								||ds[0][j].equalsIgnoreCase("Forgetfulness"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
				}
			}
				else if(ds[i][100]=="PREGNANCY")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Tiredness")
							||ds[0][j].equalsIgnoreCase("Pain")
							||ds[0][j].equalsIgnoreCase("Missed menstrual cycle")
							||ds[0][j].equalsIgnoreCase("Nausea")
							||ds[0][j].equalsIgnoreCase("Vomiting"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Dehydration")
								||ds[0][j].equalsIgnoreCase("Loss of appetite")
								||ds[0][j].equalsIgnoreCase("Chills"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}		
				else if(ds[i][100]=="ARTHRITIS")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Stiffness")
							||ds[0][j].equalsIgnoreCase("Pain")
							||ds[0][j].equalsIgnoreCase("Swelling")
							||ds[0][j].equalsIgnoreCase("Redness")
							||ds[0][j].equalsIgnoreCase("Decrease range of motion"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Obesity"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				
				else if(ds[i][100]=="BACK PAIN")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Muscle ache"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="BRONCHITIS")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("FEVER")
							||ds[0][j].equalsIgnoreCase("Chills")
							||ds[0][j].equalsIgnoreCase("Cough")
							||ds[0][j].equalsIgnoreCase("Chest Discomfort"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Mucus")
								||ds[0][j].equalsIgnoreCase("Fatigue")
								||ds[0][j].equalsIgnoreCase("Shortness of breath"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				
				else if(ds[i][100]=="POLYCYSTIC OVARY SYNDROME")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Irregular Periods")
							||ds[0][j].equalsIgnoreCase("Acne")
							||ds[0][j].equalsIgnoreCase("Excessive hair growth")
							||ds[0][j].equalsIgnoreCase("Missed menstrual cycle")
							||ds[0][j].equalsIgnoreCase("Weight gain"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Dandruff")
								||ds[0][j].equalsIgnoreCase("Skin discoloration")
								||ds[0][j].equalsIgnoreCase("Oily Skin"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="HIV/AIDS")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Joint pain")
							||ds[0][j].equalsIgnoreCase("Muscle pain")
							||ds[0][j].equalsIgnoreCase("Sore Throat"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Night Sweats")
								||ds[0][j].equalsIgnoreCase("Mouth ulcers")
								||ds[0][j].equalsIgnoreCase("Chills")
								||ds[0][j].equalsIgnoreCase("Fatigue"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="ADHD")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Impulsiveness")
							||ds[0][j].equalsIgnoreCase("Fidgeting")
							||ds[0][j].equalsIgnoreCase("Easily Distracted")
							||ds[0][j].equalsIgnoreCase("Intrupting"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Avoiding activities"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="BLADDER STONES")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Abdominal pain")
							||ds[0][j].equalsIgnoreCase("Pain during urination")
							||ds[0][j].equalsIgnoreCase("Frequent urination")
							||ds[0][j].equalsIgnoreCase("Blood in urine")
							||ds[0][j].equalsIgnoreCase("Difficulty urinating"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Infection"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="CHOLERA")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Diarrhea")
							||ds[0][j].equalsIgnoreCase("Dehydartion")
							||ds[0][j].equalsIgnoreCase("Nausea")
							||ds[0][j].equalsIgnoreCase("Vomiting"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Low blood pressure")
								||ds[0][j].equalsIgnoreCase("Dry mouth")
								||ds[0][j].equalsIgnoreCase("Muscle cramps")
								||ds[0][j].equalsIgnoreCase("Dry Skin"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="COVID-19")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Cough")
							||ds[0][j].equalsIgnoreCase("Shortness of breath"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Loss of smell")
								||ds[0][j].equalsIgnoreCase("Loss of taste")
								||ds[0][j].equalsIgnoreCase("Fatigue"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="DENGUE FEVER")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Rash")
							||ds[0][j].equalsIgnoreCase("Eye Pain")
							||ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Nausea")
							||ds[0][j].equalsIgnoreCase("Vomiting"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Abdominal Pain")
								||ds[0][j].equalsIgnoreCase("Fluid accumulation"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="EBOLA")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Fever")
							||ds[0][j].equalsIgnoreCase("Headache")
							||ds[0][j].equalsIgnoreCase("Fatigue")
							||ds[0][j].equalsIgnoreCase("Muscle pain")
							||ds[0][j].equalsIgnoreCase("Abdominal pain"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Weakness")
								||ds[0][j].equalsIgnoreCase("Unexpected Bleeding")
								||ds[0][j].equalsIgnoreCase("Unexpected bruising"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="HAY FEVER")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Itchy eyes")
							||ds[0][j].equalsIgnoreCase("Running nose")
							||ds[0][j].equalsIgnoreCase("Sneezing")
							||ds[0][j].equalsIgnoreCase("Coughing")
							||ds[0][j].equalsIgnoreCase("Watery eyes"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Loss of smell")
								||ds[0][j].equalsIgnoreCase("itchy nose")
								||ds[0][j].equalsIgnoreCase("itchy throat")
								||ds[0][j].equalsIgnoreCase("itchy mouth"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="HYPERTENSION")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("High blood pressure")
							||ds[0][j].equalsIgnoreCase("Headache")
							||ds[0][j].equalsIgnoreCase("Nose bleed")
							||ds[0][j].equalsIgnoreCase("Fatigue"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Dizziness")
								||ds[0][j].equalsIgnoreCase("Confusion"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				
				else if(ds[i][100]=="HYPOTHYROIDISM")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Weight gain")
							||ds[0][j].equalsIgnoreCase("Puffy Face")
							||ds[0][j].equalsIgnoreCase("Constipation")
							||ds[0][j].equalsIgnoreCase("Fatigue")
							||ds[0][j].equalsIgnoreCase("Dry skin"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else if(ds[0][j].equalsIgnoreCase("Hoarseness")
								||ds[0][j].equalsIgnoreCase("Muscle weakness")
								||ds[0][j].equalsIgnoreCase("Increase sensitivity to cold"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				else if(ds[i][100]=="MEASLES")
				{
					for(int j=0;j<100;j++)
					{
						if(ds[0][j].equalsIgnoreCase("Red Spots")
							||ds[0][j].equalsIgnoreCase("Itchy")
							||ds[0][j].equalsIgnoreCase("Rashes"))
						{
							double in = Math.random();
							int f =0;
							if(in>=0.5)
							{	
							 f = (int) Math.ceil(in);
							}
							else
							{
							 f = (int) Math.floor(in);
							}
							ds[i][j] = Integer.toString(f);
						//int f = (int) Math.floor((Math.random()*6));
						//ds[i][j] = Integer.toString(f);
						}
						else
						{
							ds[i][j] = Integer.toString(0);
						}
						
				}
			}	
				
				
		}
		
		System.out.println(ds[2005][20]);
	}
	
	

	public static void exportDataToExcel(String fileName, String[][] data) throws FileNotFoundException, IOException
    {
        File file = new File(fileName);
        if (!file.isFile())
            file.createNewFile();

        CSVWriter csvWriter = new CSVWriter(new FileWriter(file));

        int rowCount = data.length;

        for (int i = 0; i < rowCount; i++)
        {
            int columnCount = data[i].length;
            String[] values = new String[columnCount];
            for (int j = 0; j < columnCount; j++)
            {
                values[j] = data[i][j] + "";
            }
            csvWriter.writeNext(values);
        }

        csvWriter.flush();
        csvWriter.close();
    }

	public static void main (String args[])throws IOException
	{
		Generator g = new Generator();
				g.gen();
				exportDataToExcel("F:/Binary-200row.csv", ds);
	}
}
