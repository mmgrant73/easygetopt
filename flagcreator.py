#!/usr/bin/python

import sys, getopt, urllib, urllib2
#----------------FlagCreator----------------------
# FlagCreator by Matthew Grant
# This program helps a develop in Python'with
# setting up flags/switches for their program
# Just answer a couple of questions and this
# program will write the code for the flags/switches
# that you specified
# -----------------Arguments----------------------
# -h (help)
# -o ouput file created by file creator
#------------------Example ------------------------
# python flagcreator.py -o /root/home/temp/program1.py

#-----------------variables------------------------
outfile=""
flaglist=[]
longnamelist=[]
variablelist=[]
q=0

#-----------------functions-----------------------
def main(argv):  
# This function determine what flags was set                                        
    try:                                
        opts, args = getopt.getopt(argv, "ho:", ["help","output="])
    except getopt.GetoptError:          
        error1()                         
        sys.exit(2)                     
    for opt, arg in opts:                
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()                  
        elif opt in ("-o", "--output="):                
            global outfile 
	    outfile= arg  
	    print "file = "+outfile  
    if (outfile==""):
	print "[Error] There is an error in the format of filecreator."
	print "[Info] Enter in 'filecreator -h' to get help with the format"                    
        sys.exit() 

def error1():
	print "There was an error in the format of the filecreator option"
	print "Enter 'filecreator.py -h for help"
	return

def usage():
	print "---------------FileCreator-------------------"
	print "File Creator 1.0.1 by Matthew Grant"
	print "This program helps a developer by automatically writing"
	print "the code for flags/switches by just answering a couple"
	print "of questions"
	print "--------------Options-----------------------"
	print "-h, --help display help for using filecreator"
	print "-o, --output tells the program where to save the file"
	print "note: that if you use '-o display' instead of a filename"
	print "the output will go to the screen instead of being save to a file"
	print "--------------Example-----------------------"
	print "python filecreator.py -h (Displays the help file)"
	print "python filecreator.py -o /root/test.py (saves the output to a file name test.py"
	print "python filecreator.py -o display (will show the output on the screen and not to a file"
	print "---------------------------------------------"
	print 
	return

def getflag():
# This function gets the short-name for the flag and store it in flaglist[]
	flag1=0
	global flaglist
	while (flag1==0):
        	flag = raw_input("What is the letter for the flag? ")
		l=len(flag)
		if (l<>1):
			print "[Error] The letter for the flag has to be one character long"
		else:
			print "The flag is -"+flag
			flaglist.append(flag)
			flag1=1
	return flag

def getlongname(flag):
# This function gets the long-name for the flag and store it in longname[]
	flag1=0
	global longnamelist
	while (flag1==0):
        	longname=raw_input("What is the long name for the flag -"+flag+" Just leave blank if you do not want a longname ")
		l=len(longname)
		if (l<2 and longname!=""):
			print "[Error] The longname of a flag has to be more than one character"
		else:
			print "The long name for flag -"+flag+" is "+longname
			longnamelist.append(longname)			
			flag1=1
	return longname

def getvariable(flag,longname):
# This function gets the variable name that will save the data from the flags
	flag1=0
	global variablelist
	while (flag1==0):
        	variable=raw_input("What is the variable name for the flag -"+flag+"? ")
		l=len(variable)
		if (l<2):
			print "[Error] The variable of a flag has to be more than one character"
		else:
			print "The variable for flag -"+flag+" is "+variable
			variablelist.append(variable)
			flag1=1
	return 

def getrequired(flag, longname):
# This function sets whether the flag requirs data parameter
	flag1=0
	global variablelist
	while (flag1==0):
        	required=raw_input("Does this flag has parameter data: (y)es or(n)o ")
		if (required=="yes" or required=="y" or required=="YES" or required=="Yes"):
			getvariable(flag,longname)
			flag1=1
		elif (required=="no" or required=="n" or required=="NO" or required=="No"):
			print "The flag does not have any data to go with it"
			variablelist.append("")	
			flag1=1	
		else:
			print "Did not recognized the anwser to does this flag has parameter data: (y)es or (n)o"
	return 

