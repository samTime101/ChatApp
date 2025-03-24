import PIL.Image
import os
import google.generativeai as genai
from gtts import gTTS
import playsound
from dotenv import load_dotenv
load_dotenv()

language = 'en'
tld='co.uk'

genai.configure(api_key=os.getenv("AI_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
with open('comparePROMPT.txt','r') as comparePROMPT:
    prompt = comparePROMPT.read()

student_id_folder = './student_id'
person_image_path = './person.png'
# os.system(f'eog {person_image_path} &')

sample_file_2 = PIL.Image.open(person_image_path)
def r_data(i_name):
    print(f"from function {i_name}")
    with open('ocrPROMPT.txt','r') as ocrPROMPT:
        prompt_final = ocrPROMPT.read()

    ret_image = PIL.Image.open(i_name)

    response_new = model.generate_content([ret_image,prompt_final])
    f = open("data.txt", "w")
    f.write(response_new.text)
    f.close()
    os.system('python3 x.py')
    # print(response_new.text)
matches = {}
for file_name in os.listdir(student_id_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        database = os.path.join(student_id_folder, file_name)
        # os.system(f'eog {database} & eog {person_image_path}')
        print(f"Using {file_name} for comparison...")
        # sending = f"Using {file_name} for comparison..."
        # # os.system(f'eog {database} & eog {person_image_path} &')

        # myobj = gTTS(text=sending, lang=language, slow=False,tld=tld)

        # myobj.save("sending.wav")
        # playsound.playsound("sending.wav")
        # print(f"{file_name[0]}")

        sample_file_1 = PIL.Image.open(database)
        
        response = model.generate_content([prompt, sample_file_1, sample_file_2])
        response_data = response.text.strip().splitlines()
        # print(response_data)
        # print(response_data[1].split(":")[0].strip())
        return_data = int(response_data[1])
        confidence = float((response_data[3]))
        # myobj = gTTS(text=f"scanning {file_name} now, please wait", lang=language, slow=False,tld=tld)
        # myobj.save("scanning.wav")
        # playsound.playsound("scanning.wav")
        print(f"Returned :{return_data}")
        print(f"Conficence: {confidence}")

        # print(f"{file_name[0]}")
        sample_file_1 = PIL.Image.open(database)
        if return_data == 1:
            print(f'Potential match with confidence {confidence}')
            # matches.append(database,confidence)
            matches[database] = confidence
            print(matches)
            continue
        #     print(f"{file_name} matched")
        #     print(f"RETREIVING DATA FROM {file_name}")
        #     matched = f"{file_name} successfully found , retrieving data now"
        #     myobj = gTTS(text=matched, lang=language, slow=False,tld=tld)
        #     myobj.save("match.wav")
        #     playsound.playsound("match.wav")
        #     r_data(database)
        #     break
        # print(f"{database} didnt match")
        # matched = f"{file_name} didn't match"
        # myobj = gTTS(text=matched, lang=language, slow=False,tld=tld)
        # myobj.save("notmatch.wav")
        # playsound.playsound("notmatch.wav")
max_conf = 0.0
max_loc = None
for image,conf in matches.items():
    if conf>max_conf:
        max_conf = conf
        max_loc = image
# myobj = gTTS(text=f"Found the match {max_loc} with confidence{max_conf}", lang=language, slow=False,tld=tld)
# myobj.save("found.wav")
# playsound.playsound("found.wav")

with open('match.txt','w') as match:
    match.write(max_loc)

# os.system(f'eog {max_loc} &')

r_data(max_loc)
# print(max_loc)




