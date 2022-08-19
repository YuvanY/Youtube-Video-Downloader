from pytube import YouTube

yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

ytVideoUrl = input('Paste The Url of The YouTube Video Here\n').strip()


yt = YouTube(
    ytVideoUrl,
    on_progress_callback=0,
    on_complete_callback=-0,
    use_oauth=False,
    allow_oauth_cache=True
)
print('downloading...')
yt.streams.filter(file_extension='mp4')
stream = yt.streams.get_by_itag(22)
try:
	stream.download()
except:
	print('ERROR: THE VIDEO URL DOES NOT MATCH :\'(')

print('Congrats, you\'ve downloaded your youtube video')
print(yt.title)

