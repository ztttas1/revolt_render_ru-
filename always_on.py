from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
  return '<h1>Page is under construction.</h1><br><a href="https://app.revolt.chat/bot/01HS541Y8H5TQMWVEQD2VK213M">Invite</a><br><a href="https://revoltbots.org/bots/01HS541Y8H5TQMWVEQD2VK213M/vote">Vote</a>'


def run():
  app.run(host="0.0.0.0", port=8080)


def activate():
  server = Thread(target=run)
  server.start()
