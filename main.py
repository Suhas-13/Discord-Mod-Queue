import discord, asyncio
import requests
import sqlite3
connection=sqlite3.connect("ModQueue.db")
cursor=connection.cursor()
import os
#from keras.models import load_model
#model = load_model('my_model.h5')
import numpy as np
import sys, os
#CREATE TABLE
#sql_command = """
#CREATE TABLE modqueue ( 
#ID VARCHAR(8) PRIMARY KEY,
#messageID INTEGER,
#Time FLOAT,
#Author VARCHAR(50), 
#Title VARCHAR(150),
#Score INTEGER,
#UpvoteRatio FLOAT,
#ImageURL VARCHAR(300),
#RedditURL VARCHAR(300),
#Reports VARCHAR(1000),
#Likelihood FLOAT,
#Actioned INTEGER,
#Removed INTEGER,
#Approved INTEGER);"""
count=0
global emojilist
emojilist={607132116420919316: 'Approve', 607625779949600769: 'MetaBaiting', 607625784080990218: 'Titleisthememecaption', 607625789017423872: 'MarkNSFW', 607625793417510913: 'MarkSpoiler', 607625797242454028: 'nonredditwatermark', 607625801680158721: 'Repost', 607625806616854554: 'Repostchains', 607625810777735179: 'Tooedgy', 607625815559110676: 'Normietrash', 607625819166081034: 'Personalinformation', 607625822710267934: 'Hatespeech', 607625826628010016: 'Naturaldisasters', 607625830717325335: 'Spoiler', 607625833838018562: 'Violenttragedies', 607625844268990464: 'Notadankmeme', 607625848429740033: 'Repostchains7DAY', 607625853748248581: 'spoiler7DAY', 607625858253062146: 'Askingforupvotes3DAY', 607625862778454037: 'Violenttragedies7DAY', 607625865924182036: 'Brigading', 607625869825015811: 'Brigading7DAY', 607625874317115422: 'Badmeme', 607625877357854790: 'PewdiepieVStseries', 607625885197008906: 'Violenttragedies14DAY', 607625894181470238: 'Hatespeech7dayban', 607625898811719700: 'Naturaldisasters3DAY', 607625903169601546: 'HatespeechPERMA', 607625908106559498: 'NaturaldisastersPERMANENT', 607625912300863508: 'BrigadingPERMA', 607625915949907972: 'ViolenttragediesPERMA', 607626808216649728: 'Nomemesaboutcelebritydeaths', 607627284530069510: 'Nopedomemes20DAY', 607628969889759242: 'Incitingglorifyingviolence7DAY'}
#from skimage.transform import rescale, resize, downscale_local_mean
#from skimage import io
import praw
import time
with open("dankmemeslogid.txt","a+") as f:
                        f.write("\n")
reddit = praw.Reddit(client_id='',
                     client_secret='',
                     refresh_token='',
                     user_agent='discordmodqueue by /u/hacksorskill')
authorizationreddit= praw.Reddit(client_id='',
                     client_secret='',
                     redirect_uri='https://localhost:8080',user_agent='discordmoqueue by u/hacksorskill')
print(reddit.user.me())
flag=True

