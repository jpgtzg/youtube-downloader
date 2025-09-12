"""
Written by Juan Pablo Gutierrez

Download the highest quality video from YouTube.
"""

import yt_dlp


def download_highest_quality(url):
    """
    Download the highest quality video from YouTube.
    """
    ydl_opts = {
        "format": "bestvideo+bestaudio/best",  # Highest video + audio, or best fallback
        "merge_output_format": "mp4",  # Merge into MP4
        "outtmpl": "%(title)s.%(ext)s",  # Save as video title
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


if __name__ == "__main__":
    while True:
        input_url = input("Enter the YouTube playlist URL: ")
        if input_url == "exit":
            break
        download_highest_quality(input_url)
        print("Download complete")
