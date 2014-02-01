from flask import render_template, redirect, url_for
from ..db import db
from ..models import Entry
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/insert')
def insert():
    e = Entry(title="f", body="f")
    db.session.add(e)
    db.session.commit()
    return redirect(url_for('main.list'))

@main.route('/list')
def list():
    entries = Entry.query.all()
    return render_template('list.html', entries=entries)

