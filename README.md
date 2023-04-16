# Read Me
# Shazam Music Downloader
Shazam Music Downloader is a Python application that can download playlists that you recently Shazamed using the Shazam app, and all kinds of music identified via the app, and save them as a CSV file. The app has an automation script that can read the CSV file, search for songs from YouTube using the `youtubesearchpython` library, and download them using `youtube_dl` and `ffmpeg` libraries in Python. Every song download will be included in the CSV and logged into a TXT file.

## Installation
To use the application, you need to have Python 3.x installed on your computer. You also need to install the following Python libraries:

``` 
yt_dlp 
youtubesearchpython
ffmpeg
```
+ install ffmpeg using this [documentation](https://ffmpeg.org/download.html)
You can install these libraries using `pip`, the Python package manager. Run the following command in your terminal:


```  
pip install -r requirements.txt 
 ```
## Usage
To use the application, follow these steps:

1. Download a playlist of songs that you recently Shazamed using the Shazam app and save it as a CSV file.
2. Clone this repository to your computer.
3. Open a terminal or command prompt and navigate to the directory where you cloned the repository.
4. Run the following command:
```
python shazam_music_downloader.py
```
5. When prompted, enter the name of the CSV file you downloaded in step 1.

The application will automatically search for and download the songs in the CSV file from YouTube. The downloaded songs will be saved as MP3 files in a `downloads` folder. The application will also log each song download in a `log.txt` file.

## Future Improvements
In the future, the developer plans to add a graphical user interface (GUI) to the application and automate the process of creating a playlist of songs in the CSV file on Spotify.

## License
This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

Feel free to use, modify, and distribute the code as you see fit. If you have any suggestions or find any bugs, please open an issue or submit a pull request.
