from mongoengine import Document, fields

class Usuario(Document):
    nombre = fields.StringField(required=True, max_length=100)
    email = fields.EmailField(required=True, unique=True)
    
    meta = {
        'collection': 'usuarios',
        'indexes': ['email']
    }