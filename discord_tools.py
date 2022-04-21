import os
import time
import json 
from color import Color

install = lambda module: os.system(f"python -m pip install {module}" if os.name == "nt" else f"python3 -m pip install {module}")
try:
    import requests
    import pyfiglet
    import websocket
except ImportError:
    install('requests')
    install('websocket-client')
    install('pyfiglet')


blue = Color.blue
black = Color.black
red = Color.red
cyan = Color.cyan
white = Color.white
light_purple = Color.light_purple
dark_gray = Color.dark_gray
light_gray = Color.light_gray
green = Color.green
light_green = Color.light_green
purple = Color.purple
light_red = Color.light_red
light_blue = Color.light_blue
yellow = Color.yellow
brown = Color.brown
reset = Color.reset


class Window:
    def clear():
        os.system('cls' if os.name == "nt" else 'clear')

    def close():
        print(yellow)
        input("Thanks for using this app.\nPress any key to exit...")
        quit()


class Status:
    def __init__(self, token, customStatusTxt, emoji):
        self.token = token
        self.text = customStatusTxt
        self.emoji = emoji
        self.ws = websocket.WebSocket()

    def update(self):
        while True:
            self.ws.connect(url = 'wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream')
            self.ws.send(json.dumps({"op":2,"d":{"token": self.token,"capabilities":125,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"fr","browser_user_agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0","browser_version":"95.0","os_version":"","referrer":"https://discord.com/","referring_domain":"discord.com","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":107767,"client_event_source":None},"presence":{"status":"online","since":0,"activities":[],"afk":False},"compress":False,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}))
            print(light_blue + '[+] Updating Status' + reset)
            self.ws.send(json.dumps({"op":3,"d":{"status":"dnd","since":0,"activities":[{"type": 4, "name": "Custom Status", "state": self.text, "emoji": {"id": None, "name": self.emoji, "animated": False}}],"afk":False}}))
            time.sleep(20)


class VoiceChat:
    def __init__(self, token, guildId, channelId):
        self.ws = websocket.WebSocket()
        self.token = token
        self.guildId = guildId
        self.channelId = channelId
        self.mute = True
        self.deaf = True
    
    def join(self):
        while True:
            self.ws.connect("wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream")
            self.ws.send(json.dumps({"op":2,"d":{"token": self.token,"capabilities":125,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"fr","browser_user_agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0","browser_version":"95.0","os_version":"","referrer":"https://discord.com/","referring_domain":"discord.com","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":107767,"client_event_source":None},"presence":{"status":"online","since":0,"activities":[],"afk":False},"compress":False,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}))
            print(light_blue + "[+] Updating")
            self.ws.send(json.dumps(
                {
                    "op": 4,
                    "d": {
                        "guild_id": self.guildId,
                        "channel_id": self.channelId,
                        "self_mute": self.mute,
                        "self_deaf": self.deaf
                        }
                    }
            ))
            time.sleep(30)


class AutoBump:
    def __init__(self):
        self.sesh = requests.Session()
        self.title = pyfiglet.figlet_format("Auto  Bump  Server")

    def bump(self, token: str, channelId: int):
        self.sesh.post(url = f"https://discord.com/api/v9/channels/{channelId}/messages", 
        headers = {"Authorization": token, "Content-Type": "Application/json"},
        json = {"content": "!d bump"})
        print(light_blue + "Successfully bumped!" + reset)

    def start(self):
        print(light_purple)
        print(self.title)
        TOKEN = input("Enter your discord token: ")
        CI = int(input("Enter the channel id: "))
        self.bump(TOKEN, CI)


class DankMemer:
    def __init__(self):
        self.sesh = requests.Session()
        self.title = pyfiglet.figlet_format("Dank  Member  Auto  Grinder")

    def grinder(self, token: str, channelId: int):
        Window.clear()
        while True:
            print(light_red)
            beg = {
                "content": "pls beg"
            }
            fish = {
                "content": "pls fish"
            }
            hunt = {
                "content": "pls hunt"
            }
            dig = {
                "content": "pls dig"
            }
            time.sleep(1)
            print("Executing pls beg")
            self.sesh.post(
                url = f"https://discord.com/api/v9/channels/{channelId}/messages",
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                },
                json = beg
            )
            time.sleep(1)
            print("Executing pls fish")
            self.sesh.post(
                url = f"https://discord.com/api/v9/channels/{channelId}/messages",
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                },
                json = fish
            )
            time.sleep(1)
            print("Executing pls hunt")
            self.sesh.post(
                url = f"https://discord.com/api/v9/channels/{channelId}/messages",
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                },
                json = hunt
            )
            time.sleep(1)
            print("Executing pls dig")
            self.sesh.post(
                url = f"https://discord.com/api/v9/channels/{channelId}/messages",
                headers = {
                    "Authorization": token,
                    "Content-Type": "application/json"
                },
                json = dig
            )
            print("Waiting for the cooldown to be over...")
            time.sleep(45)

    def start(self):
        print(light_blue)
        print(self.title)
        TOKEN = input("Enter your discord token: ")
        CI = int(input("Enter the channel id in which you want to grind: "))
        print("Press [j] if you want to exit.")
        self.grinder(TOKEN, CI)


