import json
from flask import render_template


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
