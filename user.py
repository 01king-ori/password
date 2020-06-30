class Users:
    """
    This creates new instances of a user
    """
    users_list = []


def __init__(self, name, username, login_password):
    '''
    __init__ method that helps us save properties of the user
     '''

    self.name = name
    self.username = username
    self.login_password = login_password

    def save_user(self):
        '''
       this saves  the user info
       '''

    Users.users_list.append(self)


def delete_user(self):
    '''
    delete user details
    '''
    Users.users_list.remove(self)


@classmethod
def find_by_username(cls, username):
    '''
    Searching for username
    '''
    for user in Users.users_list:
        if user.username == username:
            return user
        else:
                print("You have entered an invalid username")
@classmethod
def user_exists(cls,username,login_password):
    '''
    authenticate user username and password
    '''
    for user in Users.users_list:
        if user.username == username and user.login_password == login_password:
            return True
        else:
                return False