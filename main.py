import praw
import os
import urllib.request
import json
import wget
from gfycat.client import GfycatClient

file_path = "c:/users/dgray/desktop/reddit image downloader/Images/"

_directory = ""

_currTitle = ""

def parseUrl(url):

    parsedUrl = ""

    parsedUrl = url.rsplit('/', 1)[-1]

    if "." in parsedUrl:
        temp = wget.download(url, out=_directory)
        
        renameFile(temp, ".jpg")
    else:
        if "gfycat" in url: 
            gfyJson = gfycatClient.query_gfy(parsedUrl)
            temp = wget.download(gfyJson['gfyItem']['mp4Url'], out=_directory)
            renameFile(temp, ".mp4")
        if "vid.me" in url: 
            temp = wget.download(url, out=_directory)
            renameFile(temp, ".mp4")
        else: 
            print("invalid url")      

def renameFile(fileLocation, fileExt):

    temp = _currTitle.replace('?', '')
    temp2 = temp.replace('/', '')
    temp3 = temp2.replace(':', '')
    newTitle = temp3.replace(' ', '_')
    os.rename(fileLocation, newTitle + fileExt)

def CheckDirectory(sub_name, name):

    if not os.path.exists(file_path + sub_name): 
        os.makedirs(file_path + sub_name)

    if not os.path.exists(file_path + sub_name + "/" + name):
        os.makedirs(file_path + sub_name + "/" + name)

    return file_path + sub_name + "/" + name

def GetSubreddits(sub_name):

    global _directory
    global _currTitle

    for sub in reddit.subreddit(sub_name).hot(limit=10):
        
        print("\n\n\n" + sub.title + "  :  " + sub.url)
        _currTitle = sub.title

        if sub.author.name is not None:
            _directory = CheckDirectory(sub_name, sub.author.name)
        else: 
            _directory = CheckDirectory(sub_name, 'deleted')

        parseUrl(sub.url)


def main():
    running = True
    
    while running: 
        sub_name = input("Enter subreddit name: ")
        GetSubreddits(sub_name)
        choice = input("\n\nWould you like to enter another subreddit? Y/N")

        if choice.strip(',.').lower() == 'n':
            running = False


if __name__ == "__main__":
    main()
