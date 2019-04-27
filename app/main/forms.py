from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

class PostForm(FlaskForm):

    title = StringField('Blog title')
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Music', 'Music'),('Adventures', 'Adventures'),('Fashion', 'Fashion'),('Nature', 'Nature'),('Celebrity', 'Celebrity')])
    content = TextAreaField('The Blog...')
    submit = SubmitField('Post')


class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Let us get to know you better...')
    submit = SubmitField('Submit')
