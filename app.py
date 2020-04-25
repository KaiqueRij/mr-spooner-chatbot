from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Iniciando meu projeto do Chatbot Mr. Spooner!'

if __name__ == '__main__':
  app.run()