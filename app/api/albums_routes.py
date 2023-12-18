from flask_login import login_required
from flask import Blueprint
from ..models import Album

album_routes = Blueprint('album',__name__)


@album_routes.route('/',method=['GET','POST'])
# @login_required
def first_route():
    albums = Album.query.all()
    return [album.to_dict() for album in albums]