from flask import Flask

from mrspooner.extensions import configuration

def create_app():
  app = Flask(__name__)
  configuration.init_app(app)
  configuration.load_extensions(app)
  return app

if __name__ == '__main__':
  app.run()