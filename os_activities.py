import os
import static


user = os.getlogin()
path = 'C:/Users/{0}/Documents/{1}'.format(user, static.FOLDER)
os.makedirs(path)