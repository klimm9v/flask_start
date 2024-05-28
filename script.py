import os
import subprocess
import venv

name = input("Введите имя проекта: ")
os.mkdir(name)
os.chdir(name)
env_dir = 'venv'
venv.create(env_dir, with_pip=True)
os.path.join(env_dir, 'bin', 'activate')
pip_executable = os.path.join(env_dir, 'bin', 'pip')
subprocess.run([pip_executable, "install"] + ["flask", "flask_sqlalchemy", "flask_migrate"])



with open("wsgi.py", "x") as file:
    file.write("from app.app import app\n")
    file.write("\n")
    file.write("if __name__ == '__main__':\n")
    file.write("    app.run(debug=True)")


    
os.mkdir("app")
os.chdir("app")
os.mkdir("static")
os.mkdir("templates")
with open("app.py", "x") as file:
    file.write("from flask import Flask, render_template, request, session, redirect, url_for, abort\n")
    file.write("from flask_sqlalchemy import SQLAlchemy\n")
    file.write("from flask_migrate import Migrate\n")
    file.write("\n")
    file.write("app = Flask(__name__)\napp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'\ndb = SQLAlchemy(app)\n")
    file.write("migrate = Migrate(app, db)\n")
    file.write("app.secret_key = '12345'\n")
    file.write("\n")
    file.write("\n")
    file.write("@app.route('/index', methods=['GET', 'POST'])\n")
    file.write("def index():\n")
    file.write("  if request.method == 'POST':\n")
    file.write("    pass\n")
    file.write("  return render_template('hello world')\n")



os.chdir("static")
css = open("style.css", "x")
os.chdir('..')
os.chdir("templates")
with open("index.html", "x") as file:
    file.write("<!DOCTYPE html>\n<head>\n")
    file.write('     <link rel="stylesheet" href="{{ url_for("static", filename="index.css") }}">\n')
    file.write("     <html lang='en'>\n     <meta charset='UTF-8'>\n     <meta meta name='viewport' content='width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no'>\n</head>\n")
    file.write("<body>\n</body>")
