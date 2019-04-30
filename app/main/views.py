from flask import Flask
from . import main
from flask import render_template, request, redirect, url_for, abort, flash
from flask_login import login_required, current_user
from ..models import User, Blog, Comment,Subscriber
from .forms import UpdateProfile, PostForm , CommentForm
from .. import db, photos 
import json
import requests



# @main.route('/')
# def index():
    


# views
@main.route("/")
def index():
    
   random = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()
    
   title = 'Personal-Blog'
   blogs = Blog.query.all()

   return render_template('index.html', title= title, blogs = blogs, random=random)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',blogs = blogs, user= user)
    
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname, blog_id):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()

    return redirect(url_for('main.profile',uname=user.username))

    return render_template('profile/update.html',form=form)

@main.route('/post/new', methods=['GET','POST'])
@login_required
def new_blog(id):
    form = BlogForm()

    if form.validate_on_submit():

        title=form.title.data
        content=form.content.data
        category=form.category.data
        blog = form.blog_post.data
        # new_blog =new_ blog(title=title,category=category,blog=blog,blogger=current_user._get_current_object().id)

        db.session.add(post)
        db.session.commit()

        flash('Your blog has been created...!', 'success')

        subscribers = Subscriber.query.all()
        for subscriber in subscribers:
            mail_message("New Blog Post", "email/new_blog", subscriber.email, subscriber = subscriber)

        return redirect(url_for('main.index', id=new_blog.id))

    return render_template('new_blog.html', title='Add Blog', blog_form=form)


@main.route('/comment/new/<int:id>', methods=['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()

    if form.validate_on_submit():
        
        comment_content = form.comment.data

        comment = Comment(comment_content= comment_content, blog_id=id)

        db.session.add(comment)
        db.session.commit()
        
    comment = Comment.query.filter_by(blog_id=id).all()
    return render_template('new_comment.html', blog=blog, comments=comments, user=user)

@main.route('/music/new', methods=['GET','POST'])
# @login_required
def music(category = "Music"):

    musics = Blog.query.filter_by(category = "Music")
    
    title = "Music Blog"
    return render_template('music.html', music= music, title=title)



@main.route('/adventure/new', methods=['GET','POST'])
# @login_required
def adventure(category = "Adventures"):

    adventures = Post.query.filter_by(category = "Adventures")
    
    title = "Adventures Blog"
    return render_template('adventure.html', adventures= adventures, title=title, blog = 'blog')


@main.route('/celebrity/new', methods=['GET','POST'])
# @login_required
def celebrity(category = "Celebrity"):

    celebritys = Post.query.filter_by(category = "Celebrity")
    
    title = "Celebrity Blog"
    return render_template('celebrity.html', celebrity= celebrity, title=title, post ='New Post')


@main.route('/nature/new', methods=['GET','POST'])
# @login_required
def nature(category = "Nature"):

    natures = Post.query.filter_by(category = "Nature")
    
    title = "Nature Blog"
    return render_template('nature.html', natures= natures, title=title, post ='New Post')

@main.route('/fashion/new', methods=['GET','POST'])
# @login_required
def fashion(category = "Fashion"):

    fashions = Post.query.filter_by(category = "Fashion")
    
    title = "Fashion Blog"
    
    return render_template('fashion.html', fashions= fashions, title=title, post ='New Post')

@main.route('/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete(id):
   del_post = Post.query.filter_by(id=id).first()
   db.session.delete(del_post)
   db.session.commit()
   
   return redirect(url_for('main.index'))    





