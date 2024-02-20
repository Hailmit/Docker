from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load sample data from JSON file
with open('sample.json', encoding='utf-8-sig') as f:
    sample_data = json.load(f)


def get_user_by_age(age):
    for user in sample_data:
        if isinstance(user, dict) and user.get('age') == age:
            return user
    return None



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        age = int(request.form['age'])
        user = get_user_by_age(age)
        if user:
            return render_template('result.html', user=user)
        else:
            return render_template('result.html', error="No user found with that age.")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)