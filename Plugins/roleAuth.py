##This file contains the functions used to ensure users are authenticated by a role before they can access the bot.
from configparser import ConfigParser
import os
import re

config = ConfigParser()

def currentPath():
    cwd = os.getcwd()
    if re.findall('Plugins', cwd):
        return cwd
    else:
        path = cwd + '/Plugins'
        return path

def adminRole(author):
    config.read(currentPath() + '/settings.txt')
    user_id = config.get('Admin_ID', 'user')
    if user_id == author:
        print('Admin User Detected: ' + user_id)
        return True
    else:
        pass

def checkRole(author):
    config.read(currentPath() + '/settings.txt')
    role1 = config.get('Authorized_Roles', 'role1')
    role2 = config.get('Authorized_Roles', 'role2')
    role3 = config.get('Authorized_Roles', 'role3')
    role4 = config.get('Authorized_Roles', 'role4')
    for role in author:
        print('Debug: ' + str(role))
        if str(role).lower() == role1.lower():
            return True
        if str(role).lower() == role2.lower():
            return True
        if str(role).lower() == role3.lower():
            return True
        if str(role).lower() == role4.lower():
            return True
        else:
            pass
