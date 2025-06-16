import json
from flask import Flask
from flask import render_template, request
from src.script import LanguageProcessor


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
language_processor = LanguageProcessor()


@app.route('/')
@app.route('/<lang>/')
def index(lang='pt'):
    if lang not in ['pt', 'en']:
        return page_not_found(404)
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    return render_template('index.html', personal_data=personal_data, languagerTarget=lang)


@app.route('/education')
@app.route('/education/')
@app.route('/<lang>/education')
@app.route('/<lang>/education/')
def education(lang='pt'):
    if lang not in ['pt', 'en']:
        return page_not_found(404)
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    
    education = language_processor.get_education(lang)
    had_skills = language_processor.get_skills(lang, 'HadSkills')
    curriculum_link = language_processor.get_curriculum(lang)


    if lang == 'pt':
        heading = "Formação"
    else:
        heading = "Education"

    return render_template('education.html', data=education,had_skills=had_skills, personal_data=personal_data, heading=heading, languagerTarget=lang, curriculum_link=curriculum_link)


@app.route('/work')
@app.route('/work/')
@app.route('/<lang>/work')
@app.route('/<lang>/work/')
def work(lang='pt'):
    if lang not in ['pt', 'en']:
        return page_not_found(404)
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    curriculum_link = language_processor.get_curriculum(lang)
    
    match lang:
        case 'pt':
            work = language_processor.get_jobs('pt/Br')
            heading = "Experiência"
        case 'en':
            work = language_processor.get_jobs('en/Us')
            heading = "Experience"

    soft_skills = language_processor.get_skills(lang,'Softskills')
    return render_template('experience.html', data=work,soft_skills=soft_skills, personal_data=personal_data, heading=heading, languagerTarget=lang, currulum_link=curriculum_link)


@app.route('/articles')
@app.route('/<lang>/articles')
@app.route('/articles/')
@app.route('/<lang>/articles/')
def projects(lang='pt'):
    if lang not in ['pt', 'en']:
        return page_not_found(404)
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    articles = language_processor.get_articles('pt')

    return render_template('articles.html', data=articles, personal_data=personal_data, languagerTarget=lang)


@app.route('/repositories')
@app.route('/repositories/')
@app.route('/<lang>/repositories')
@app.route('/<lang>/repositories/')
def repositories(lang='pt'):
    if lang not in ['pt', 'en']:
        return page_not_found(404)
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, lang)
    repositories = language_processor.get_repositories(lang)
    return render_template('repository.html', data=repositories, personal_data=personal_data,  languagerTarget=lang)


@app.errorhandler(404)
def page_not_found(e):
    print(request.url)
    if fr"/en" in request.url:
        language_target = "en"
    else:
        language_target = "pt"
    personal_data_all = language_processor.get_json(
        "static/data/personal_data.json")
    personal_data = language_processor.get_language_json(
        personal_data_all, language_target)
    return render_template('404.html', personal_data=personal_data, languagerTarget=language_target), 404


if __name__ == '__main__':
    app.run(port=10000, debug=True)
