# Discord-Messages-Deleter
Deletes multiple messages for you at once on Discord.

## Information
This was made to show you how easy it is to develop a Discord selfbot as it's still supported in the discord.py library. A "message deleter" could be useful if you need to delete a huge amount of messages quickly. It is against Discord's T.O.S (Terms of Service) to use selfbots so this is not anything I recommend you should use. However, if you choose to use this you are doing it at your own risk.

## Previews
![](https://i.imgur.com/YHYMvCT.png)<br/>
![](https://i.imgur.com/b5kOVpE.gif)

## Usage
Run this command in CMD, terminal or PowerShell (if you don't already have the **discord.py** library installed):
```
pip install discord.py
```
1. Replace the "token" value inside Token.json with your Discord token — see how to get your Discord token below.
2. Run the script.
3. Let it log in.

• Send "!purge 10" in the channel you would like to delete your 10 recent messages in — you can of course replace "10" with any amount you'd like.<br/>
• Send "!masspurge" in the channel you would like to delete your 500 recent messages in.

## How to get your Discord token (using Google Chrome)
1. Use the web version of Discord or the app (on your computer).
2. Go into a channel and hit Ctrl + Shift + I, you should now see your console appear.
3. Head over to the "Network" tab in the console.
4. Send any message in that Discord channel you're in.
5. You should now see a new row in the Network tab called "messages". Click on it.
6. Scroll down and under "Request Headers" you should see "authorization". Copy the value of "authorization" — that's your Discord token.
![](https://i.imgur.com/bEucEdE.png)
**DO NOT SHARE YOUR DISCORD TOKEN WITH ANYONE.**

## Legal Notice
This is once again against Discord's Terms of Service. I am not accountable for anything you get into, this was just a speedrun to demonstrate how selfbots work. This is 100% educational, please do not misuse this tool.
