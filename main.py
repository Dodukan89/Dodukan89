# Import
from flask import Flask, render_template,request, redirect
from datetime import datetime



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    lenlail = request.form.get('email')
    coment = request.form.get('text')
    button_python = request.form.get('button_python')

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open("feedback.txt", 'a', encoding='utf-8') as f:
        f.write(f"[{now}] {lenlail}: {coment}\n")
    return render_template('index.html', button_python=button_python)




if __name__ == "__main__":
    app.run(debug=True)
