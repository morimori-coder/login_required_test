from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
from flask import Flask, render_template, jsonify
from flask_login import LoginManager
import user
from user import *


login_manager = LoginManager()

# テストで使いやすいように、create_app関数を定義
def create_app():
    app = Flask(__name__)
    app.secret_key = "secret key"

    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # 本来はDBからユーザ情報を取得する
        return User(user_id, "testuser")

    # ルートとAPIエンドポイントの定義
    @app.route("/")
    def index():
        message = get_hello_message()
        return render_template("index.html", api_message=message)

    @app.route("/api/hello")
    def hello():
        message = get_hello_message()
        return jsonify({"message": message})
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        login_user(User(1, "username"))
        return render_template("index.html")
        
    # ログアウト処理
    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return render_template("index.html")
    
    # ログインが必要なページ
    @app.route("/login-required", methods=["GET"])
    @login_required
    def login_requied_page():
        return render_template("login_required.html")
    return app


def get_hello_message():
    return "Hello, Flask"


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, host="0.0.0.0")
