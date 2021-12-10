# Reboot Your DigitalOcean Droplet from Discord
You can use this bot to reboot your DigitalOcean droplet from Discord and text someone in an emergency (like PagerDuty). 

My gaming community's server is hosted on DigitalOcean and we have less technically inclined team members who want to be able to assist with server resets when needed. This lets them reboot the droplet with `^reboot` and also lets them ping me in an emergency with `^ping`.

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Finvictus2010%2Frebootbot%2Ftree%2Fmain&envs=digitalocean_token%2Cdiscord_token%2Cdiscord_allowed_role_id%2Cdigitalocean_droplet_id%2Ctwilio_token%2Ctwilio_account%2Ctwilio_phone_number%2Cuser_phone_number&digitalocean_tokenDesc=Find+this+in+your+DigitalOcean+account.+Click+APIs+and+generate+an+API+key.&discord_tokenDesc=This+is+the+bot%27s+discord+token.+Find+it+in+your+discord+account.&discord_allowed_role_idDesc=This+is+the+role+of+Discord+users+who+can+command+the+bot.+Find+it+in+Discord+Server+Settings+-%3E+Roles.+Copy+the+role+id.&digitalocean_droplet_idDesc=The+droplet+ID+of+the+droplet+you+want+to+reset.&twilio_tokenDesc=The+auth+token+associated+with+your+Twilio+account.&twilio_accountDesc=The+account+SID+associated+with+your+Twilio+account.&twilio_phone_numberDesc=The+phone+number+associated+with+your+Twilio+account.+This+number+will+send+the+text+message.&user_phone_numberDesc=The+phone+number+you+want+to+be+able+to+text%2Fping.+This+number+will+receive+the+text+message.&referralCode=jwithing)


## Environmental Variables You Need to Setup

1. `digitalocean_token`: Find this in your DigitalOcean account. Click APIs and generate an API key.
2. `discord_token`: This is the bot's discord token. Find it in your discord account.
3. `discord_allowed_role_id`: This is the role of Discord users who can command the bot. Find it in Discord Server Settings -> Roles. Copy the role id.
4. `digitalocean_droplet_id`: The droplet ID of the droplet you want to reset.
5. `twilio_token`: The auth token associated with your Twilio account.
6. `twilio_account`: The account SID associated with your Twilio account.
7. `twilio_phone_number`: The phone number associated with your Twilio account. This number will send the text message.
8. `user_phone_number`: The phone number you want to be able to text/ping. This number will receive the text message.

## Customizations
Customize the message in the `text_message` function and user name within the `on_message` event.