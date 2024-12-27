import json

class LanguageProcessor:
    def __init__(self):
        pass

    def get_json(self, file_path):
        with open(file_path, encoding='utf-8') as my_json:
            return json.load(my_json)

    def get_language_json(self,json_actual, lang_target):
        return json_actual[lang_target]

