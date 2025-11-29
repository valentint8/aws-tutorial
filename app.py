from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask on ECS Fargate! 🚀 This is a modification which will lead to a new version!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)