from config import Config
import pyrebase

class Firebase():
    firebase = pyrebase.initialize_app(Config.FIREBASE_CONFIG_JSON)

    def login(self, email, password):
        # Authenticate with firebase
        auth = self.firebase.auth()

        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print(user)
        except:
            print('Failed to login')
            return None
        else:
            print('Login successful')
            return user