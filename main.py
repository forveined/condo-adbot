import os
import time
import requests
import colorama
from colorama import Fore, Style, init

def sendad(channelid, message, gameid, token):
    
    url = f"https://discord.com/api/v9/channels/{channelid}/messages"

    headers = {
        "Authorization": f"{token}",
        "Content-Type": "application/json"
    }

    payload = {
        "content": message + f"\nhttps://www.roblox.com/games/{gameid}",
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print(Fore.GREEN + "Sent advertisement.")
    else:
        if response.status_code == 429:
            print(Fore.RED + "You are being ratelimited.")
        else:
            if response.status_code == 403: 
                print(Fore.RED + "You are banned or your token is invalid.")

def readtokens(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def readchannels(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

def getmessage(filename):
    with open(filename, "r") as file:
        return file.read().strip()

def main():
    gameid = input("Enter the game id: ")

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        print(Fore.WHITE + f"\033]0;Adbot V2 | by: forveined#0001\a", end="")

        tokens = readtokens("token.txt")
        channels = readchannels("channels.txt")
        message = getmessage("message.txt")

        for channelid in channels:
            for token in tokens:
                print(Fore.YELLOW + f"Sending message with token {token} to channel {channelid}")
                sendad(channelid, message, gameid, token)

        time.sleep(120)

if __name__ == "__main__":
    init()
    main()
