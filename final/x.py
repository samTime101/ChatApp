import json
import os
import playsound
from gtts import gTTS
language = 'en'
tld='co.uk'
with open('data.txt','r') as responsex:
    response = responsex.read()
    response_data = response.strip().splitlines()
    name = response_data[0].split(":")[1].strip()
# responsex = open("data.txt", "r")


with open('./1.json', 'r') as json_file:
    students_data = json.load(json_file)
for student in students_data:
    if student['name'].lower() == name.lower():  
        student['attendence'] = "present"
        break

with open('./1.json', 'w') as json_file:
    json.dump(students_data, json_file, indent=4)
    if name.lower() == "samip regmi":
        result = f"Successfully marked attendence as present for my boss and creator {name}"
        print(result)
        # myobj = gTTS(text=result, lang=language, slow=False,tld=tld)
        # myobj.save("attendence_boss.wav")
        # playsound.playsound("attendence_boss.wav")
    else:
        result = f"Successfully marked attendence as present for {name}"
        print(result)
        # myobj = gTTS(text=result, lang=language, slow=False,tld=tld)
        # myobj.save("attendence_boss.wav")
        # playsound.playsound("attendence_boss.wav")

os.system('http-server -p 8000 & xdg-open http://localhost:8000')