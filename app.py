from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Thank you for the oppurtunity sir... Looking forward for the feedbak!!!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
