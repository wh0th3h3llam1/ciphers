/*
* Case Sensitive Caesar Cipher Using Java
* Author : wh0am1
* GitHub : https://github.com/wh0th3h3llam1
*/

/* Case Sensitive Caesar Cipher */


import java.lang.*;
import java.util.Scanner;
import java.io.*;


class CaesarCipher
{
	public static void main(String[] args) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int ch;
		String Lin = "Linux";
		String Win = "Windows 10";
		while(true)
		{
			if(System.getProperty("os.name").equals(Lin))
			{
				System.out.print("\033[H\033[2J");
			}
			if(System.getProperty("os.name").equals(Win))
			{
				new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
			}
			System.out.flush();
			System.out.println("\t\t\t\t\tCasear Cipher");
			System.out.println();
			System.out.println("\t1. Encrypt A String");
			System.out.println("\t2. Decrypt A String");
			System.out.println("\t0. Exit");
			System.out.println();
			System.out.print("\tEnter Your Choice : ");

			ch = sc.nextInt();

			switch(ch)
			{
				case 1 :
					Encrypt en = new Encrypt();
					try
					{
						en.getData();
					}catch(Exception e){}
					String enc = en.getEncryptedString();
					System.out.println("\n\tEncrypted String : " + enc);
					System.out.println();
					break;
				case 2 :
					Decrypt de = new Decrypt();
					try
					{
						de.getData();
					}catch(Exception e){}
					String dec = de.getDecryptedString();
					System.out.println("\n\tDecrypted String : " + dec);
					System.out.println();
					break;
				case 0 :
					System.exit(0);
				default :
					System.out.println("\n\tInvalid Choice.....Please Try Again");
					System.out.println();
					break;
			}
			System.in.read();
		}
	}
}


class Encrypt
{
	String str="";
	int shift=0;

	void getData() throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("\n\tEnter A String : ");
		str = br.readLine();
		System.out.print("\tEnter Shift Value : ");
		shift = Integer.parseInt(br.readLine());
	}

	String getEncryptedString()
	{
		String s = "";
		for(int i = 0; i < str.length(); i++)
		{
			char c = 'a';

			// Character is Between A-Z
			if((str.charAt(i)) >= 65 && (str.charAt(i)) <= 90)
			{
				if(((str.charAt(i)) + shift) > 90)
				{
					c = (char)(((str.charAt(i)) + shift - 65) % 26 + 65);
				}
				else
				{
					c = (char)((str.charAt(i)) + shift);
				}
			}

			// Character is Between a-z
			else if((str.charAt(i)) >= 97 && (str.charAt(i)) <= 122)
			{
				if(((str.charAt(i)) + shift) > 122)
				{
					c = (char)(((str.charAt(i)) + shift - 97) % 26 + 97);
				}
				else
				{
					c = (char)((str.charAt(i)) + shift);
				}
			}

			// Character is Between 0-9
			else if((str.charAt(i)) >= 48 && (str.charAt(i)) <= 57)
			{
				if(((str.charAt(i)) + shift) > 57)
				{
					c = (char)(((str.charAt(i)) + shift - 48) % 10 + 48);
				}
				else
				{
					c = (char)((str.charAt(i)) + shift);
				}
			}

			// Character is a Space ' '
			else if(str.charAt(i) == 32)
			{
				c = (char)(str.charAt(i));
			}

			// Character is a special character
			else
			{
				c = (char)(str.charAt(i));
			}
			String ci = Character.toString(c);
			s += ci;
		}
		return s;
	}
}

class Decrypt
{
	String str="";
	int shift=0;

	void getData() throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.print("\n\tEnter A String : ");
		str = br.readLine();
		System.out.print("\tEnter Shift Value : ");
		shift = Integer.parseInt(br.readLine());
	}

	String getDecryptedString()
	{
		String s = "";
		for(int i = 0; i < str.length(); i++)
		{
			char c = 'a';

			// Character is Between A-Z
			if((str.charAt(i)) >= 65 && (str.charAt(i)) <= 90)
			{
				if(((str.charAt(i)) - shift) < 65)
				{
					c = (char)(((str.charAt(i)) - shift - 65 + 26) % 26 + 65);
				}
				else
				{
					c = (char)((str.charAt(i)) - shift);
				}
			}

			// Character is Between a-z
			else if((str.charAt(i)) >= 97 && (str.charAt(i)) <= 122)
			{
				if(((str.charAt(i)) - shift) < 97)
				{
					c = (char)(((str.charAt(i)) - shift - 97 + 26) % 26 + 97);
				}
				else
				{
					c = (char)((str.charAt(i)) - shift);
				}
			}

			// Character is Between 0-9
			else if((str.charAt(i)) >= 48 && (str.charAt(i)) <= 57)
			{
				if(((str.charAt(i)) - shift) < 48)
				{
					c = (char)(((str.charAt(i)) - shift - 48 + 10) % 10 + 48);
				}
				else
				{
					c = (char)((str.charAt(i)) - shift);
				}
			}

			// Character is a Space ' '
			else if(str.charAt(i) == 32)
			{
				c = (char)(str.charAt(i));
			}

			// Character is a special character
			else
			{
				c = (char)(str.charAt(i));
			}
			String ci = Character.toString(c);
			s += ci;
		}
		return s;
	}
}

/* wh0am1 */
