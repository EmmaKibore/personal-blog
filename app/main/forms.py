from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField

<<<<<<< HEAD
class PostForm(FlaskForm):

    title = StringField('Blog title')
    category= SelectField('Blog Category', choices=[('Select a category', 'Select a category'),('Music', 'Music'),('Adventures', 'Adventures'),('Fashion', 'Fashion'),('Nature', 'Nature'),('Celebrity', 'Celebrity')])
    content = TextAreaField('The Blog...')
    submit = SubmitField('Post')
=======
class PitchForm(FlaskForm):

    title = StringField('Pitch title')
    category= SelectField('Pitch Category', choices=[('Select a category', 'Select a category'),('Business', 'Business'),('Science and Tech', 'Science and Tech'),('Interview Pitch', 'Interview Pitch'),('Funny pitches', 'Funny pitches'),('Pick-up lines', 'Pick-up lines')])
    content = TextAreaField('The pitch...')
    submit = SubmitField('Add Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment about the particular Pitch')    
>>>>>>> 14aae2dcc0c6ce0324a855cec00bb71830ae2709


class CommentForm(FlaskForm):

    comment = TextAreaField('Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Let us get to know you better...')
    submit = SubmitField('Submit')