class WebhookSpammer:
    def __init__(self):
        self.title = pyfiglet.figlet_format("Webhook  Spammer")

    def spammer(self, webhook_url: str, ts: int, msg):
        print(blue)
        for ___i___ in range(ts):
            requests.post(
                url = webhook_url,
                json = {
                    "content": msg
                }
            )
        print("Spam Done")
        time.sleep(1.5)
        Window.clear()

    def start(self):
        print(cyan)
        print(self.title)
        WEBHOOK_URL = input("Enter the webhook url: ")
        HTS = int(input("Enter how many times to spam: "))
        MESSAGE = input("Enter the message: ")
        self.spammer(WEBHOOK_URL, HTS, MESSAGE)


class TypingSpammer:
    def __init__(self):
        self.title = pyfiglet.figlet_format("Typing  Spammer")
        self.sesh = requests.Session()

    def spammer(self, channelId: int, token: str):
        self.sesh.post(
            url = f"https://discord.com/api/v9/channels/{channelId}/typing",
            headers = {
                "Authorization": token,
                "Content-Type": "Application/json"
            }
        )
        print(purple)
        print("Typing Spammer Started.")
        print("This will only last for few seconds.")

    def start(self):
        print(light_red)
        print(self.title)
        CHID = int(input("Enter the channel id: "))
        TK = input("Enter your discord token: ")
        self.spammer(CHID, TK)
        time.sleep(2)


class GetGuildInfo:
    def __init__(self):
        self.title = pyfiglet.figlet_format("Guild  Info")
        self.sesh = requests.Session()

    def getinfo(self, guildInviteCode):
        ginfo = self.sesh.get(f"https://discord.com/api/v9/invites/{guildInviteCode}").text
        if "Unknown Invite" in ginfo:
            print("This server does not exist.")
            input("Press any key...")
            Main().start()
        info = json.loads(ginfo)
        guildId = info['guild']['id']
        guildName = info['guild']['name']
        guildDesc = info['guild']['description']
        guildVerLvl = info['guild']['verification_level']
        guildNsfw = info['guild']['nsfw']
        guildNsfwLvl = info['guild']['nsfw_level']
        print(light_blue)
        print(f"""
Id:                 {guildId}
Name:               {guildName}
Description:        {guildDesc}
Verification Level: {guildVerLvl}
Nsfw:               {guildNsfw}
Nsfw Level:         {guildNsfwLvl}
""")
        input("Press any key...")
    def start(self):
        print(light_green)
        print(self.title)
        code = input("Enter the server invite code: (Note only enter the code, for eg: wqmdgP4e) ")
        self.getinfo(code) 


class Main:
    def __init__(self):
        self.title = pyfiglet.figlet_format("Discord  Tools")

    def main(self):
        while True:
            Window.clear()
            time.sleep(1)
            print(light_blue)
            print(self.title)
            print("""
_________________________________________________________________
|                                                               |
|   [1] Status Changer                 [2] Join VC              |
|                                                               |
|   [3] Auto Bump Server               [4] Dank Memer Grinder   |
|                                                               |
|   [5] Webhook Spammer                [6] Typing Spammer       |
|                                                               |
|   [7] Guild Info                     [8] Exit                 |
|_______________________________________________________________|
""")
            try:
                choice = int(input("Enter your choice > "))
            except ValueError:
                print("Please type an integer.")
                time.sleep(1.5)
                self.main()
            if choice == 1:
                Window.clear()
                time.sleep(1)
                print(light_blue)
                pyfiglet.print_figlet("Status  Changer")
                sctk = input("Enter your discord token: ")
                scst = input("Enter the status text: ")
                scem = input("Enter the emoji: ")
                status = Status(sctk, scst, scem)
                status.update()

            elif choice == 2:
                Window.clear()
                time.sleep(1)
                print(light_purple)
                pyfiglet.print_figlet("Vc  Joiner")
                vctk = input("Enter your discord token: ")
                vcgi = int(input("Enter the guild id: "))
                vcci = int(input("Enter the channel id: "))
                vc = VoiceChat(vctk, vcgi, vcci)
                vc.join()

            elif choice == 3:
                Window.clear()
                time.sleep(1)
                AutoBump().start()

            elif choice == 4:
                Window.clear()
                time.sleep(1)
                DankMemer().start()

            elif choice == 5:
                Window.clear()
                time.sleep(1)
                WebhookSpammer().start()

            elif choice == 6:
                Window.clear()
                time.sleep(1)
                TypingSpammer().start()

            elif choice == 7:
                Window.clear()
                time.sleep(1)
                GetGuildInfo().start()

            elif choice == 8:
                Window.clear()
                Window.close()
        
            else:
                print("Invalid Choice.")
                time.sleep(1.5)
                self.main()
    
    def start(self):
        self.main()


discord_tools = Main()
discord_tools.start()