import random
import string

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = []

    def __init__ (self, application_name, account_username, account_password):
        '''
        __init method that helps us define properties for our objects
        
        '''
        self.application_name = application_name
        self.account_username = account_username
        self.account_password = account_password

    def add_credentials(self):
        '''
         saves credentials into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
         removes credentials from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of all credentials
        '''
        return Credentials.credentials_list

    @classmethod
    def find_by_application_name(cls, application_name):
        '''
        It takes in an application name and returns the credentials for the said application
        
        '''
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return credential
    
    @classmethod
    def credentials_exist(cls, application_name):
        '''
        It checks if a credential exist from credentials_list
    
        '''
        for credential in Credentials.credentials_list:
            if credential.application_name == application_name:
                return True
        return False

    @staticmethod
    def generate_password(passwordLength):
        '''
        method that generates a random password for the user
        '''
        random_alphanumeric = string.ascii_letters + string.digits
        password = ''.join((random.choice(random_alphanumeric) for i in range(passwordLength)))
        return password