import unittest
from app.models import Pitch, User

class PitchTest(unittest.TestCase):
    '''
    Test Class to test teh Behaviourof the Pitch class
    '''
    def Setup(self):
        '''
        set up method that will run before every Test
        '''

        self.new_user = User(username = 'emma', password = '1234', email = 'emmaKibore@gmail.com')
        self.new_pitch = Pitch(id=50,title = 'My pitch',content='I can pitch all day long',category ='pickuplines',user_id = 10)

        def tearDown(self):
        User.query.delete()
        Pitch.query.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch,Pitch))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_content,"Pitch content")
        self.assertEquals(self.new_pitch.pitch_category,'pickup')
        self.assertEquals(self.new_pitch.user,self.new_user)

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    
    