flairlist={'MetaBaiting': '7758d0c2-a985-11e9-9bab-0e0839a4fa5e', 'Titleisthememecaption': '916edc2e-f06a-11e8-9f07-0e111b70abfc', 'MarkNSFW': '7e59cfb4-6616-11e9-8073-0e9988a9d5b6', 'MarkSpoiler': '482d62d6-71ae-11e9-9698-0eb9473fc964', 'nonredditwatermark': 'b62e13e4-f27d-11e8-92ec-0e8c7a6116b0', 'Repost': 'a3330782-f06a-11e8-a85f-0ebcce5fe3bc', 'Repostchains': '8f160a5c-5b67-11e9-81af-0e4583115d02', 'Tooedgy': '8d2c6eec-62de-11e9-a771-0ed15a315736', 'Normietrash': 'a5607116-f06a-11e8-ad67-0e8309d513b6', 'Personalinformation': '945f4612-f06a-11e8-8457-0e18d7ddfb6c', 'Hatespeech': 'b706c988-f06a-11e8-885a-0e5ee253237a', 'Naturaldisasters': '895ed484-5b69-11e9-9991-0efd22e2abae', 'Spoiler': 'b08b73ce-4844-11e9-a0f1-0e8303fb97d0', 'Violenttragedies': 'cf530aa0-5b69-11e9-959e-0e70548b7118', 'Nomemesaboutcelebritydeaths': '4e071ddc-976f-11e9-ad24-0e625012b1d6', 'Notadankmeme': 'a08bcee2-f06a-11e8-8a79-0e44d2f2af80', 'Repostchains7DAY': 'c2d623c6-f06a-11e8-ab86-0ee1ae2b2c90', 'spoiler7DAY': '0438a926-5f7c-11e9-bada-0e83081f75f4', 'Askingforupvotes3DAY': '97fd4062-f06a-11e8-a5df-0e775737aed0', 'Violenttragedies7DAY': '99f9e2c6-f06a-11e8-ac9a-0e8c8f78fa7c', 'Brigading': 'b1e592b8-f06a-11e8-ad9a-0e7b81c93bee', 'Brigading7DAY': 'df7ffcc8-5b67-11e9-85a6-0e64b51c095c', 'Badmeme': '8ea20ebc-f06a-11e8-8827-0e142d5f9500', 'PewdiepieVStseries': '8ec3f3ac-fc85-11e8-a8a5-0e18d55a2e62', 'Incitingglorifyingviolence7DAY': '62d7ea9e-f322-11e8-8c5c-0e775737aed0', 'Violenttragedies14DAY': '9c5c8d8e-f06a-11e8-b8fe-0ee4e763bfc6', 'Nopedomemes20DAY': 'b46d1e66-f06a-11e8-84cc-0e1e1f9c5176', 'Hatespeech7dayban': 'ba2f0b20-f06a-11e8-bcab-0e849e96c3aa', 'Naturaldisasters3DAY': 'bd3f3b28-f06a-11e8-919f-0e955e1ae188', 'HatespeechPERMA': '7253a7d0-031a-11e9-8f72-0e3cc9068b70', 'NaturaldisastersPERMANENT': '870d55b2-5b6d-11e9-b518-0e1200386cf8', 'BrigadingPERMA': 'c6ef37ac-5b6a-11e9-8ce9-0e6c3e5df2f4', 'ViolenttragediesPERMA': '9f05adea-f06a-11e8-b40d-0ee5b8c6efde'}

client = discord.Client()
@client.event

async def on_ready():
    print('logged in as: ', client.user.name, ' - ', client.user.id)

  
    
@client.event
async def on_message(message):
    if "DankOrNot" in str(message.author):
        pass
    else:
        if message.content.lower()=="!register":
            author=message.author
            await message.delete()
            await author.send("Please remember this is still in testing phases, you are responsible for checking the mod log to make sure everything is fine, if there are any issues please immediately revoke access the bot has by going to reddit.com/prefs/apps and deactivating DiscordModQueue then send a message in the registration channel with !delete, then contact HacksOrSkill")
            await author.send("Please authenticate using this URL: https://www.reddit.com/api/v1/authorize?client_id=1GNzCoxhguA_GQ&duration=permanent&redirect_uri=https%3A%2F%2Flocalhost%3A8080&response_type=code&scope=modposts+read+modflair+flair&state=STATETEST")
            await author.send("After you have clicked the link and pressed authorize, it should say page not found, copy the URL in your browser and send it in the registration channel.")
        if "https://localhost:8080" in message.content.lower():
            try:
                author=message.author
                code=authorizationreddit.auth.authorize(message.content.split("&code=")[1])
                with open("authenticationDiscord.txt","a+") as f:
                    f.write(str(author).replace(" ","")+":"+str(code)+" ")
                role = discord.utils.get(client.get_guild(590904331033640960).roles, name="Authenticated")
                await author.add_roles(role)

                await author.send("Authentication succesful!")

                await message.delete()
            except Exception as e:
                print(e)
                await author.send("An error occured, please contact HacksOrSkill.")
        #print(message.content)
        if "!delete" in message.content.lower():
            author=str(message.author).replace(" ","")
            mainauthor=message.author
            authlist=open("authenticationDiscord.txt","r").read().split(" ")
            for i in authlist:
                if author in i:
                    authlist.pop(authlist.index(i))
            with open("authenticationDiscord.txt","w+") as f:
                f.write(" ".join(authlist))
            role = discord.utils.get(client.get_guild(590904331033640960).roles, name="Authenticated")
            await mainauthor.remove_roles(role)
            await message.delete()
            await mainauthor.send("Succesfully deauthenticated. Please let HacksOrSkill know the issue or why you decided to deauthenticate.")