def anotherflag():
# This function determines whether you want to add another flag
	flag1=0
	global variablelist
	while (flag1==0):
        	required=raw_input("Do you want to add another flag: (y)es or(n)o ")
		if (required=="yes" or required=="y" or required=="YES" or required=="Yes"):
			againflag=0
			flag1=1
		elif (required=="no" or required=="n" or required=="NO" or required=="No"):
			print "Done adding flags...."
			variablelist.append("")	
			againflag=1
			flag1=1	
		else:
			print "Did not recognized the input you entered: (y)es or (n)o"
	return againflag

def printoutput():
# This function prints the output file 
	global flaglist
	str1=""
	str1+= "#-------------------------------\n"
	str1+= "#!/usr/bin/python\n"
	str1+= "#-----------------------FlagCreator-------------------------------\n"
	str1+= "#Flagcreator by Matthew Grant\n"
	str1+= "#flagcreator was used to create the flags/switches in this program\n"
	str1+= "#Free to use as you wish\n"
	str1+= "#Proud member of the Zeigst-Movement\n"
	str1+= "#-----------------------------------------------------------------\n"
	str1+= "import sys, getopt\n"
	str1+= "#----------Global Variable List---------------\n"
	for var1 in variablelist:
		if (var1!=""):
			str1+= var1+"=''\n"
	str1+= "#----------Functions---------------------------\n"
	str1+= "def usage():\n"
	str1+= "# This is the function that handles the help flag\n"
	str1+= "		print 'FlagCreator Help'\n"
	str1+= "		return\n"
	str1+= "\n"
	str1+= "def main(argv):\n"                                          
    	str1+= "		try:\n"    
	flagstr=getflagstr() 
	str1+= "			"+flagstr+"\n"                           
    	str1+= "		except getopt.GetoptError:\n"         
        str1+= "			print 'There was an error in the format of FileCreator option'\n"      
	str1+= "                        print 'Enter filecreator.py -h for help'\n"                   
        str1+= "			sys.exit(2)\n"                     
	str1+= "		for opt, arg in opts:\n"               
        str1+= "			if opt in ('-h', '--help'):\n"      
	str1+= "		        	usage()\n"                     
	str1+= "			        sys.exit()\n"
	bodystr=getbodystr()
	str1+= "			"+bodystr+"\n" 
	str1+= "#-------------Main Body of the Program--------\n"               
	str1+= "if __name__ == \"__main__\":\n"
    	str1+= "		main(sys.argv[1:])\n"
	str1+= "#---------------------------------------------\n"
	global outfile
	if (outfile=="display" or outfile=="Display" or outfile=="DISPLAY"):
		print str1
	else:
		outtofile(outfile,str1)
	return str1

def getbodystr():
# This is a helper function to the printout function, it sets the flag in the program
	global flaglist
	global variablelist
	global longnamelist
	c1=0
	str1=""
	for flag1 in flaglist:
		str1+="elif opt in ('-"+flag1+"','--"+longnamelist[c1]+"='):\n"
		#print "v="+variablelist[c1]
		if (variablelist[c1]!=""):
			str1+="				global "+variablelist[c1]+"\n"
			str1+="				"+variablelist[c1]+"=arg\n"
		str1+="				# replace with a call to a function to handle this flag\n			"
		c1+=1
	return str1
	

def getflagstr():
# This is a helper function for the printout function it gets the format for the flags in the program.
	global flaglist
	global variablelist
	global longnamelist
	c1=0
	str1="h"
	str2="'help='"
	for flag1 in flaglist:
		str1+=flag1
		if variablelist[c1]!="":
			str1+=":"
		c1+=1
	#print "str="+str1
	for longname1 in longnamelist:
		str2+="'"+longname1+"=',"
	str2=str2[:-1]
	strtotal="opts, args = getopt.getopt(argv, '"+str1+"',["+str2+"])"
	return	strtotal

def outtofile(file1,str1):
	# Open a file
	try:
		fo = open(file1, "w")
		fo.write( str1+"\n");
	except IOError:
		print "I/O Error: could not create the file.  Check your path"
	else:
		# Close opend file
		fo.close()
	return

#------------------Main Body---------------------------------
if __name__ == "__main__":
        main(sys.argv[1:])
	print "--------------flag creator -----------------"
	print "Just answer the questions and the flags will be set up for you"
	print "--------------------------------------------"
	while (q==0):	
		flag=getflag()
		longname=getlongname(flag)
		getrequired(flag,longname)
		again=anotherflag()
		if (again==1):
			q=1
		print "-------------------------------------"
	printoutput()
	print "Finished!!!"
