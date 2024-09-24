import json
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('index.html',personal_data=personal_data)

@app.route('/education')
def education():
    with open("static/data/profissional_skills_data.json", encoding='utf-8') as my_json:
        education = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('education.html',data=education, personal_data=personal_data)

@app.route('/work')
def work():
    with open("static/data/profissional_skills_data.json", encoding='utf-8') as my_json:
        work = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('experience.html',data=work,personal_data=personal_data)

@app.route('/articles')
def projects():
    with open("static/data/articles.json", encoding='utf-8') as my_json:
        articles = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('articles.html',data=articles,personal_data=personal_data)

@app.route('/repositories')
def repositories():
    with open("static/data/repositories.json", encoding='utf-8') as my_json:
        repositories = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('repository.html',data=repositories,personal_data=personal_data)

if __name__ == "__main__":
    app.run(debug=True)