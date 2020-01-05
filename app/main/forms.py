from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Optional, Length


# Forms
class PostForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    categories = StringField('Categories', validators=[DataRequired()])
    tags = StringField('Tags', validators=[Optional()])
    info = TextAreaField('Info',
                         validators=[Optional(), Length(max=254)])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')


class SearchForm(FlaskForm):
    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
