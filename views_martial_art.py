from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models.martial_arts import MartialArts
from objects.martialArtForm import MartialArtForm
from app import db, app, UPLOAD_PATH
from helpers import find_image, delete_file
import time

@app.route('/')
def index():
    martialList = MartialArts.query.order_by(MartialArts.id)

    return render_template('index.html', martialArts=martialList, title='Martial Arts')

@app.route('/new')
def newMartialArt():
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login',next_page=url_for('newMartialArt'))) 
    form = MartialArtForm()
    return render_template('new.html', title='New Martial Art', form=form)

@app.route('/martialCreate', methods=['POST', ])
def martialCreate():
    form = MartialArtForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('newMartialArt'))

    name = form.name.data
    category = form.category.data
    points = form.points.data

    martial_art = MartialArts.query.filter_by(name=name).first()
    if martial_art:
      flash('Martial art already in database!')
      return redirect(url_for('index'))

    new_martial_art = MartialArts(name=name, category=category, points=points)
    db.session.add(new_martial_art)
    db.session.commit()    

    file = request.files['cape_file']
    timestamp = time.time()

    file.save(f'{UPLOAD_PATH}/cape_{new_martial_art.id}-{timestamp}.jpg')

    flash('Martial art added with sucess!')
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    if 'user_logged' not in session or session['user_logged'] == None:
        return redirect(url_for('login',next_page=url_for('edit', id=id)))
    martial_art = MartialArts.query.filter_by(id=id).first() 
    
    form = MartialArtForm()
    form.name.data = martial_art.name
    form.category.data = martial_art.category
    form.points.data = martial_art.points

    martial_cape = find_image(id)
    return render_template('edit.html', title='Edit Martial Art', id=id, martial_cape=martial_cape, form=form)

@app.route('/martialUpdate', methods=['POST', ])
def martialUpdate():
    form = MartialArtForm(request.form)
    if form.validate_on_submit:
        martial_art = MartialArts.query.filter_by(id=request.form['id']).first()
        martial_art.name = form.name.data
        martial_art.category = form.category.data
        martial_art.points = form.points.data

        db.session.add(martial_art)
        db.session.commit()
        file = request.files['cape_file']
        timestamp = time.time()
        delete_file(martial_art.id)
        file.save(f'{UPLOAD_PATH}/cape_{martial_art.id}-{timestamp}.jpg')

        flash('Martial art updated with sucess!')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
  if 'user_logged' not in session or session['user_logged'] == None:
    return redirect(url_for('login'))
  MartialArts.query.filter_by(id=id).delete()
  db.session.commit()
  flash('Martial art Deleted with sucess!')
  return redirect(url_for('index'))

@app.route('/uploads/<file_name>')
def image(file_name):
    return send_from_directory('uploads', file_name)

