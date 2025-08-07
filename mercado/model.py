from mercado import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id   ))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(length=30), nullable = False)
    preco = db.Column(db.Integer, nullable = False)
    cod_de_barra = db.Column(db.String(length =12), nullable = False)
    descricao = db.Column(db.String(length= 1024), nullable = False)
    dono = db.Column(db.Integer, db.ForeignKey('user.id'))

    def compra(self, usuario):

        self.dono = usuario.id
        usuario.valor -= self.preco
        db.session.commit() 

    def venda(self, usuario):
        self.dono = None  # tira o dono do produto
        usuario.valor += self.preco
        db.session.commit()

    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key= True)
    usuario = db.Column(db.String(length=30), nullable = False, unique = True)
    email = db.Column(db.String(length=50), nullable = False, unique=True)
    senha = db.Column(db.String(length=60), nullable = False)
    valor = db.Column(db.Integer, nullable=False, default=5000)
    itens = db.relationship('Item', backref='dono_user', lazy=True)

    @property
    def senhacrip(self):
        return self.senhacrip
     
    @senhacrip.setter
    def senhacrip(self, senha_texto):
        self.senha = bcrypt.generate_password_hash(senha_texto).decode("utf-8")

    def converte_senha(self, senha_texto_claro):
        return bcrypt.check_password_hash(self.senha, senha_texto_claro)
    
    def compra_disponivel(self, produto_aux):
        return self.valor >= produto_aux.preco
    
    def venda_disponivel(self, produto_aux):
        return produto_aux in self.itens     #se ele esta no campo itens do User, que tem todos itens do usuario