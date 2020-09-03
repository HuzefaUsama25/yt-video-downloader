# Made by Huzefa

import time
from pytube import YouTube
from youtubesearchpython import *
import random
import os

def getVideoLinks():
    queries = []
    n = int(input("\nNumber of Videos : "))
    for i in range(0, n):
        query = str(input(": "))
        queries.append(query)
    print("\nFinding Video Links\n\n")
    urls = []
    for topic in queries:
        search = SearchVideos(str(topic).replace(" ","+"), offset = 1, max_results = 1)
        links = search.links
        urls.append(links)
    return urls

def download(url):
    if "Videos" not in os.listdir():
        os.mkdir("Videos")
    print("\nStarting Download...")
    yt = YouTube(url)
    print("Video size: "+str(int(yt.streams.first().filesize)*10**-6)+" MB")
    #################################
    print("Your file will download in a maximum of "+str(yt.streams.first().filesize*10**-6*(0.0167))+" minutes")
    if downmultiple.subjectFolder not in os.listdir("Videos"):
        os.mkdir("Videos/"+downmultiple.subjectFolder+"/"+yt.title)
    yt.streams.get_highest_resolution().download("Videos/"+downmultiple.subjectFolder+"/"+yt.title)
    #################################
    print("Download Ended\n")


def downmultiple():
    linkstodown = getVideoLinks()
    downmultiple.subjectFolder = input("Subject for these Videos: ")
    if downmultiple.subjectFolder not in os.listdir("Videos"):
        os.mkdir("Videos/"+downmultiple.subjectFolder)
    for this in linkstodown:
        this = str(this).replace("]","").replace("[","")
        titlev = YouTube(this).title
        print(titlev)
        download(this)
        time.sleep(random.randint(1,3))

def main():
    downmultiple()

if __name__=="__main__":
    try:
        main()
    except Exception as e:
        print("There was an error:\n"+str(e))
        
