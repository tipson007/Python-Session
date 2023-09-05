from flask import Flask

app=flask(__name__)

@app.route('/')
def home():
    return "website content goes here"

if __name__=="__main__":
    app.run(debug=True)
