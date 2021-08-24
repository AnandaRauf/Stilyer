#Stilyer 
#Setup Installer Python

nameprog = "Stilyer"
version = "1.0"
devby = "Ananda Rauf Maududi"
devdate = "25 August 2021"

print("------------------------------------------------------------------------------------------------------\n")
print(nameprog)
print(version)
print(devby)
print(devdate)
print("------------------------------------------------------------------------------------------------------\n")

class Menu():
	def menu():
		print("Menu Stilyer :")
		print
		print("1.Choose Folder")
		print("2.Choose File")
		print("3.Create Setup Installation")
class ChFd():
	def chfd(self):
		print("Please,change your folder")
		os.system("pyinstaller -D Stilyer(Setup Installer Python)")
		print("Successfull choose folder")

class ChFl():
	def chfl(self):
		print("Please,change your file")
		os.system("pyinstaller --onefile stilyer.py")
		print("Successfull choose file")
class CSIns():
	def csins(self):
		ChFd.chfd()
		ChFl.chfl()
		print("Successfull Create Setup Installation")
		print("Thank you using Stilyer ^-^")
Menu.menu()
CHFD = ChFd()
CHFL = ChFl()
CSINS = CSIns()

chm = int(input("Please choose number on menu Stilyer:"))

if chm== 1:
	CHFD.chfd()
elif chm== 2:
	CHFL.chfl()
elif chm== 3:
	CSINS.csins()
else:
	exit()



