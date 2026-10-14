from flask import Flask, render_template, request, redirect, url_for
from models import db, Product

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tokyo-archive-secure-key-2026'

# Возвращаем стандартный путь к базе данных, где лежат твои 1000 товаров
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    """Главная страница: загрузка каталога из базы данных"""
    try:
        products = Product.query.all()
    except Exception as e:
        print(f"Ошибка загрузки каталога: {e}")
        products = []
        
    return render_template('index.html', products=products)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Страница входа"""
    if request.method == 'POST':
        return redirect(url_for('index'))
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Tokyo Archive — Вход</title>
        <style>
            body { background: #080808; color: #fff; font-family: -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: #121212; padding: 40px; border: 1px solid #222; border-radius: 8px; text-align: center; width: 340px; }
            h2 { margin-bottom: 10px; letter-spacing: 1px; }
            p { color: #777; font-size: 13px; margin-bottom: 25px; }
            .btn { display: inline-block; background: #fff; color: #000; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-weight: 600; font-size: 14px; }
            .btn:hover { opacity: 0.85; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>ВХОД</h2>
            <p>Модуль авторизации в разработке.</p>
            <a href="/" class="btn">На главную</a>
        </div>
    </body>
    </html>
    """

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Страница регистрации"""
    if request.method == 'POST':
        return redirect(url_for('index'))
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Tokyo Archive — Регистрация</title>
        <style>
            body { background: #080808; color: #fff; font-family: -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: #121212; padding: 40px; border: 1px solid #222; border-radius: 8px; text-align: center; width: 340px; }
            h2 { margin-bottom: 10px; letter-spacing: 1px; }
            p { color: #777; font-size: 13px; margin-bottom: 25px; }
            .btn { display: inline-block; background: #fff; color: #000; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-weight: 600; font-size: 14px; }
            .btn:hover { opacity: 0.85; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>РЕГИСТРАЦИЯ</h2>
            <p>Модуль создания аккаунта в разработке.</p>
            <a href="/" class="btn">На главную</a>
        </div>
    </body>
    </html>
    """

@app.route('/cart')
def cart():
    """Страница корзины"""
    return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Tokyo Archive — Корзина</title>
        <style>
            body { background: #080808; color: #fff; font-family: -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: #121212; padding: 40px; border: 1px solid #222; border-radius: 8px; text-align: center; width: 360px; }
            h2 { margin-bottom: 10px; letter-spacing: 1px; }
            p { color: #777; font-size: 13px; margin-bottom: 25px; }
            .btn { display: inline-block; background: #fff; color: #000; padding: 10px 20px; text-decoration: none; border-radius: 4px; font-weight: 600; font-size: 14px; }
            .btn:hover { opacity: 0.85; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>КОРЗИНА ПОКУПОК</h2>
            <p>Ваша корзина пуста.</p>
            <a href="/" class="btn">Вернуться к каталогу</a>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, port=8080)