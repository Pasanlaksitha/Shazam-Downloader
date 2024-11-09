import csv
import yt_dlp as youtube_dl
import json
from youtubesearchpython import VideosSearch
import datetime
import os

# Set current time for logging and navigate to the script's directory
time = datetime.datetime.now()
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Reads the CSV file, retrieves YouTube links, and downloads MP3s
def csv_reader(file_name):
    num_rows = 0
    # Count total rows for progress tracking
    for _ in open(file_name, encoding="utf-8"):
        num_rows += 1

    # Open the CSV file and process each song entry
    with open(f'{file_name}', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            # Skip the header row
            if line_count == 0:
                line_count += 1
            else:
                # Ensure row has valid data for processing
                if row[0].isdigit():
                    line_count += 1
                    file_number, song_title, artist_name = row[0], row[2], row[3]
                    
                    # Construct the filename without .mp3 to avoid duplicates
                    shazam_file_name = f"{artist_name} - {song_title}"
                    
                    # Skip if the file is already downloaded
                    if os.path.exists(f"downloads/{shazam_file_name}.mp3"):
                        print(f"Skipping {shazam_file_name}.mp3 (already downloaded)")
                        continue
                    
                    # Search YouTube and download the song
                    try:
                        # Get YouTube link using song name
                        link, _ = youtube_search(shazam_file_name)
                        # Download and save as MP3
                        downloader(link, shazam_file_name)
                        # Log the downloaded song
                        log(f"{shazam_file_name}.mp3")
                        print(f"{line_count}/{num_rows -1} files downloaded")
                    except IndexError:
                        # If no results found, skip this song
                        print(f"No YouTube results found for {shazam_file_name}. Skipping.")
                    except Exception as e:
                        print(f"An error occurred for {shazam_file_name}: {e}")

        print(f'Downloaded {line_count} Songs.')

# Searches YouTube for the song and returns the link
def youtube_search(shazam_file_name):
    # Search for the song title on YouTube
    videosSearch = VideosSearch(f'{shazam_file_name}', limit=1)
    result = json.loads(json.dumps(videosSearch.result()))
    
    # If no search result, raise an error to skip this song
    if not result['result']:
        raise IndexError("No results found.")
    
    # Extract the video link and title
    link = result['result'][0]['link']
    yt_title_name = result['result'][0]['title']
    return link, yt_title_name

# Downloads the YouTube video as an MP3 file
def downloader(link, shazam_file_name):
    try:
        options = {
            'format': 'bestaudio[ext=m4a]/bestaudio/best',  # Best available audio format
            'keepvideo': False,  # Only keep the audio
            'outtmpl': f'downloads/{shazam_file_name}',  # Filename for saving (no .mp3 here)
            'retries': 5,  # Retry on failure
            'socket_timeout': 15,  # Timeout for network issues
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',  # Convert to MP3
                'preferredcodec': 'mp3',
                'preferredquality': '320',  # Set audio quality to 320 kbps
            }],
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        }

        # Download and process the audio using yt-dlp
        with youtube_dl.YoutubeDL(options) as ydl:
            ydl.download([link])
        print(f"Download complete... {shazam_file_name}.mp3")
        
    except youtube_dl.utils.DownloadError as e:
        # Handle download errors
        print(f"Failed to download {shazam_file_name}: {e}")

# Logs the downloaded song to a log file
def log(song):
    # Append the song name and download time to log.txt
    with open('log.txt', 'a', encoding="utf8") as log_file:
        log_file.write(f"{time} \t {song} \n")

# Start the download process
file_name = input("Enter File Name in same directory: ")
csv_reader(file_name)
