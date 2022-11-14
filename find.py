import pychromecast

chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=["ベッドルーム"])
print(chromecasts)
