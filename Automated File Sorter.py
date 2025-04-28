import os
import shutil
path = r"C:/Users/user/Documents/"
list_dir = os.listdir(path)
folder_names = ["Csv Files","Xlsx Files","Text Files","Rstudio Files","Pdf Files","R Files","Xlsm Files"]
for loop in range(0,7):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs(path + folder_names[loop])
for file in list_dir:
    if ".csv" in file and not os.path.exists(path + "Csv Files/" + file):
        shutil.move(path + file,path + "Csv files/" + file)
    if ".xlsx" in file and not os.path.exists(path + "Xlsx Files/" + file):
        shutil.move(path + file , path + "Xlsx Files/" + file)
    if ".txt" in file and not os.path.exists(path + "Text Files/" + file):
        shutil.move(path + file , path + "Text Files/" + file)
    if ".Rdata" in file and not os.path.exists(path + "Rstudio Files/" + file):
        shutil.move(path + file , path + "Rstudio Files/" + file)
    if ".pdf" in file and not os.path.exists(path + "Pdf Files/" + file):
        shutil.move(path + file , path + "Pdf Files/" + file)
    if ".xlsm" in file and not os.path.exists(path + "Xlsm Files/" + file):
        shutil.move(path + file , path + "Xlsm Files/" + file)
    if ".R" in file and not os.path.exists(path + "R Files/" + file):
        shutil.move(path + file , path + "R Files/" + file)