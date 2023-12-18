from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,FileField
from wtforms.validators  import DataRequired
from flask_wtf.file import FileAllowed,FileRequired
from ..models.AWS_file import ALLOWED_EXTENSIONS

class AlbumForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    cover_img = FileField('Cover Image',validators= [FileAllowed(list(ALLOWED_EXTENSIONS)),FileRequired()])
    description = StringField('Desctiption', validators=[DataRequired()])
   