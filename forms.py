# Importing necessary classes and libraries from Flask-WTF and WTForms
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

# Form for creating a new blog post
class CreatePostForm(FlaskForm):
    # Field for the post title with a validator to ensure it's not empty
    title = StringField("Blog Post Title", validators=[DataRequired()])
    # Field for the subtitle with a validator to ensure it's not empty
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    # Field for the blog image URL with a validator to ensure it's not empty and a valid URL
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    # Field for the blog content using CKEditor to allow rich text formatting
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    # Submit button for the blog post
    submit = SubmitField("Submit Post")

# Form for registering new users
class RegisterForm(FlaskForm):
    # Field for email with a validator to ensure it's not empty
    email = StringField("Email", validators=[DataRequired()])
    # Field for password with a validator to ensure it's not empty
    password = PasswordField("Password", validators=[DataRequired()])
    # Field for name with a validator to ensure it's not empty
    name = StringField("Name", validators=[DataRequired()])
    # Submit button for registration
    submit = SubmitField("Sign Me Up!")

# Form for user login
class LoginForm(FlaskForm):
    # Field for email with a validator to ensure it's not empty
    email = StringField("Email", validators=[DataRequired()])
    # Field for password with a validator to ensure it's not empty
    password = PasswordField("Password", validators=[DataRequired()])
    # Submit button for login
    submit = SubmitField("Let Me In!")

# Form for commenting on blog posts
class CommentForm(FlaskForm):
    # Field for comment text using CKEditor for rich text formatting
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    # Submit button for the comment
    submit = SubmitField("Submit Comment")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
