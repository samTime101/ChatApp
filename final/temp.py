from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def handle_post():
    data = request.data.decode('utf-8')
    print(f"Received POST data: {data}")
    with open('imagedata.txt','w') as idata:
        idata.write(data)
    return "POST request received!", 200
# print(f"{data}")
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