@client.event
async def on_reaction_add(reaction, user):
    
    if "DankOrNot" not in str(user):
        print("User reacted: " + str(user))
        message=reaction.message.content
        author=str(user)
        
        await reaction.message.delete()
        
        authlist=open("authenticationDiscord.txt","r").read().split(" ")
        for i in authlist:
            if author.replace(" ","") in i:
                tempuser = praw.Reddit(client_id='',
                     client_secret='',
                     redirect_uri='',
                     refresh_token=i.split(":")[1].replace(" ",""),
                     user_agent='discordmodqueue by /u/hacksorskill')
                

                
        submissionid=message[message.find("https://reddit.com/r/"):len(message)].split("/comments/")[1].split("/")[0]
        if str(reaction.emoji).split(":")[1].split(":")[0]=="Approve":
            print("Approving " + submissionid)
            tempuser.submission(submissionid).mod.approve()
            cursor.execute("""update modqueue set Actioned = 1,Approved=1,Removed=0 where ID = '"""+str(submissionid)+"""'""")
            connection.commit()
            
            
    
        
        else: 
            reactstr=flairlist[str(reaction.emoji).split(":")[1].split(":")[0]]
        
            
            print("Flairing " + submissionid + " with " + str(reaction.emoji).split(":")[1].split(":")[0])
            tempuser.submission(submissionid).flair.select(reactstr)
            cursor.execute("""update modqueue set Actioned = 1,Approved=0,Removed=1 where ID = '"""+str(submissionid)+"""'""")
            connection.commit()
            
           
    #await client.reaction.message   
        

    
                


print("passed")    


async def main():
    print("main running")
    await asyncio.sleep(7.5)
    while True:
        try:
            for submission in reddit.subreddit("dankmemes").mod.reports(limit=100):
                if flag==False:
                    #print(flag)
                    pass
                else:
                    #print(flag)
                    try:

                        #channel=client.get_channel(590904331033640962)
                        if submission.name[1] == "3":
                            if len(cursor.execute("select * from modqueue where ID = '"""+str(submission.id)+"""'""").fetchall()) == 0:
                                
                            
                                if submission.link_flair_text is not None and "Removed:" in submission.link_flair_text:
                                    pass
                                
                                #Redo this part using SQLite later

                                elif ".jpg" in submission.url or ".png" in submission.url:
                                    
                                    
                                    reports=""
                                    if len(submission.user_reports) > 0:
                                        reports=reports+"User Reports:\n"
                                        for i in submission.user_reports:
                                            reports=reports+str(i).replace("[","").replace("]","")+"\n"
                                    if len(submission.mod_reports) > 0:
                                        reports=reports+"\nMod Reports:\n"
                                        for i in submission.mod_reports:
                                            reports=reports+str(i).replace("[","").replace("]","")+"\n"

                                    likelihood=0
                                    totalremovals=open("discordserverlogusernames.txt","r").read().count(str(submission.author).replace(" ",""))
                                    if totalremovals == 0:
                                        likelihood+=0
                                    elif totalremovals  == 1:
                                        likelihood+=1.5
                                    elif totalremovals  == 2:
                                        likelihood+=2.5
                                    elif totalremovals > 2:
                                        likelihood+=3.5
                                    ratio=submission.upvote_ratio
                                    if ratio >= 0.9:
                                        likelihood+=0
                                    elif ratio >= 0.8 and ratio < 0.9:
                                        likelihood+=1
                                    elif ratio >= 0.7 and ratio < 0.8:
                                        likelihood+=2
                                    else:
                                        likelihood+=3
                                    
                                    usercount=0
                                    modcount=0
                                    for report in submission.user_reports:
                                        usercount+=int(report[1])
                                    modcount+=len(submission.mod_reports)
                                    modcount=modcount*2
                                    reportcount=modcount+usercount
                                    if reportcount == 1:
                                        likelihood+=0
                                    elif reportcount == 2:
                                        likelihood+=1
                                    elif reportcount == 3:
                                        likelihood+=2
                                    elif reportcount == 4:
                                        likelihood+=3

                                    else:
                                        likelihood+=3.5
                                    message=submission.title + "\n\n" + "Author: " + str(submission.author) +"\n"+"Likelihood: " +str(likelihood) + "\n\n\n" +"Created: "+str(submission.created_utc) + "\n" +"Score: " + str(submission.score) + "\n" + "Spoiler: " + str(submission.spoiler) + "\n" + "NSFW: " + str(submission.over_18) + "\n" + reports+"\n\n"+"https://reddit.com" + submission.permalink + "\n\n"+ submission.url+"\n\n"
                                    sql_command = """INSERT INTO modqueue (ID, messageID, Time, Author, Title, Score, UpvoteRatio, ImageURL, RedditURL, Reports, Likelihood, Actioned, Removed, Approved)
                    VALUES ("""+"""?,?,?,?,?,?,?,?,?,?,?,?,?,?"""+""");"""

                                    channel=client.get_channel(606905056415186977)
                                    
                                    newmessage=await channel.send(message)
                                    cursor.execute(sql_command,(str(submission.id),newmessage.id,submission.created_utc,str(submission.author),str(submission.title)[0:150],submission.score,submission.upvote_ratio,str(submission.url),"https://reddit.com" + str(submission.permalink),str(reports.replace("\n",",")),likelihood,0,0,0))
                                    connection.commit()
                                    #for emoji in client.get_guild(590904331033640960).emojis:
                                       #await newmessage.add_reaction(emoji)
                                    emojis=['Notadankmeme','MetaBaiting','Approve','Normietrash','Repost','Repostchains7DAY','Titleisthememecaption','Violenttragedies','Personalinformation','Tooedgy']

                                    emojilist=client.get_guild(590904331033640960).emojis
                                    

                                    for i in emojilist:
                                        if i.name in emojis:
                                            await newmessage.add_reaction(i)
                                    await asyncio.sleep(2)

                            
                    except Exception as e:
                        print("possibly duplicate mysql")
                        exc_type, exc_obj, exc_tb = sys.exc_info()
                        print(e)
                        print(exc_tb.tb_lineno)  
                        pass       
                
            await asyncio.sleep(4)

                    

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(e)
            print(exc_tb.tb_lineno)  

