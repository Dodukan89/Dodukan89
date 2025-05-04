import random
from flask import Flask, render_template, url_for, request, redirect , send_from_directory 
import config
from config import ultrakillrandom
from flask_sqlalchemy import SQLAlchemy
import secrets
from sqlalchemy.exc import IntegrityError
from flask_login import current_user, login_required, LoginManager, login_user , UserMixin


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app )
login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

def result_calculate(size, lights, device):
    home_coef = 100
    light_coef = 0.04
    devices_coef = 5   
    return size * home_coef + lights * light_coef + device * devices_coef 

@app.route('/')
def home():
    return f'''
    <html>
        <head>
            <title> XD </title>
            <style>
                @keyframes p1frame {{
                    0% {{ transform: translate(0px, 0px); color: #1b1919; }}
                    25% {{ transform: translate(50px , -50px); color: #464646; }}
                    50% {{ color: #969696; }}
                    75% {{ transform: translate(-50px , 50px); color: #464646; }}
                    100% {{ transform: translate(0px, 0px); color: #000000; }}
                }}
                body {{
                    background-color: #292929;
                    color: white;
                    font-family: Arial, sans-serif;
                    text-align: center;
                }}
                a {{
                    display: block;
                    color: #1dffc6;
                    font-size: 20px;
                    margin: 10px auto;
                    text-decoration: none;
                }}
                a:hover {{
                    color: #ff5500;
                }}
                button {{
                    color: rgb(255, 255, 255);
                    border: 2px solid rgb(0, 140, 55);
                    padding: 12px 24px;
                    font-size: 16px;
                    font-weight: bold;
                    border-radius: 8px;
                    cursor: pointer;
                    transition: background-color 0.3s, transform 0.2s;
                    text-decoration: none;
                    display: inline-block;
                }}

                .button:hover {{
                    transform: scale(1.05);
                }}

                .button:active {{
                    transform: scale(0.98);
                }}
                html, body {{
                    margin: 0;
                    padding: 0;
                    width: 100%;
                    height: 100%;
                    overflow-x: hidden;
                }}

                .header {{
                    background-repeat: repeat;
                    background-position: left;
                    background-color: #181515;
                    width: 100vw;
                    height: auto;
                    margin: 0;
                    padding: 0;
                }}
            </style>
        </head>
        <body>

        <header class="header">
            <h1> Selam! </h1>
            <p> Ben Dodukan89! Aşağıda merak ettiğin yerler varsa bir bakmanı isterim :D </p>
        </header>
            <a href="{url_for('home01')}">Teknoloji bağımlılığı hakkında bilgiler!</a>
            <a href="{url_for('home02')}">Ultrakill</a>
            <a href="{url_for('sifre01')}">Yetkili Harici Giremez</a>
            <a href="{url_for('sifre02')}">Yetkili Harici Giremez</a>
            <a href={ url_for('index2') } class="button">Çevre Dostu Musun? Teste Katıl!</a>
            <a href="{ url_for('miims')}">Miim sayfası</a>
            <a href="{ url_for('home29')}">M4L1</a>
        </body>
    </html>
    '''

@app.route('/teknoloji-bagimliligi')
def home01():
    return render_template('index.html')

@app.route('/ultrakill')
def home02():
    
    return render_template("index.html")

@app.route('/sifre-kontrol', methods=['GET', 'POST'])
def sifre01():
    if request.method == 'POST':
        girilen_sifre = request.form.get('sifre')
        config.ilksifre

        print("Girilen şifre:", girilen_sifre)
        print("Doğru şifre:", config.ilksifre)
        if girilen_sifre.strip() == config.ilksifre.strip():
            return redirect(url_for("yetkili_sayfa"))
        else:
            return "Yanlış şifre! Tekrar deneyin.", 403
        
    return '''
<!DOCTYPE html>
<html lang="tr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Güvenlik Duvarı</title>
        <style>
            body {
                text-align: center;
                background-color: #121212;
                color: white;
                font-family: Arial, sans-serif;
            }
            h2 {
                text-align: center;
                font-size: 24px;
            }
            form {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin-top: 20px;
            }
            input {
                padding: 10px;
                width: 200px;
                font-size: 16px;
                margin-bottom: 10px;
                border: 1px solid white;
                background: transparent;
                color: white;
                border-radius: 5px;
                text-align: center;
            }
            input::placeholder {
                color: rgba(255, 255, 255, 0.7);
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                background-color: #007BFF;
                color: white;
                border: none;
                cursor: pointer;
                border-radius: 5px;
                transition: 0.3s;
            }
            button:hover {
                background-color: #ff5500;
                transform: scale(1.05);
            }
        </style>
    </head>
    <body>
        <h2>Bu sayfaya erişmek için şifre girin:</h2>
        <form method="POST">
            <input type="password" name="sifre" placeholder="Şifre girin..." required>
            <br>
            <button type="submit">Giriş</button>
        </form>
    </body>
</html>
'''

