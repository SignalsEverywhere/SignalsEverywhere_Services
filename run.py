import discord
import requests
import re
from Plugins import roleAuth
from Plugins import botConf
from Plugins import fccid
from Plugins import hamCall

client = discord.Client()

def serverRole(author_id, server_id):
    roles = client.get_server(server_id).get_member(author_id).roles
    return roles


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='!helpme'))


@client.event
async def on_message(message):

    if message.content.startswith('?help'):
        #await client.purge_from(message.channel, limit=1, check=message.author)
        #help_file = open("help.txt", "r")
        #help_msg = help_file.read()
        help_msg = botConf.grabHelp()
        privateMessage = await client.start_private_message(message.author)
        await client.send_message(privateMessage, help_msg)

    if message.content.startswith('?updatehelp'):
        if roleAuth.adminRole(message.author.id):
            privateMessage = await client.start_private_message(message.author)
            msg = message.content
            stripped = re.sub('\?updatehelp', '', msg)
            await client.send_typing(message.channel)
            await client.send_message(privateMessage, "Thanks, here is a preview of your help file\r\n\r\n" + stripped + '\r\n\r\n\r\n')
            await client.send_message(privateMessage, 'Type \'confirmed\' to save.')
            if await client.wait_for_message(author=message.author, content='confirmed'):
                botConf.updateHelp(stripped)
                await client.send_typing(message.channel)
                await client.send_message(privateMessage, 'updated')

    if message.content.startswith('!call'):
        if roleAuth.checkRole(serverRole(message.author.id, message.server.id)):
            await client.send_typing(message.channel)
            msg = message.content
            split = msg.split(' ')
            print(hamCall.callsign_start(split[1]))
            await client.send_message(message.channel, hamCall.callsign_start(split[1]))


    if message.content.startswith('!id'):
        if roleAuth.checkRole(serverRole(message.author.id, message.server.id)):
            await client.send_typing(message.channel)
            try:
                msg = message.content
                split = msg.split(' ')
                id = split[1].upper()
                pageRequest = requests.get("http://fccid.io/%s" % id)
                if fccid.isValid(pageRequest) == True: ##check to see if the fcc id is valid
                    url1 = ('https://fccid.io/%s\\' % id)
                    url2 = ('https://gov.fccid.io/%s\\' % id)
                    title = fccid.manu(pageRequest, id)
                    freq = fccid.freq(pageRequest)
                    photos = fccid.internal(pageRequest)
                    power = fccid.power(pageRequest)
                    diagram = fccid.diagram(pageRequest)
                    schematics = fccid.schematics(pageRequest)
                    part = fccid.part(pageRequest)
                    assembled = "```" + title + "\r\n" + freq + "\r\n" + power + "  " + part + "```" + "\r\n" + 'Details: ' + url1 + ' or ' + url2 + '\r\n' + photos + '\r\n' + diagram + '\r\n' + schematics
                    await client.send_message(message.channel, assembled)
                else:
                    await client.send_message(message.channel, "Sorry that ID does not appear to be valid")
            except:
                await client.send_message(message.channel,
                                          'Sorry, the website syntax must be weird on this one.\rTake your pick of links instead.\n\r\n' + 'FCCID: ' + url1 + '\r\n' + 'FCC.GOV: ' + url2)
                print("Debug " + assembled)
        else:
            privateMessage = await client.start_private_message(message.author)
            await client.send_message(privateMessage, 'Sorry You don\'t have the botaccess role')

    if message.content.startswith('?myid'):
        print(message.author.id)


    if message.content.startswith('?getroles'):
        if roleAuth.adminRole(message.author.id):
            privateMessage = await client.start_private_message(message.author)
            await client.send_message(privateMessage, botConf.grabAuthroles())

    if message.content.startswith('?updateroles'):
        if roleAuth.adminRole(message.author.id):
            privateMessage = await client.start_private_message(message.author)
            msg = message.content.lower()
            split = msg.split(' ', 4)
            try:
                role1 = split[1]
            except:
                role1 = 'None'
            try:
                role2 = split[2]
            except:
                role2 = 'None'
            try:
                role3 = split[3]
            except:
                role3 = 'None'
            try:
                role4 = split[4]
            except:
                role4 = 'None'
            await client.send_typing(message.channel)
            await client.send_message(privateMessage, 'Below are the new roles, to save these roles now type: confirmed')
            await client.send_message(privateMessage, 'Role1: ' + role1 + '\r\nRole2: ' + role2 + '\r\nRole3: ' + role3 + '\r\nRole4: ' + role4)
            if await client.wait_for_message(author=message.author, content='confirmed'):
                botConf.updateAuthroles(role1, role2, role3, role4)
                await client.send_message(privateMessage, 'Authorized roles have been succesfully saved.')
            else:
                await client.send_message(privateMessage, 'Authorized roles have NOT been saved.')



client.run(botConf.grabKey())
#client.run(botConf.devKey())
