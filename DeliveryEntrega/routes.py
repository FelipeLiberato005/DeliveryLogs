#rotas das paginas
from flask import render_template, url_for, redirect, request, session, flash
from DeliveryEntrega import app, database, bcrypt
from flask_login import login_required, login_user, logout_user, current_user
from DeliveryEntrega.models import Usuario, logLogin
from DeliveryEntrega.forms import FormLogin, FormCriarConta
import os
from werkzeug.utils import secure_filename
from datetime import datetime


@app.route("/", methods=["GET", "POST"])
def homepage():
    form_login = FormLogin()
    if form_login.validate_on_submit():
        ip = request.remote_addr
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario)
            return redirect(url_for('perfil', id_usuario=usuario.id))
        # usuario nã existe - registrar tentativa
        if not usuario:
            log = logLogin(usuario_id=None, ip=ip, sucesso=False, motivo='Usuario não encontrado')
            database.session.add(log)
            database.session.commit()
            flash('Usuario não encontrado')
        return redirect(url_for('homepage'))

        #senha errada

    return render_template("homepage.html", form=form_login)


@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    form_criarconta = FormCriarConta()
    if form_criarconta.validate_on_submit():
        senha = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, senha=senha,
                          email=form_criarconta.email.data)
        database.session.add(usuario)
        database.session.commit()
        login_user(usuario, remember=True)
        return redirect(url_for("perfil", id_usuario=usuario.id))
    return render_template("criarconta.html", form=form_criarconta)


@app.route("/feed")
def feed():
    return render_template("feed.html")


@app.route("/perfil", methods=["GET", "POST"])
def perfil():
    return render_template("perfil.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("homepage"))