from sqlalchemy import text
from datetime import date
from app.models import db, Album, environment, SCHEMA
def seed_album():
    album1 =  Album(
                title = 'First Title',
                cover_img = 'https://azad-new-bucket.s3.us-east-2.amazonaws.com/a0a1ba547cd2408e8fa305cab3cddcce.png',
                description = 'First Album',
                artist_id = 1,
                num_songs = 1,
                release_date = date.today()
                )
    db.session.add(album1)
    db.session.commit()

def undo_albums():
        if environment == "production":
            db.session.execute(f"TRUNCATE table {SCHEMA}.albums RESTART IDENTITY CASCADE;")
        else:
            db.session.execute(text("DELETE FROM albums"))
        
        db.session.commit()