import json
from flask import Flask
from flask import render_template
from src.script import LanguageProcessor


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
language_processor = LanguageProcessor()


@app.route('/')
@app.route('/<lang>/')
def index(lang='pt'):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    if lang not in ['pt', 'en']:
        personal_data = language_processor.get_language_json(
            personal_data_all, 'pt')
        return render_template('404.html', personal_data=personal_data, languagerTarget="pt"), 404

    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    return render_template('index.html', personal_data=personal_data, languagerTarget=lang)


@app.route('/education')
@app.route('/education/')
@app.route('/<lang>/education')
@app.route('/<lang>/education/')
def education(lang='pt'):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    education_all = language_processor.get_json(
        "static/data/profissional_skills_data.json")
    education = language_processor.get_language_json(education_all, lang)
    if lang == 'pt':
        heading = "Formação"
    else:
        heading = "Education"

    return render_template('education.html', data=education, personal_data=personal_data, heading=heading, languagerTarget=lang)


@app.route('/work')
@app.route('/work/')
@app.route('/<lang>/work')
@app.route('/<lang>/work/')
def work(lang='pt'):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    work_all = language_processor.get_json(
        "static/data/profissional_skills_data.json")
    work = language_processor.get_language_json(work_all, lang)
    if lang == 'pt':
        heading = "Experiência"
    else:
        heading = "Experience"
    return render_template('experience.html', data=work, personal_data=personal_data, heading=heading, languagerTarget=lang)


@app.route('/articles')
@app.route('/<lang>/articles')
@app.route('/articles/')
@app.route('/<lang>/articles/')
def projects(lang='pt'):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    with open("static/data/articles.json", encoding='utf-8') as my_json:
        articles = json.load(my_json)

    return render_template('articles.html', data=articles, personal_data=personal_data, languagerTarget=lang)


@app.route('/repositories')
@app.route('/repositories/')
@app.route('/<lang>/repositories')
@app.route('/<lang>/repositories/')
def repositories(lang='pt'):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    repositories_all = language_processor.get_json(
        "static/data/repositories.json")
    repositories = language_processor.get_language_json(repositories_all, lang)
    return render_template('repository.html', data=repositories, personal_data=personal_data,  languagerTarget=lang)


@app.errorhandler(404)
def page_not_found(e):
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, "pt")
    return render_template('404.html', personal_data=personal_data, languagerTarget="pt"), 404


if __name__ == '__main__':
    app.run(port=10000, debug=True)
