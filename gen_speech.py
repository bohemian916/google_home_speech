from gtts import gTTS
tts = gTTS(text='電気消費が4000ワットを超えています。エアコンをきります', lang='ja')
tts.save('./hello_world_ja.mp3')
