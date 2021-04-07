import flask_wtf
import wtforms
from wtforms import validators as vld


# Add a validator to these fields to make them required fields
# city’s name
# city’s country
# number of inhabitants

# class QueryForm(flask_wtf.FlaskForm):
    
#     query = wtforms.StringField("Query: ", validators=[vld.DataRequired(message="Input something..")])

#     submit = wtforms.SubmitField("Search")


class AddCities(flask_wtf.FlaskForm):

    citys_name = wtforms.StringField("City:", validators=[vld.DataRequired(message="Must fill it out")])
    citys_country = wtforms.StringField("Country", validators=[vld.DataRequired(message="Must fill it out")])
    number_of_inhabitants = wtforms.IntegerField("Number of inhabitants:", validators=[vld.DataRequired(message="Must fill it out")])
    citys_area = wtforms.IntegerField("City's area (in square km):")
    submit = wtforms.SubmitField("Add city")
