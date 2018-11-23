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

def cwd():
    return os.getcwd()


def grabKey():
    config.read(currentPath() + '/settings.txt')
    key = config.get('GRANT_CONF', 'key')
    return key

def devKey():
    config.read(currentPath() + '/settings.txt')
    devkey = config.get('GRANT_CONF', 'devkey')
    print("WARNING: RUNNING WITH DEV KEY")
    return devkey

def authorizedRoles():
    currentRoles = grabAuthroles()


def grabAuthroles():
    config.read(currentPath() + '/settings.txt')
    role1 = config.get('Authorized_Roles', 'role1').lower()
    role2 = config.get('Authorized_Roles', 'role2').lower()
    role3 = config.get('Authorized_Roles', 'role3').lower()
    role4 = config.get('Authorized_Roles', 'role4').lower()
    currentRoles = 'Role1: ' + role1 + '\r\nRole2: ' + role2 + '\r\nRole3 ' + role3 + '\r\nRole4 ' + role4
    return currentRoles

def updateAuthroles(role1 = None, role2 = None, role3 = None, role4 = None):
    config.read(currentPath() + '/settings.txt')
    config.set('Authorized_Roles', 'role1', str(role1))
    config.set('Authorized_Roles', 'role2', str(role2))
    config.set('Authorized_Roles', 'role3', str(role3))
    config.set('Authorized_Roles', 'role4', str(role4))
    with open('Plugins/settings.txt', 'w') as configfile:
        config.write(configfile)

#updateAuthroles('droogs', 'admins')
#print(grabAuthroles())



# parse existing file
#config.read('settings.txt')

# read values from a section
#key = config.get('Grant', 'key')
#role1 = config.get('Authorized_Roles', 'role1')
#bool_val = config.getboolean('section_a', 'bool_val')
#int_val = config.getint('section_a', 'int_val')
#float_val = config.getfloat('section_a', 'pi_val')

#print(key)
#print(role1)

# update existing value
#config.set('section_a', 'string_val', 'world')

# add a new section and some values
#config.add_section('section_b')
#config.set('section_b', 'meal_val', 'spam')
#config.set('section_b', 'not_found_val', '404')

# save to a file
#with open('settings.txt', 'w') as configfile:
#    config.write(configfile)
