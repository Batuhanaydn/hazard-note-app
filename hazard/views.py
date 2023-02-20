from flask import Blueprint, render_template, request
from flask_login import login_required, current_user, flash
from .models import Note
from . import db
import json
import jsonify
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        note= request.form.get('note')

        if len(note) < 1:
            flash('Note is to short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note is to success!', category='success')

    return render_template('index.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteID =  note['noteID']
    note = Note.query.get(noteID)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    
    return jsonify({'status': 'Note has deleted'})

