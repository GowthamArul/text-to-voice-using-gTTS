from gtts import gTTS
import os
import os.path


mytext ="Hi all, Welcome to the programming world"

language ="en"


if os.path.isfile('output.mp3'):
    print('file already exist')
else:
    print('file does not exist, creating new one')
    output = gTTS(text=mytext, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")


