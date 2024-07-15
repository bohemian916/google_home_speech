from gtts import gTTS
tts = gTTS(text='電気消費が3500ワットを超えています。エアコンをきります', lang='ja')
tts.save('./alert_3500watt.mp3')