@app.route('/sifre-kontrol-2', methods=['GET', 'POST'])
def sifre02():
    if request.method == 'POST':
        girilen_sifre = request.form.get('sifre')
        config.ikincisifre

        print("Girilen şifre:", girilen_sifre)
        print("Doğru şifre:", config.ikincisifre)
        if girilen_sifre.strip() == config.ikincisifre.strip():
            return redirect(url_for("fazladan_bir_sayfa"))
        else:
            return "Yanlış şifre! Tekrar deneyin.", 403
        
    return '''
    <!DOCTYPE html>
    <html lang="tr">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Güvenlik Duvarı</title>
            <style>
                body {
                    text-align: center;
                    background-color: #121212;
                    color: white;
                    font-family: Arial, sans-serif;
                }
                h2 {
                    text-align: center;
                    font-size: 24px;
                }
                form {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    margin-top: 20px;
                }
                input {
                    padding: 10px;
                    width: 200px;
                    font-size: 16px;
                    margin-bottom: 10px;
                    border: 1px solid white;
                    background: transparent;
                    color: white;
                    border-radius: 5px;
                    text-align: center;
                }
                input::placeholder {
                    color: rgba(255, 255, 255, 0.7);
                }
                button {
                    padding: 10px 20px;
                    font-size: 16px;
                    background-color: #007BFF;
                    color: white;
                    border: none;
                    cursor: pointer;
                    border-radius: 5px;
                    transition: 0.3s;
                }
                button:hover {
                    background-color: #ff5500;
                    transform: scale(1.05);
                }
            </style>
        </head>
        <body>
            <h2>Bu sayfaya erişmek için şifre girin:</h2>
            <form method="POST">
                <input type="password" name="sifre" placeholder="Şifre girin..." required>
                <br>
                <button type="submit">Giriş</button>
            </form>
        </body>
    </html>
    '''

@app.route('/Nurihemdem-Devleti')
def yetkili_sayfa():
    return render_template("index.html")

@app.route('/XD')
def fazladan_bir_sayfa():
    return render_template('index.html')

# Çevre dostu musun?
@app.route('/Çevre-farkındalığı')
def index2():
    return render_template('index.html')

#Cihazlar
@app.route('/<size>')
def lights(size):
    return render_template(
                            'index.html', 
                            size=size
                           )

#Işık
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'index.html',
                            size = size, 
                            lights = lights                           
                           )

#Sonuç sayfası
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    try:
        size = int(size)
        lights = int(lights)
        device = int(device)

        result = result_calculate(size, lights, device)

        return render_template('index', result=result)
    except ValueError:
        return "Hata: Geçersiz giriş! Lütfen sayı girin.", 400
    except Exception as e:
        return f"Beklenmeyen bir hata oluştu: {str(e)}", 500
    
#Form sayfası
@app.route('/form')
def form():
    return render_template('index.html')

#Form alındı!
@app.route('/submit', methods=['POST'])
def submit_form():
    # Veri toplama için değişkenleri tanımlayın
    name = request.form['name']
    email = request.form['email']
    address = request.form['address']
    date = request.form['date']

    with open('form.txt', 'a') as f:
        f.write(f"Name: {name}, Email: {email}, Address: {address}, Date: {date}\n")

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz
    return render_template('index.html', 
                           # Değişkenleri buraya yerleştirin
                           name=name,
                           email=email,
                           address=address,
                           date=date

                           )

#Miim oluşturma sayfası
@app.route('/randommiim', methods=['GET','POST'])
def miims():
    if request.method == 'POST':

        selected_image = request.form.get('image-selector')

        textTop = request.form.get('textTop')
        textBottom = request.form.get('textBottom')

        selected_color = request.form.get('color-selector')

        textTop_Y = request.form.get('textTop_Y')
        textBottom_Y = request.form.get('textBottom_Y')

        return render_template('index3.html', 

                               selected_image=selected_image,

                               textTop=textTop,
                               textBottom=textBottom,

                               selected_color=selected_color,

                               textTop_Y=textTop_Y,
                               textBottom_Y=textBottom_Y

                               )
    else:
        # Varsayılan olarak ilk resmi görüntüleme
        return render_template('index3.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    subtitle = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

def __repr__(self):
        return f'<Card {self.id}>'

# İçerik sayfasını çalıştırma
@app.route('/M4L1')
def home29():
    cards = Card.query.order_by(Card.id).all()
    

    

    return render_template('index4.html',
                           cards = cards
                           )



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'









# İçerik sayfasını çalıştırma
@app.route('/login', methods=['GET','POST'])
def login():
    error = ''
    if request.method == 'POST':
        form_login = request.form['username']
        form_email = request.form['email']
        form_password = request.form['password']
        
        # Kullanıcı adı veya e-posta ile kullanıcıyı bul
        user = User.query.filter((User.username == form_login) | (User.email == form_email)).first()
        
        if user and user.password == form_password:
            login_user(user)  # 🟢 Girişi burada gerçekleştiriyoruz
            return redirect('/account')
        else:
            error = 'Incorrect login or password'
            return render_template('login.html', error=error)
            
    return render_template('login.html')



@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        username = request.form['username']
        login = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(username=login).first()
        existing_user = User.query.filter_by(email=login).first()
        if existing_user:
            return "Bu e-posta zaten kayıtlı!"

        try:
            user = User(username=login, email=login, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
        except IntegrityError:
            db.session.rollback()
            return "Kayıt sırasında bir hata oluştu. Tekrar dener misin? "
    
    return render_template('registration.html')

# Kartla sayfayı çalıştırma
@app.route('/card/<int:id>')
def card(id):
    card = Card.query.get(id)
    

    return render_template('card.html', card=card)

# Sayfayı çalıştırma ve kart oluşturma
@app.route('/create')
def create():
    return render_template('create_card.html')

# Kart formu
@app.route('/form_create', methods=['GET','POST'])
def form_create():
    if request.method == 'POST':
        title =  request.form['title']
        subtitle =  request.form['subtitle']
        text =  request.form['text']

        card = Card(title=title, subtitle=subtitle, text=text)
        db.session.add(card)
        db.session.commit()
        




        return redirect('/')
    else:
        return render_template('create_card.html')
    
@app.route('/account', methods=['GET'])
@login_required  # Sadece giriş yapmış kullanıcılar erişebilir
def account():
    return render_template('account.html', user=current_user)

@app.route('/upload', methods=['GET', 'POST'])
def upload_profile_pic():
    # Profil fotoğrafı yükleme işlemleri
    return render_template('upload.html')

        

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
