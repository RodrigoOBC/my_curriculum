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
        
        