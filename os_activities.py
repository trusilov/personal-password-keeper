import os

import static

user = os.getlogin()
folder_path = 'C:/Users/{0}/Documents/{1}'.format(user, static.FOLDER)
file_path = '{0}/Keeper.json'.format(folder_path)


def CreateFile(file):
    f = open(file, "w+")
    f.close()


def CreateFolder(folder):
    try:
        os.makedirs(folder)
    except FileExistsError:
        print("This folder already exists")




CreateFolder(folder_path)
CreateFile(file_path)
