from flask import Flask, render_template_string
import requests

app = Flask(__name__)

# URL dari file index.html di GitHub
GITHUB_HTML_URL = 'hfrom flask import Flask, render_template_string
import requests

app = Flask(__name__)

# URL dari file index.html di GitHub
GITHUB_HTML_URL = 'https://raw.githubusercontent.com/USERNAME/REPOSITORY/BRANCH/index.html'

@app.route('/')
def index():
    # Mendapatkan isi file index.html dari GitHub
    response = requests.get(GITHUB_HTML_URL)
    html_content = response.text
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)'

@app.route('/')
def index():
    # Mendapatkan isi file index.html dari GitHub
    response = requests.get(GITHUB_HTML_URL)
    html_content = response.text
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
