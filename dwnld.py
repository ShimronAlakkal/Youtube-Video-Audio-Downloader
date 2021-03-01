import pafy 

time = int(input("How many songs are you upto downloading ? "))
n = 0
while time >n : 
	videoToGetAudioFrom = input('Link to the video here : ')

	video = pafy.new(videoToGetAudioFrom)
	Streams = video.audiostreams

	# the bitrate for audio 
	print()
	print('****************************************************')
	for rate in Streams:

		print('Quality = ',rate.bitrate, ' , ext : ',rate.extension , ' , size : ',round(rate.get_filesize()/1024/1024 , 2))
		
	print()
	print('****************************************************') 
	
	downloadWhich = int(input('stream to download (enter 10 to get highest quality download): '))

	try:
		if downloadWhich != 10:
			Streams[downloadWhich].download(r'C:/Users/hp/Desktop/youtube/download')
		else:
			video.getbestaudio().download()
	except :
		print('ERROR:')

	n += 1