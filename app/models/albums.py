from .db import db

class Album(db.Model):
    __tablename__ = 'albums'
    id = db.Column(db.Integer)
    title = db.Column(db.String)
    cover_img = db.Column(db.String)
    description = db.Column(db.String)
    artist_id = db.Column(db.Integer)
    num_songs = db.Column(db.Integer)
    release_date = db.Column(db.Date)
    
    user = db.relationship('User', back_populates = 'album')

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




