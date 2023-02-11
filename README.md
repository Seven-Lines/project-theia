# Theia [0.6.0] 

Personal viewBOOSTing software. As opposed to throwing cheap, obviously fake views at youtube, Theia will manage a large number of hyper-realistic bot accounts.

The challenge when view botting on YouTube is that - considering the relatively large amount of money they give to creators - YouYube has gotten very good at tracking bots. They check your IP, your browser session behavior, and I've heard even the keyboard and mouse the system is using. The cost and computing power to circumvent these measures is fucking grandious. Therefore, Theia compromises in two areas while still delivering artificial success on Youtube: (1) Instead of view *botting* it instead view *boosts* and (2) utilizes bots on other websites.

---
###### BOTS
Bots are just a collection of names, usernames, passwords, IP addresses, etc. stored in string format that are used when workers execute behavior. Like so: ``"john doe;jdoe000;A1B2C3D4;john_doe001@protonmail.com;0.0.0.0"``. To be stored inside of ``./data/bots.json``. 
| 'Name' | 'Username' | 'Password' | 'Email' | 'VPN' | 
| --- | --- | --- | --- | --- | 
| Formated "first last", created from a wordlist of 1000+ first and last names. | Can be created using a random noun OR a combination of the first and last name. See ``./util/password_generation`` or ``./util/username_generation``. | A collection of 8 random characters or numbers. Subject to change, but should theoretically work fine. | The email address used to create/manage the bot. Handled on [ProtonMail](https://proton.me/mail). | This is the VPN connection associated with the account. Designed such that YT doesn't instantly flag the fucking thing for connecting to a bunch of random connections. |

*\*All of this is subject to change depending on what YouTube/TikTok flag.*
