import pychromecast

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["リビングルーム"])
cast = chromecasts[0]
mc = cast.media_controller
cast.wait()
mc.play_media('https://github.com/bohemian916/google_home_speech/blob/main/notice.mp3?raw=true','audio/mp3')
#mc.play_media('https://samplelib.com/lib/preview/mp3/sample-3s.mp3','audio/mp3')
print(mc.status)
