import csv
import yt_dlp as youtube_dl
import json
from youtubesearchpython import VideosSearch
import datetime
import os

time = datetime.datetime.now()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def csv_reader(file_name):
    num_rows = 0
    for _ in open(file_name):num_rows += 1
    with open(f'{file_name}') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                if row[0].isdigit() == True:
                    line_count += 1
                    file_number, song_title, artist_name  = row[0], row[2], row[3]
                    shazam_file_name = song_title + ' - ' + artist_name
                    link, yt_title_name, shazam_file_name = youtube_search(shazam_file_name, file_number) #youtube search link by name
                    downloader(link, yt_title_name, shazam_file_name)   #youtube Download mp3 by link
                    log(shazam_file_name)
                    print(f"{line_count}/{num_rows} files downloaded")
                else:
                    pass

                

        print(f'Downloaded {line_count} Songs.')


def youtube_search(shazam_file_name, file_number):

    videosSearch = VideosSearch(f'{shazam_file_name}', limit = 1)
    result = json.loads(json.dumps(videosSearch.result()))
    link = result['result'][0]['link']
    yt_title_name = result['result'][0]['title']
    return link, yt_title_name, shazam_file_name

def downloader(link, yt_title_name, shazam_file_name):
    video_url = link
    video_info = youtube_dl.YoutubeDL().extract_info(url = video_url,download=False)
    filename = f"{video_info['title']}.mp3"

    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':'downloads/'+shazam_file_name +'.mp3'
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Download complete... {}".format(shazam_file_name))

def log(song):
    log = open('log.txt', 'a')
    log.write(f"{time} \t {song} \n")


file_name = input(str("Enter File Name in same directory: "))
csv_reader(file_name)

