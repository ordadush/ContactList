from config import db

class Contact(db.Model):
    #Always have to have id
    id = db.Column(db.Integer, primary_key = True)
    
    #Length, the namse don't have to be unique and won't except null
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        #In general we work with API with JSON that works like py dictanory 
        #Use camel words as a convention for json

        return {
            "id" : self.id,
            "firstName" : self.first_name,
            "lastName" : self.last_name,
            "email" : self.email, 
        }
    

