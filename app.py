import json
from flask import Flask
from flask import render_template


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    with open("static/data/personal_data.json", encoding='utf-8') as my_json:
        personal_data = json.load(my_json)
        
    return render_template('index.html',data=personal_data)




if __name__ == "__main__":
    app.run(debug=True)