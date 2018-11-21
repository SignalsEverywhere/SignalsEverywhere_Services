# SignalsEverywhere_Services
A Discord bot to provide various services to SignalsEverywhere members.

The settings file is not included in the repo to keep the key safe.
settings.txt goes in the Plugins folder and should look like this...


[FCC]<br>
key = API KEY FOR DISCORD HERE<br><br>

[Authorized_Roles]<br>
role1 = Member<br>
role2 = None<br>
role3 = None<br>
role4 = None<br><br>

[Admin_Role]<br>
adminrole = Admins



# Cron script to restart
Just point a cron job at the restart_cron.sh file ensuring that the name fields inside it match the name you've given the container in docker. This will ensure that if the bot dies for any reason it'll come back up within 1min.
