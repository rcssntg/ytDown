# import pytube
# import io
# import tqdm


# # Get the YouTube video URL
# video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# # Create a YouTube object
# youtube = pytube.YouTube(video_url)

# # Get the highest resolution stream
# stream = youtube.streams.get_highest_resolution()

# # Create a file-like object to wrap the string returned by the stream.download() method
# fd = io.BytesIO(stream.download())

# # Create a progress bar
# pbar = tqdm.tqdm(total=stream.filesize)

# # Read the file-like object and write the bytes to a file
# with open("video.mp4", "wb") as f:
#     for chunk in fd.read(1024):
#         pbar.update(len(chunk))
#         f.write(chunk)

# # Close the progress bar
# pbar.close()

# # Close the file
# f.close()

import pytube

video_url = input("Paste your youtube url: ")
yt = pytube.YouTube(video_url)

stream = yt.streams.get_highest_resolution()
print('Downloading.... Please wait...')

stream.download()
print("Download Finished!")

# import pytube

# def download_video(video_url, filepath, resolution="1080p"):
#   """Downloads a YouTube video to the specified filepath in the specified resolution."""

#   youtube = pytube.YouTube(video_url)
#   stream = youtube.streams.get_highest_resolution(resolution=resolution)
#   stream.download(filepath)

# if __name__ == "__main__":
#   # Get the YouTube video URL
#   video_url = input("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

#   # Specify the output directory and filename for the downloaded video
#   filepath = "C:/Users/RCS/Documents/PYTHON-PROJECTS/YT-videos"

#   # Download the video in 1080p resolution
#   download_video(video_url, filepath, resolution="1080p")

#   print("Video downloaded successfully!")

# import pytube
# import tqdm

# def download_video(video_url, filepath, resolution="1080p"):
#   """Downloads a YouTube video to the specified filepath in the specified resolution with a progress bar."""

#   youtube = pytube.YouTube(video_url)
#   stream = youtube.streams.get_by_resolution(resolution)

#   # Create a progress bar
#   pbar = tqdm.tqdm(total=stream.filesize)

#   # Download the video
#   with stream.download(filepath) as fd:
#     for chunk in fd.read(1024):
#       pbar.update(len(chunk))

#   pbar.close()

# if __name__ == "__main__":
#   # Get the YouTube video URL
#   video_url = input("Paste your YouTube URL here: ")

#   # Specify the output directory and filename for the downloaded video
#   filepath = "C:/Users/RCS/Documents/PYTHON-PROJECTS/YT-videos"

#   # Download the video in 1080p resolution with a progress bar
#   download_video(video_url, filepath, resolution="1080p")

#   print("Video downloaded successfully!")


# from pytube import YouTube

# # where to save
# SAVE_PATH = "C:/Users/RCS/Documents/PYTHON-PROJECTS/YT-videos" #to_do

# # link of the video to be downloaded
# link="https://www.youtube.com/watch?v=xWOoBJUqlbI"

# try:
# 	# object creation using YouTube
# 	# which was imported in the beginning
# 	yt = YouTube(link)
# except:
# 	print("Connection Error") #to handle exception

# # filters out all the files with "mp4" extension
# mp4files = yt.filter('mp4')

# #to set the name of the file
# yt.set_filename('GeeksforGeeks Video')

# # get the video with the extension and
# # resolution passed in the get() function
# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
# try:
# 	# downloading the video
# 	d_video.download(SAVE_PATH)
# except:
# 	print("Some Error!")
# print('Task Completed!')
