from app.firebase import Firebase

class User():
    def __init__(self, email, password):
        self.id = email
        self.password = password

    @classmethod
    def get(cls, id, password):
        return Firebase().login(id, password)

    def __repr__(self):
        return '<User {}>'.format(self.id)