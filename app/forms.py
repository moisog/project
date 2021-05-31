from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms import validators

from .models import User

def user_validator(form, field):
    if field.data=='adsi' or field.data=='Adsi':
        raise validators.ValidationError('EL username adsi no es permitido')

class LoginForm(Form):
    username = StringField('Username',[
        validators.length(min=4, max=50,
        message='El nombre de usuario debe encontarse entre 4 y 50 caracteres de largo'),

    ])
    password = PasswordField('Password',[
        validators.Required(message='El password es requerido')
    ])

class RegisterForm(Form):
    username = StringField('Username',[
        validators.length(min=4, max=50),
        user_validator
    ])
    email = EmailField('Correo electronico',[
        validators.length(min=6, max=100),
        validators.Required(message='El email es requerido.'),
        validators.Email(message='Ingrese un email valido.')
    ])
    password = PasswordField('Password',[
        validators.Required('El password es requerido.'),
        validators.EqualTo('confirm_password', message='La contraseña no coincide')
    ])
    confirm_password = PasswordField(' Confirmar contraseña')
    accept = BooleanField('', [
        validators.DataRequired()
    ])

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise validators.ValidationError('El username ya se encuentra en uso')

    def validate_email(self,email):
        if User.get_by_email(email.data):
            raise validators.ValidationError('El Email ya se encuentra en uso')

    def validate(self):
        if not Form.validate(self):
            return False

        if len(self.password.data) < 3 :
            self.password.errors.append('El password es demasiado corto')
            return False

        return True

class TaskForm(Form):
    title = StringField('Titulo', [
        validators.length(min=4, max=50, message = 'Título fuera de rango'),
        validators.DataRequired(message='El título es requerido')
    ])
    description = TextAreaField('Descripción',[
        validators.DataRequired(message='La Descripción es requerida')
    ], render_kw = {'rows':5} )
