BookStack is http://localhost/
Login to Bookstack
Email - admin@admin.com
Password - password



Attempted to use bind mounts however GitHub would not take the matomo bind mounts due to exceeding size limits
Matomo is http://localhost/matomo/

Set up Instructions otherwise - 
Hit install Matomo
Hit next
Hit next on system check

Database Setup should auto fill this - 
Database server - matomo_db
Login - matomo
Password - matomopass
Database Name - matomo
Table Prefix - matomo_
Adapter - PDO/MYSQL
Database Engine - MySQL
Hit Next

Hit Next

Superuser is you login that you create but this is what I used -
Superuser Login - bookstack
Password - Admin1234
Password Repeat - Admin1234
Email - admin@admin.com
Hit Next

Website name - bookstack
Website URL - https://bookstack
Timezone - Newyork
Hit Next

Copy the Script in this file - MatomoScriptInCase.html

Got to Bookstack settings
Go to Customization
Insert copied script into Custom HTML Head Content spot
Save Settings

Go back to Matomo
Hit Next

Hit continue to Matomo