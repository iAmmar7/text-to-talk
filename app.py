from flask import Flask
from routes import hello, health

app = Flask(__name__)

# Register routes
app.add_url_rule('/', view_func=hello.hello)
app.add_url_rule('/health', view_func=health.health_check)

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8000)