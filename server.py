from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('mainpage.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

if __name__=="__main__":
    app.run(debug=True)