

def init_app(app):
  @app.route('/')
  def index():
    return 'Iniciando meu projeto do Chatbot Mr. Spooner!'