import praw
import os
import urllib.request
import json
import wget
from gfycat.client import GfycatClient



file_path = "c:/users/dgray/desktop/reddit image downloader/Images/"

_directory = ""

def parseUrl(url):

    parsedUrl = ""

    parsedUrl = url.rsplit('/', 1)[-1]

    if "." in parsedUrl:
        wget.download(url, out=_directory)
    else:
        if "gfycat" in url: 
            
            print("Gfylink is: " + parsedUrl)

            gfyJson = gfycatClient.query_gfy(parsedUrl)
            print(gfyJson['gfyItem']['gifUrl'])

            wget.download(gfyJson['gfyItem']['mp4Url'], out=_directory)
            print("gfycat link")
        else: 
            print("invalid url")      

def CheckDirectory(sub_name, name):

    if not os.path.exists(file_path + sub_name): 
        os.makedirs(file_path + sub_name)

    if not os.path.exists(file_path + sub_name + "/" + name):
        os.makedirs(file_path + sub_name + "/" + name)

    return file_path + sub_name + "/" + name

def GetSubreddits(sub_name):

    global _directory

    for sub in reddit.subreddit(sub_name).hot(limit=50):
        
        print("\n\n\n" + sub.title + "  :  " + sub.url)

        if sub.author.name is not None:
            _directory = CheckDirectory(sub_name, sub.author.name)
        else: 
            _directory = CheckDirectory(sub_name, 'deleted')

        print("\nDirectory: " + _directory)
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
