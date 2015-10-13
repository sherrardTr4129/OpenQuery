import csv
from gtts import gTTS
import pyglet


age =  ""
gender = ""

with open('gender.csv', 'rb') as f:
    reader = csv.reader(f)
    your_gender_list = list(reader)
    print(your_gender_list)
    gender = your_gender_list[1][14]

with open('age.csv', 'rb') as f:
    reader = csv.reader(f)
    your_age_list = list(reader)
    age = your_age_list[1][5]

print(age, gender)

mesage_str = "hello, from my best calculations you appear to be " + str(float(age) - 20) + "years old. " + "and you are a " + gender 
print(mesage_str) 
tts = gTTS(text=mesage_str, lang="en") 
tts.save("msg.wav")

song = pyglet.media.load('msg.wav')
song.play()
pyglet.app.run()




