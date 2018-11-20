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
    adminRole = config.get('Admin_Role', 'adminrole')
    for role in author:
        print('Admin Detected :' + str(role))
        if str(role) == adminRole:
            return True
        else:
            pass

def checkRole(author):
    config.read(currentPath() + '/settings.txt')
    role1 = config.get('Authorized_Roles', 'role1')
    role2 = config.get('Authorized_Roles', 'role2')
    role3 = config.get('Authorized_Roles', 'role3')
    role4 = config.get('Authorized_Roles', 'role4')
    adminRole = config.get('Admin_Role', 'adminrole')
    for role in author:
        print('Debug: ' + str(role))
        if str(role) == role1:
            return True
        if str(role) == role2:
            return True
        if str(role) == role3:
            return True
        if str(role) == role4:
            return True
        if str(role) == adminRole:
            return True
        else:
            pass
