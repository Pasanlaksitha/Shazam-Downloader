# Shazam Music Downloader

Shazam Music Downloader is a Python application that can download playlists that you recently Shazamed using the Shazam app, and all kinds of music identified via the app, and save them as a CSV file. The app has an automation script that can read the CSV file, search for songs from YouTube using the `youtubesearchpython` library, and download them using `youtube_dl` and `ffmpeg` libraries in Python. Every song download will be included in the CSV and logged into a TXT file.

## Requirements

To use the application, you need to have Python 3.x installed on your computer. You also need to install the following Python libraries:

```
yt_dlp
youtubesearchpython
ffmpeg
```

> **Note:** To install **FFmpeg**, refer to the official [FFmpeg documentation](https://ffmpeg.org/download.html) for platform-specific instructions.

You can install the required Python libraries using `pip` and the provided `requirements.txt` file, as shown in the steps below.

## Setup

1. **Prepare the Playlist CSV File**  
   Download a playlist of songs you recently Shazamed using the Shazam app and save it as a CSV file.

2. **Clone the Repository**  
   Open your terminal or command prompt and clone this repository to your computer:

   ```bash
   git clone https://github.com/Pasanlaksitha/Shazam-Downloader.git
   cd Shazam-Downloader
   ```

3. **Create a Virtual Environment**  
   Set up a virtual environment to isolate dependencies for this project:

   ```bash
   python -m venv .venv
   ```

4. **Activate the Virtual Environment**

   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

5. **Install Dependencies**  
   Use `pip` to install the required libraries listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Application**  
   In your terminal, ensure the virtual environment is activated, and then run the application:

   ```bash
   python shazam_music_downloader.py
   ```

2. **Enter the CSV File Name**  
   When prompted, enter the name of the CSV file you downloaded in step 1.

   The application will search for and download the songs listed in the CSV file from YouTube. The downloaded songs will be saved as MP3 files in a `downloads` folder, and each download will be logged in a `log.txt` file.

## Future Improvements

In the future, the developer plans to add a graphical user interface (GUI) to the application and automate the process of creating a playlist of songs in the CSV file on Spotify.

## License

This project is licensed under the [MIT License](https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt).

Feel free to use, modify, and distribute the code as you see fit. If you have any suggestions or find any bugs, please open an issue or submit a pull request.
