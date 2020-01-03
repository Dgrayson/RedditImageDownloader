import praw
import os
import urllib.request
import json
import wget
import tkinter



file_path = "c:/users/dgray/desktop/reddit image downloader/Images/"

_directory = ""

def parseUrl(url):

    parsedUrl = ""

    parsedUrl = url.rsplit('/', 1)[-1]

    if "." in parsedUrl:
        wget.download(url, out=_directory)
    else:
        print("invalid url")      

def CheckDirectory(name):

    if not os.path.exists(file_path + name):
        os.makedirs(file_path + name)

    return file_path + name

def GetSubreddits(sub_name):

    global _directory

    for sub in reddit.subreddit(sub_name).hot(limit=10):
        
        print()
        print()
        print(sub.title + "  :  " + sub.url)
        _directory = CheckDirectory(sub.author.name)
        parseUrl(sub.url)


def main():
    sub_name = input("Enter subreddit name: ")
    GetSubreddits(sub_name)


if __name__ == "__main__":
    main()
