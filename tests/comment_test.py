import unittest
from app.models import Comment, Pitch, User
from flask_login import current_user
from app import db

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the comment class
    '''

    self.user_anto = User(username='emma',password='1234',email='emmaKibore@gmail.com')
        self.new_pitch = Pitch(pitch_content = "Pitch Test", pitch_category='Technology',user=self.user_emma)
        self.new_comment = Comment(comment_content = "Test Comment", pitch=self.new_pitch, user=self.user_emma)
    

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = Comment(id =1, comment_content = 'This pitch is wondrous!')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
