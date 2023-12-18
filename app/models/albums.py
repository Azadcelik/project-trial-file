from .db import db
from sqlalchemy import ForeignKey

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer,primary_key=True,nullable=False)
    title = db.Column(db.String,nullable=False)
    cover_img = db.Column(db.String)
    description = db.Column(db.String)
    artist_id = db.Column(db.Integer,ForeignKey("users.id"))
    num_songs = db.Column(db.Integer)
    release_date = db.Column(db.Date)
    
    user = db.relationship('User',back_populates = 'album')

    def to_dict(self):
        return {
            'id': self.id,
            'title' : self.title,
            'cover_img': self.cover_img,
            'description': self.description,
            'artist_id': self.artist_id,
            'num_songs ': self.num_songs,
            'release_date': self.release_date
        }

