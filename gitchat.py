import speech_recognition as sr
import openai
from gtts import gTTS
from playsound import playsound
anahtar=openai.api_key="Buraya API keyinizi giriniz"
def sesAl(sure=8):
    tanimlayici=sr.Recognizer()
    with sr.Microphone()as ses:
        tanimlayici.adjust_for_ambient_noise(ses)
        print("Sesinizi Tanımlıyor...")
        kaydet=tanimlayici.record(ses,sure)
        metin=tanimlayici.recognize_google(kaydet,language="tr")
        return metin

chat=openai.Completion.create(model="text-davinci-003",prompt=sesAl(4),temperature=0.8,max_tokens=200,top_p=1,best_of=1)
text=chat.choices[0].text.replace('\n','')

tts=gTTS(text=text,lang="tr",slow=False)
tts.save("chat.mp3")
playsound("Buraya mp3 dosyasını kaydettiğiniz dizin yolunu girin")