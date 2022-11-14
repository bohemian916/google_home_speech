import pychromecast

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["ベッドルーム"])
cast = chromecasts[0]
mc = cast.media_controller
cast.wait()
mc.play_media('https://www.ne.jp/asahi/music/myuu/wave/menuettm.mp3','audio/mp3')
#mc.play_media('https://samplelib.com/lib/preview/mp3/sample-3s.mp3','audio/mp3')
print(mc.status)
