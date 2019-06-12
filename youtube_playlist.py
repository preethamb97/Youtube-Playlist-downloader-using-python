from bs4 import BeautifulSoup
import requests
import os
from pytube import YouTube
fwrite=open("playlist_detail.txt","a")
class Playlist():
    def __init__(self, playListUrl):
        self.playListUrl = playListUrl
        self.htmldoc = requests.get(str(self.playListUrl)).text
        self.soup = BeautifulSoup(self.htmldoc, 'html.parser')
        self.rawList = self.soup('a', {'class': 'pl-video-title-link'})
        for i,link in enumerate(self.rawList):
            name=link.string
            name=name.strip()
            detail=str(i+1)+'\t'+name+'\n'
            fwrite.write(detail)
        fwrite.close()
        os.system("attrib +r playlist_detail.txt")
objPlaylist = Playlist(input('enter the playlist url :'))
