import json
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
@app.route('/<lang>/')
def index(lang='pt'):
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
            personal_data_all = json.load(my_json)
    if lang == 'pt':
        personal_data = personal_data_all['pt']
    elif lang == 'en':
        personal_data = personal_data_all['en']
    return render_template('index.html', personal_data=personal_data, languagerTarget=lang)

@app.route('/education')
@app.route('/<lang>/education')
def education(lang='pt'):
    with open("static/data/profissional_skills_data.json", encoding='utf-8') as my_json:
        education = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
    heading = "Formação"
        
    return render_template('education.html',data=education, personal_data=personal_data,heading=heading, languagerTarget=lang)

@app.route('/work')
@app.route('/<lang>/work')
def work(lang='pt'):
    with open("static/data/profissional_skills_data.json", encoding='utf-8') as my_json:
        work = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
    heading = "Experiência"
    return render_template('experience.html',data=work,personal_data=personal_data,heading=heading, languagerTarget=lang)

@app.route('/articles')
@app.route('/<lang>/articles')
def projects(lang='pt'):
    with open("static/data/articles.json", encoding='utf-8') as my_json:
        articles = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('articles.html',data=articles,personal_data=personal_data, languagerTarget=lang)

@app.route('/repositories')
@app.route('/<lang>/repositories')
def repositories(lang='pt'):
    with open("static/data/repositories.json", encoding='utf-8') as my_json:
        repositories = json.load(my_json)
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('repository.html',data=repositories,personal_data=personal_data,  languagerTarget=lang)

if __name__ == '__main__':
    app.run(port=10000, debug=True)