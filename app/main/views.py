<<<<<<< HEAD
from flask import Flask
from . import main
import datetime
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required
from ..models import User, Post, Comment
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos
app = Flask(__name__)


# views
@main.route("/")
def index():
   
   title = 'Personal-Blog'
   posts = Post.query.all()

   return render_template('index.html', title= title, posts = posts)
=======
# from flask import Flask
from flask import render_template,redirect,url_for,abort,flash
from app import app
from ..import db,photos
from flask_login import login_required, current_user
from .. models import User, Pitch, Comment
# from . forms import RegistrationForm
from . forms import UpdateProfile, PitchForm, CommentForm
# from ..email import mail_message
from . import main
import markdown2




#views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch panel'
    pitches = Pitch.query.all()


    return render_template('index.html', title= title, pitches = pitches)
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

<<<<<<< HEAD
=======
    if user is None:
        abort (404)


>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

<<<<<<< HEAD
    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
=======
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

    return render_template('profile/update.html',form =form)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

<<<<<<< HEAD
@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
=======
@main.route('/pitch/new', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
<<<<<<< HEAD
        post = Post(title=title, content=content,category=category)
        db.session.add(post)
        db.session.commit()

        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index', id=post.id))

    return render_template('new_post.html', title='New Post', post_form=form, post ='New Post')


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content, post_id=id)

        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(post_id=id).all()
    return render_template('new_comment.html', title='New Post', comment=comment,comment_form=form, post ='New Post')

@main.route('/music/new', methods=['GET','POST'])
@login_required
def music(category = "Music"):

    musics = Post.query.filter_by(category = "Music")
    
    title = "Music Blogs"
    return render_template('music.html', musics= musics, title=title, post ='New Post')



@main.route('/adventure/new', methods=['GET','POST'])
@login_required
def adventure(category = "Adventures"):

    adventures = Post.query.filter_by(category = "Adventures")
    
    title = "Adventures Blogs"
    return render_template('adventure.html', adventures= adventures, title=title, post ='New Post')


@main.route('/celebrity/new', methods=['GET','POST'])
@login_required
def celebrity(category = "Celebrity"):

    celebritys = Post.query.filter_by(category = "Celebrity")
    
    title = "Celebrity Blogs"
    return render_template('celebrity.html', celebritys= celebritys, title=title, post ='New Post')


@main.route('/nature/new', methods=['GET','POST'])
@login_required
def nature(category = "Nature"):

    natures = Post.query.filter_by(category = "Nature")
    
    title = "Nature Blogs"
    return render_template('nature.html', natures= natures, title=title, post ='New Post')

@main.route('/fashion/new', methods=['GET','POST'])
@login_required
def fashion(category = "Fashion"):

    fashions = Post.query.filter_by(category = "Fashion")
    
    title = "Fashion Blogs"
    
    return render_template('fashion.html', fashions= fashions, title=title, post ='New Post')

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
   del_post = Post.query.filter_by(id=id).first()
   db.session.delete(del_post)
   db.session.commit()
   
   return redirect(url_for('main.index'))    





=======
        pitch.likes = 0
        pitch.dislikes = 0

        pitch = Pitch(title=title, content=content,category=category, user = current_user)
        db.session.add(pitch)
        db.session.commit()

        flash('Your pitch has been created!', 'success')
        return redirect(url_for('main.index'))

    return render_template('pitch.html', form=form)



@main.route('/reviews/<pitch_id>/like')
@login_required
def like(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())
    like = pitch.like()

    return render_template('reviews.html', pitch = pitch, reviews = reviews, like = like)

@main.route('/reviews/<pitch_id>/dislike')
@login_required
def dislike(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    reviews = Review.query.filter_by(pitch_id = pitch.id).order_by(Review.posted.desc())
    dislike = pitch.dislike()

    return render_template('reviews.html', pitch = pitch, reviews = reviews, dislike =dislike)

@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():

        comment_content = form.comment.data
        comment = Comment(comment_content= comment_content,pitch_id=id)

        db.session.add(comment)
        db.session.commit()
        return redirect(url_for(".index"))

    comment = Comment.query.filter_by(pitch_id=id).all()



    return render_template('pitch.html', my_form=form,comment=comment)
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709
