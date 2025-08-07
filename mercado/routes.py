from mercado import app, db
from flask import  render_template, redirect, url_for, flash, request
from mercado.model import Item, User
from mercado.forms import CadastroForm, LoginForm, CompraProdutoForm, VenderProdutoForm
from flask_login import login_user, logout_user, login_required, current_user



@app.route('/')
def page_home():
    return render_template('home.html')


@app.route('/produtos', methods=["GET", "POST"])
@login_required
def page_produtos():
    compra_form = CompraProdutoForm()
    venda_form = VenderProdutoForm()
    if request.method == 'POST':
        compra_produto = request.form.get('compra_produto')
        produto_aux = Item.query.filter_by(nome = compra_produto).first()
        #COMPRA PRODUTO
        if produto_aux:      # se o produto existe
            if current_user.compra_disponivel(produto_aux):   #se o user tem saldo
                produto_aux.compra(current_user)
                flash(f"Produto Adquirido! {produto_aux.nome}", category="success")
            else:
                flash(f"Saldo Insuficiente para a Compra!", category="danger")

        #VENDA PRODTUTO
        venda_produto = request.form.get("venda_produto")
        produto_venda_aux = Item.query.filter_by(nome = venda_produto).first()
        if produto_venda_aux:
            if current_user.venda_disponivel(produto_venda_aux):
                produto_venda_aux.venda(current_user)
                flash(f"Voce Vendeu o Produto {produto_venda_aux.nome}", category="success")
            else:
                flash(f"A venda não foi possivel!", category="danger")

                
        return redirect(url_for("page_produtos"))
    if request.method == "GET":
        itens = Item.query.filter_by(dono = None)
        dono_itens = Item.query.filter_by(dono = current_user.id)
        return render_template('produtos.html' ,itens=itens, compra_form = compra_form, dono_itens = dono_itens, venda_form=venda_form)
 

@app.route('/login', methods=['GET', 'POST'])
def page_login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        usuario_log = User.query.filter_by(usuario = form_login.usuario.data).first()   # se o login existe

        if usuario_log and usuario_log.converte_senha(form_login.senha1.data):     #se o login do form bateu com a senha
            login_user(usuario_log)
            flash(f"Bem vindo de Volta {usuario_log.usuario}", category="success")
            return redirect(url_for('page_produtos'))
        else:
            flash("Usuario ou Senha incorretos!", category="danger")
    return render_template("login.html", form = form_login)



@app.route('/cadastro', methods=['GET','POST'])
def page_logout():
    logout_user()
    flash("Sessão Encerrada", category="info")
    return redirect(url_for("page_home"))

@app.route('/cadastro', methods=['GET','POST'])
def page_cadastro():
    form = CadastroForm()
    if form.validate_on_submit():
        usuario_forms = User(
            usuario = form.usuario.data,
            email = form.email.data,
            senhacrip = form.senha1.data
        )
        
        db.session.add(usuario_forms)
        db.session.commit()
        return redirect(url_for('page_produtos'))
    if form.errors != {}:
        for erro in form.errors.values():
            flash(f"Erro: {erro}", category="danger")
    return render_template("cadastro.html", form=form)