async def remove_no_longer_in_queue():
    print("Queue removal beginning")
    await asyncio.sleep(4)
    channel=client.get_channel(606905056415186977)
    while True:
        
        await client.wait_until_ready()
        print("beginning running background task")
        for item in cursor.execute("select * from modqueue where Actioned=0").fetchall():
            tempsubmission=reddit.submission(item[0])
            if tempsubmission.banned_by is not None:
                try:
                    cursor.execute("""update modqueue set Actioned = 1,Approved=0,Removed=1 where ID = '"""+str(tempsubmission.id)+"""'""")
                    connection.commit()
                    message = await channel.fetch_message(item[1])
                    await message.delete()
                except Exception as e:
                    print(e)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    print(exc_tb.tb_lineno) 
                    pass

            elif tempsubmission.approved == True:
                try:
                    cursor.execute("""update modqueue set Actioned = 1,Approved=1,Removed=0 where ID = '"""+str(tempsubmission.id)+"""'""")
                    connection.commit()
                    message = await channel.fetch_message(item[1])
                    await message.delete()

                except Exception as e:
                    print(e)
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    print(exc_tb.tb_lineno) 
                    pass
            await asyncio.sleep(1)
    
        print("Finished checking posts against queue, resuming")
        await asyncio.sleep(6)
      
async def modlog():
    print("Beginning modlog collection program.")
    with open("discordserverlogids.txt","a+") as f:
        f.write(" ")
    with open("discordserverlogusernames.txt","a+") as f:
        f.write(" ")
    while True:
        try:
            await client.wait_until_ready()
            for log in reddit.subreddit('dankmemes').mod.log(limit=100,action="editflair"):
                if log.target_permalink is None:
                    pass
                else:
                    if log.target_permalink.split("/comments/")[1].split("/")[0] in open("discordserverlogids.txt","r").read():
                        pass
                    else:
                        with open("discordserverlogids.txt","a+") as f:
                            f.write(log.target_permalink.split("/comments/")[1].split("/")[0] + " ")
                        with open("discordserverlogusernames.txt","a+") as f:
            
                            f.write(str(log.target_author) + " ")
                await asyncio.sleep(2)

        except Exception as e:
            print(e)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            print(exc_tb.tb_lineno) 
            pass
    


if __name__ == '__main__':
  
    client.loop.create_task(main())
    client.loop.create_task(remove_no_longer_in_queue())
    client.loop.create_task(modlog())
    client.run('')
    

