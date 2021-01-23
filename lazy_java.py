from subprocess import call
from os import path
from sys import argv

def fast_crt():
	file_name = argv[1].title()


	j1 = f"class {file_name} "

	j2 = """{

		public static void main(String[] args){



		}


	}
	"""
	java = j1 +j2

	if path.exists(f"{file_name}.java"):
		print("Файл с данным именем существует")

	else:

		with open(f"{file_name}.java","w") as f:
			print(java,file=f)

		call(f"gedit {file_name}.java &",shell=True)

fast_crt()
