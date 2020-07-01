import unittest #importing the unnitest module
from user import Users
class TestUsers(unittest.TestCase):
    '''
    Defines test cases for the Users
    '''
    def initialization(self):
        '''
        initialization before each case
        '''
        self.new_user = Users("kingori","King","2001")

    def test_initialization(self):
        '''
        Tests whether initialization works properly
        '''
        self.assertEqual(self.new_user.name,"kingori")
        self.assertEqual(self.new_user.username,"king")
        self.assertEqual(self.new_user.password,"2001")
    def test_add_user(self):
        '''
        tests whether the users properties are saved
        '''
        
