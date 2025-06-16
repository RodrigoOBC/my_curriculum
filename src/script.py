import json
from flask import render_template
from dotenv import load_dotenv
import os
from .DB.Mongo_oparator import MongoOperator


class LanguageProcessor:
    def __init__(self):
        pass

    def get_json(self, file_path):
        with open(file_path, encoding='utf-8') as my_json:
            return json.load(my_json)

    def get_language_json(self, json_actual, lang_target):
        return json_actual[lang_target]

    def validate_language(self, lang):
        if lang not in ['pt', 'en']:
            return 

    def get_jobs(self, lang):
        mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
        jobs = mongo_operator.find_by_query('Experiencia', {'lang': lang})
        return jobs
    
    def get_education(self, lang):
        mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
        education = mongo_operator.find_by_query('Education', {'lang': lang})
        return education
        
    def get_skills(self, lang, type_skills):
        mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
        skills = mongo_operator.find_by_query('Skills', {'lang': lang})
        print(skills)
        skills = skills[0][type_skills]
        return skills
    
    def get_repositories(self, lang):
        mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
        repositories = mongo_operator.find_by_query('Repositories')
        repositories = repositories[0][lang]
        return repositories
    
    def get_articles(self,lang):
        mongo_operator = MongoOperator(os.getenv("URL_MONGO_DB"),'Curriculo')
        articles = mongo_operator.find_by_query('Articles', {'lang':lang})
        print(articles)
        return articles
    
    def get_curriculum(self, lang):
        match lang:
            case 'pt':
                return os.getenv("CURRICULUM_PORTUGUES")
            case 'en':
                return os.getenv("CURRICULUM_INGLES")