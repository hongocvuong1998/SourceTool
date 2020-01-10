import youtube_dl

SAVE_PATH = "/home/vuonghn/Music"

options = {
    'format': '251',  # choice of quality
    'extractaudio': True,        # only keep the audio
    'audioformat': "mp3",        # convert to mp3
    'noplaylist': True,          # only download single song, not playlist
    'outtmpl':SAVE_PATH + '/%(title)s.%(ext)s',
    # 'listformats': True,         # print a list of the formats to stdout and exit
}
with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://www.youtube.com/watch?v=sBWt6c0NcZk"])