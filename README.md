Easygetopt
==========

easygetopt is a python script that generates code in python for parsing command line arguments by just answering a couple of question.

I wrote this script because I found myself copy and pasting the code for dealing with command line options using getopt from one project to another.
Thus, like any good programmer I decided to automate the process.  This is a useful script when you are beginning a need program in python.
Just run the script, answer the questions that are prompted and the program will create a new python file with the command line parsing already done for you.

Requirments:
------------
* Just need to make sure python and its standard library are installed on your computer

Usage:
------
Just download the script (flagcreator.py) and than go to the folder that has the Easygetopt.  After which type the following into the terminal window.

```
# run the script 
# -o option is the file name of the file you want to create with this script
python ./flagcreator.py -o test.py 

file = test.py
--------------flag creator -----------------
Just answer the questions and the flags will be set up for you
--------------------------------------------
What is the letter for the flag? a  
The flag is -a                      # letter that will represent the option (-a)
What is the long name for the flag -a Just leave blank if you do not want a longname all
The long name for flag -a is all    # longname of the option (--all)
Does this flag has parameter data: (y)es or(n)o y  #Does the option have data with it (-a testfile)
What is the variable name for the flag -a? files   #The data will be stored this variable (files = testfile)
The variable for flag -a is files
Do you want to add another flag: (y)es or(n)o y # Do you want to add another option
-------------------------------------
What is the letter for the flag? b
The flag is -b
What is the long name for the flag -b Just leave blank if you do not want a longname bug
The long name for flag -b is bug
Does this flag has parameter data: (y)es or(n)o n
The flag does not have any data to go with it
Do you want to add another flag: (y)es or(n)o y
-------------------------------------
What is the letter for the flag? c
The flag is -c
What is the long name for the flag -c Just leave blank if you do not want a longname cat
The long name for flag -c is cat
Does this flag has parameter data: (y)es or(n)o y
What is the variable name for the flag -c? pet
The variable for flag -c is pet
Do you want to add another flag: (y)es or(n)o n
Done adding flags....
-------------------------------------
Finished!!!

```
After answering these question, a new python file called test.py is created for you.  The output file for test.py is shown below.
```
#-------------------------------
#!/usr/bin/python
#-----------------------FlagCreator-------------------------------
#Flagcreator by Matthew Grant
#flagcreator was used to create the flags/switches in this program
#Free to use as you wish
#Proud member of the zeitgeist movement
#-----------------------------------------------------------------
import sys, getopt
#----------Global Variable List---------------
files=''
pet=''
#----------Functions---------------------------
def usage():
# This is the function that handles the help flag
		print 'FlagCreator Help'
		return

def main(argv):
		try:
			opts, args = getopt.getopt(argv, 'ha:bc:',['help=''all=','bug=','cat='])
		except getopt.GetoptError:
			print 'There was an error in the format of FileCreator option'
                        print 'Enter filecreator.py -h for help'
			sys.exit(2)
		for opt, arg in opts:
			if opt in ('-h', '--help'):
		        	usage()
			        sys.exit()
			elif opt in ('-a','--all='):
				global files
				files=arg
				# replace with a call to a function to handle this flag
			elif opt in ('-b','--bug='):
				# replace with a call to a function to handle this flag
			elif opt in ('-c','--cat='):
				global pet
				pet=arg
				# replace with a call to a function to handle this flag
			
#-------------Main Body of the Program--------
if __name__ == "__main__":
		main(sys.argv[1:])
#---------------------------------------------

```
Note: You do not have to add the -h (--help) option as it is automatically added for you.

