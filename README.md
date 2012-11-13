evemail-bridge - AppEngine-based EVEMail Forwarder
=========================================

A small bridge app that runs on AppEngine and polls for new corp/alliance EVEMails
and forwards them to a specified email address.

Usage
-----

 1. Clone the repository.
 2. Edit the app.yaml to specify your unique app ID.
 3. Upload the app.
 4. Visit the homepage of the app (admin only) to configure it.
 5. Let it run.

The polling runs every 10 minutes by default, though this can be adjusted in cron.yaml if desired.

Configuration
-------------

* API Key ID, API Key Verification Code - self explanatory. The API key needs MailMessages + MailBodies permissions.
* API Key Character - the name of the character whose mailbox should be polled.
* Recipient Organization - the name or ID of a corp/alliance to forward mail for (the character must be in that corp/alliance).
* Recipient Organization #2 - same as above; most useful for specifying an alliance if the previous was a corp or vice versa.
* Destination Email Address - where to send forwarded EVEMail.

Dependencies
------------

There are no dependencies beyond the appengine utilities which are necessary to upload the app.

The [EVELink](https://github.com/eve-val/evelink) library is bundled as part of the source code for this application.
