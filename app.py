from flask import Flask, render_template, request
import grader

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def grade():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)
    score = grader.grade(image_path)

    return render_template('index.html',score=score)




if __name__ == '__main__':
    app.run(port=3000, debug=True)