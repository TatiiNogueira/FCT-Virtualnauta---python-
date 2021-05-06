#Link Copie File -> https://www.youtube.com/watch?v=hSTw7CAWRpo
#Link Copie Folder -> https://www.youtube.com/watch?v=aQpHzBkaU3o

#Módulos
import os, shutil

#Pasta do projeto
os.chdir('C:\\Users\\nogue\\Desktop\\Work\\k\\Flask_Contas')

#Passar uma pasta 
shutil.copytree('C:\\Users\\nogue\\Desktop\\Work\\k\\mypkg\\mypkg','mypkg')
shutil.copytree('C:\\Users\\nogue\\Desktop\\Work\\k\\mypkg\\tests','tests')
#Passar um ficheiro
shutil.copyfile('C:\\Users\\nogue\\Desktop\\Work\\k\\mypkg\\pyproject.toml','pyproject.toml')