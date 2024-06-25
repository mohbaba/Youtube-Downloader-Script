from pytube import YouTube
import os
from moviepy.editor import VideoFileClip
from pytube.exceptions import VideoUnavailable, RegexMatchError


def download(url: str) -> None:
    try:
        yt = YouTube(url)
        audiofile = yt.streams.filter(only_audio=True).first()
        if audiofile is None:
            download_video(yt)
        else:
            download_audio(audiofile)
    except RegexMatchError as e:
        print("The link you entered is invalid")
    except VideoUnavailable as e:
        print("Video not available")


def download_audio(downloaded_audiofile) -> None:
    print(f"Downloading {downloaded_audiofile.title}...")
    downloaded_audiofile.download(output_path=os.path.expanduser('~/Downloads'))
    print(f"Download Complete, downloaded to ")


def download_video(youtube: YouTube) -> None:
    video = youtube.streams.first()
    downloaded_video = video.download(output_path=os.path.expanduser('~/Downloads'))
    convert_to_audio(downloaded_video)


def convert_to_audio(video_file) -> None:
    base, ext = os.path.splitext(video_file)
    audio_file = f"{base}.mp3"

    print(f"Converting {video_file} to audio...")

    video_clip = VideoFileClip(video_file)
    video_clip.audio.write_audiofile(audio_file)

    print(f"Conversion Complete: {audio_file}")


if __name__ == '__main__':
    youtube_url = input("Enter URL: ")
    download(youtube_url)
