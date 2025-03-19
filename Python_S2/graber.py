import os
import requests
from you_get import common as you_get
import sys
def download_video(url, output_dir="./videos"):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    sys.argv = ['you-get', '-o', output_dir, url]
    try:
        you_get.main()
        print(f"video saved in: {output_dir}")
    except Exception as e:
        print(f"failed {e}")

if __name__ == "__main__":
    video_url = input("url to download")

    download_video(video_url)