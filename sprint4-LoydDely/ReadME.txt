Login to Bookstack
Email - admin@admin.com
Password - password



Attempted to use bind mounts however GitHub would not take the matomo bind mounts due to exceeding size limits

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
Website URL - https://localhost:8000
Timezone - Newyork
Hit Next

Copy the Script

Go to Bookstack settings
Go to Customization
Insert copied script into Custom HTML Head Content spot
Save Settings

Go back to Matomo
Hit Next

Hit continue to Matomo

Copy this Script

<!-- Matomo -->
<script>
  var _paq = window._paq = window._paq || [];
  /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//matomo:80/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
<!-- End Matomo Code -->


Go back to Bookstack settings
Go to Customization
Insert copied script into Custom HTML Head Content spot
Save Settings

Go back to Matomo




