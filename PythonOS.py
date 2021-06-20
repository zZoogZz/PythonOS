import getpass
import time
import random
import sys
import signal

######################ACCOUNTS: ######################
#EXAMPLEUSER
EXUSERuser = 'Username' #User's Username
EXUSERpwrd = 'Password' #User's Password
EXUSERenabled = 'TRUE' #Is User Enabled, can be TRUE or FALSE #FALSE BY DEFAULT!
#USER1
USER1user = 'Admin'
USER1pwrd = 'Password'
USER1enabled = 'TRUE'
#USER2
USER2user = ''
USER2pwrd = ''
USER2enabled = 'FALSE'
#USER3
USER3user = ''
USER3pwrd = ''
USER3enabled = 'FALSE'
#USER4
USER4user = ''
USER4pwrd = ''
USER4enabled = 'FALSE'
#USER5
USER5user = ''
USER5pwrd = ''
USER5enabled = 'FALSE'
#USER6
USER6user = ''
USER6pwrd = ''
USER6enabled = 'FALSE'
#USER7
USER7user = ''
USER7pwrd = ''
USER7enabled = 'FALSE'
#USER8
USER8user = ''
USER8pwrd = ''
USER8enabled = 'FALSE'
#USER9
USER9user = ''
USER9pwrd = ''
USER9enabled = 'FALSE'
##################GUI DEFAULTS##################
widsize = 70 #WIDTH OF WINDOW SIZE NOTE:DO NOT USE HIGH VALUES
height = 50 #HEIGHT OF WINDOW SIZE NOTE:DO NOT USE HIGH VALUES
#END OF CONFIG!

#########################CODE#########################
###########DO NOT CHANGE UNLESS GOOD AT CODE##########
print("Loading Libraries, Please Wait!", end="\r")
time.sleep(3)
print("                                       ", end="\r")
time.sleep(1)
for x in range(15):
	b = "Loading: " + "▋" * x
	print(b, end="\r")
	time.sleep(random.randint(1,2))
print("Done!                           ", end="\r")
for x in range(60):
	print("")
###################DEFAULT VARIABLES##################
middlepoint = int(widsize/2)
###################DEFINED PROGRAMS###################
#TIMED INPUT:
class AlarmException(Exception):
    pass

def alarmHandler(signum, frame):
    raise AlarmException

def timedinput(prompt='', timeout=15):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = input(prompt)
        signal.alarm(0)
        return "RUNOUT"
    except AlarmException:
        print ('\n ')
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return "TIMEOUT"
#END OF TIMED INPUT

#GUI WINDOWS
##NORMAL WINDOW
def normalbox(widsize=widsize,height=height):
	print("┍"+"━"* widsize+"┑")
	for i in range(height):
		print("│"+" "*widsize+"│")
	print("└"+"━"* widsize+"┘")
##TTILED WINDOW
def titledbox(title="UNDEF TITLE CONTACTDEV",widsize=widsize,height=height,middlepoint=middlepoint):
	print("┍"+"━"* widsize+"┑")
	titlelen=len(title)
	middlepoint=middlepoint-int(titlelen/2)
	print("│"+" "*middlepoint+title+" "*middlepoint+"│")
	print("├"+"━"* widsize+"┤")
	for i in range(height):
		print("│"+" "*widsize+"│")
	print("└"+"━"* widsize+"┘")

################END OF DEFINED PROGRAMS###############

Login = "0"
while Login != "1":
	time.sleep(5)
	for x in range(60):
		print("")
	print("PythonOS")
	print("")
	print("Hello, Please Enter Your Username and Password.")
	username = input("Username: ")
	password = getpass.getpass("Password: ")
	if username == USER1user:
		if password == USER1pwrd:
			if "TRUE" == USER1enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER1user
				LoginPWRD = USER1pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER2user:
		if password == USER2pwrd:
			if "TRUE" == USER2enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER2user
				LoginPWRD = USER2pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER3user:
		if password == USER3pwrd:
			if "TRUE" == USER3enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER3user
				LoginPWRD = USER3pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER4user:
		if password == USER4pwrd:
			if "TRUE" == USER4enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER4user
				LoginPWRD = USER4pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER5user:
		if password == USER5pwrd:
			if "TRUE" == USER5enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER5user
				LoginPWRD = USER5pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER6user:
		if password == USER6pwrd:
			if "TRUE" == USER6enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER6user
				LoginPWRD = USER6pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER7user:
		if password == USER7pwrd:
			if "TRUE" == USER7enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER7user
				LoginPWRD = USER7pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER8user:
		if password == USER8pwrd:
			if "TRUE" == USER8enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER8user
				LoginPWRD = USER8pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	elif username == USER9user:
		if password == USER9pwrd:
			if "TRUE" == USER9enabled:
				print("Welcome!")
				Login = "1"
				LoginUSER = USER9user
				LoginPWRD = USER9pwrd
			else:
				print("User Disabled!")
				print("If you belive this is a fault please contact your Adminaistrator!")
		else:
			print("Username Or Password Incorrect!")
	else:
		print("Username or Password Incorrect!")

if Login == "0":
	print("FIREWALL EMERGENCY SHUTDOWN")
	print("Disconnecting!")
	print("Shutting Down!")
	sys.exit("Shut Down!")
for x in range(60):
	print("")
print("PythonOS")
print("Welcome, ",LoginUSER)
time.sleep(3)
bootup=timedinput("Press Enter To Enter Setup Mode",15)
if bootup == "BOOTUP":
	print("┍","━"* widsize,"┑")






for x in range(60):
	print("")
print("PythonOS")
input("Press Enter To Shutdown")
