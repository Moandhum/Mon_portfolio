from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def projects():
    with open('data/projects.json', encoding='utf-8') as f:
        projects = json.load(f)
    return render_template('projects.html', projects=projects)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)



