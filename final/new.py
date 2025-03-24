import PIL.Image
import os
import google.generativeai as genai
from gtts import gTTS
import playsound
language = 'en'
tld='co.uk'

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("AI_KEY"))
model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")

prompt = '''
[IMPORTANT INSTRUCTIONS]
You will analyze two images and determine if they belong to the same person. 

Guidelines for analysis:
- Carefully compare facial features, including eyes, nose, mouth, hairstyle, skin tone, and overall appearance.
- Consider all potential factors like ethnicity, age, gender, and lighting conditions.

Output Instructions:
- If you believe both images represent the same person, respond with "1".
- If you believe the images do not represent the same person, respond with "0".
- After the decision, provide a concise reason for your choice (e.g., "The nose shape and eye alignment differ" or "Both images share identical features, including facial proportions and hairstyle").

**Output Format**:
RESULT:
[1 or 0]
REASON:
[Your reason here]

Ensure your response strictly follows the format. Do not include any additional details or commentary beyond the format above.
S IS HIGHLY SENSITIVE CHECK FACE CAREFULLY]
[ALSO IF U THINK U HAVE ANY SUSPICIOUS THINKING U CAN PUT 0 AS THERE WILL BE MORE IMAGES
ONLY PUT 1 IF YOU ARE 97% BELIEVE THEY ARE SAME PERSON ELSE 0
]
'''

student_id_folder = './student_id'
person_image_path = './person.png'


sample_file_2 = PIL.Image.open(person_image_path)
def r_data(i_name):
    print(f"from function {i_name}")
    prompt_final = '''
    return format
    no need to write in json write in normal text
    name: return student name
    collegename:return collegename
    studentid:return student id number starting with NP
    stream:return stream
    no need to send anything more
    '''
    ret_image = PIL.Image.open(i_name)

    response_new = model.generate_content([ret_image,prompt_final])
    f = open("data.txt", "w")
    f.write(response_new.text)
    f.close()
    os.system('python3 x.py')
    print(response_new.text)

for file_name in os.listdir(student_id_folder):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        database = os.path.join(student_id_folder, file_name)
        # os.system(f'eog {database} & eog {person_image_path}')
        print(f"Using {file_name} for comparison...")
        sending = f"Using {file_name} for comparison..."

        myobj = gTTS(text=sending, lang=language, slow=False,tld=tld)

        myobj.save("sending.wav")
        playsound.playsound("sending.wav")
        # print(f"{file_name[0]}")

        sample_file_1 = PIL.Image.open(database)
        
        response = model.generate_content([prompt, sample_file_1, sample_file_2])
        response_data = response.text.strip().splitlines()
        print(response_data[1].split(":")[0].strip())
        return_data = int(response_data[1].split(":")[0].strip())
        myobj = gTTS(text=f"scanning {file_name} now, please wait", lang=language, slow=False,tld=tld)

        myobj.save("scanning.wav")
        playsound.playsound("scanning.wav")
        # print(f"{file_name[0]}")
        sample_file_1 = PIL.Image.open(database)
        if return_data == 1:
            print(f"{file_name} matched")
            print(f"RETREIVING DATA FROM {file_name}")
            matched = f"{file_name} successfully found , retrieving data now"
            myobj = gTTS(text=matched, lang=language, slow=False,tld=tld)
            myobj.save("match.wav")
            playsound.playsound("match.wav")
            r_data(database)
            break
        print(f"{database} didnt match")
        matched = f"{file_name} didn't match"
        myobj = gTTS(text=matched, lang=language, slow=False,tld=tld)
        myobj.save("notmatch.wav")
        playsound.playsound("notmatch.wav")





