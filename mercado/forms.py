from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.model import User

class CadastroForm(FlaskForm):
    usuario = StringField(label="Username:",  validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label="Email:", validators=[Email(), DataRequired()])
    senha1 = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    senha2 = PasswordField(label="Confirme a Senha:", validators=[EqualTo('senha1'), DataRequired()])
    submit = SubmitField(label='Cadastrar')

    def validate_usuario(self,check_user):
        user = User.query.filter_by(usuario=check_user.data).first()
        if user:
            raise ValidationError("Usuario já Existe!")

    def validate_email(self, check_email):   
        email = User.query.filter_by(email=check_email.data).first()
        if email:
            raise ValidationError("Ja existe um Cadastro com esse Email!") 


class LoginForm(FlaskForm):
    usuario = StringField(label="Username:",  validators=[DataRequired()])
    senha1 = PasswordField(label="Senha:", validators=[DataRequired()])
    submit = SubmitField(label='Log In')

class CompraProdutoForm(FlaskForm):
    submit = SubmitField(label="Comprar Produto")

class VenderProdutoForm(FlaskForm):
    submit = SubmitField(label="Vender Produto")