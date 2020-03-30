import speech_recognition as sr
r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listening...")
    r.pause_threshold =1
    audio = r.listen(source)

  try:
    print("recognizing...")
    query = r.recognize_google(audio,language='en-in')
    print(f"you said:{query}\n")

  except Exception as e:
     #print(e)
     print("sorry sir! i can't recognize please say that again....")
     return "None"
  
  return query
