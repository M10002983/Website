
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('C:\max siewert\index.html')

@app.route('/execute', methods=['POST'])
def execute():
    import subprocess
    result = subprocess.run(['echo', 'Hello from the server!'], capture_output=True, text=True)
    return result.stdout

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Nutze hier einen anderen Port, z.B. 5001


