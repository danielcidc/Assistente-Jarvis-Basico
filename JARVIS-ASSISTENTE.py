import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia

# Inicializando o reconhecedor de voz
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')

# Definindo a voz padrão
engine.setProperty('voice', voices[0].id)

# Função para falar
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Função para cumprimentar o usuário falar a hora atual
def time():
    speak("Bem vindo, mestre!")
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    print(Time)
    speak(f"Agora são {Time}")

time() 

# Função para pesquisar um tópico na Wikipédia
def wiki():
    topico = input("Digite o tópico para pesquisar na wikipedia: ")
    query = (f"{topico}")
    results = wikipedia.summary(query, sentences=2)
    speak("De acordo com a wikipédia, ")
    print(results)
    speak(results)

wiki()

# Função para transcrever comandos de voz captados pelo microfone do usuário
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Escutando...")
        r.pause_threshold = 1
        audio = r.listen(source) 

    try:
        print("Reconhecendo...")
        query = r.recognize_google(audio, language= 'pt-br')
        print(f"Você disse:{query}\n")

    except Exception as e:
        print(e)
        print("Não entendi, fale novamente...")
        speak("Fale novamente, por favor")
        return "None" 
    return query 

take_command()