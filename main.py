from flask import Flask, request, redirect
from bot import *
import random
from subprocess import call
import time

os.environ['IP_ADDR'] = "None"
app = Flask(__name__)
ip_address = None


@app.route('/')
def home():
    ip_address = request.environ.get('HTTP_X_FORWARDED_FOR',request.remote_addr)
    os.environ['IP_ADDR'] = ip_address
    call(["python", "bot.py"])
    time.sleep(1)
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))
