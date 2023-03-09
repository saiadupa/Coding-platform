import mimetypes
import os
from re import X
from unicodedata import name
from flask import Blueprint, appcontext_popped, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from .models import  Note
from . import db
import json
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        title = request.form['title']

        new_note = Note(title=title, user_id=current_user.id)

        db.session.add(new_note)
        db.session.commit()
        flash('added!', category='success')  


    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
        return jsonify({})





