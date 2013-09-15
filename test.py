#-------------------------------
#!/usr/bin/python
#-----------------------FlagCreator-------------------------------
#Flagcreator by Matthew Grant
#flagcreator was used to create the flags/switches in this program
#Free to use as you wish
#Proud member of the Zeigst-Movement
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

