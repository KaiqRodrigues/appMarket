Sistema web para compra e venda de produtos, com autenticação, proteção contra ataques CSRF e uso de modais dinâmicos para confirmação de transações. Registro em Banco de Dados SQLITE.
Aplicação desenvolvida em curso na Udemy.
No repositório, anexei um relatório que fiz ao longo do desenvolvimento, acredito que aborde os principais pontos e funcionalidades.

Para aplicação, será necessário a criação do banco e das tabelas conforme a abstração no forms.py onde existe o modelo de tabela.
A estilização é opcional, utilizei bootstrap, mesclando com style direto nos elementos. 

FERRAMENTAS UTILIZADAS:
•	wtfforms permite abstração dos formularios por meio de classes no Python permitindo tambem validação no front com o "validators"
•	FlaskForm é uma classe base de form do flask_wtf - extensão flask para wtforms (um complementa o outro)
•	SQLAchemy permite abstração do banco na forma de ORm
•	FLASK-BCRYPT
Bcrypt permite a criptografia de um valor em hash

•	FLASK-LOGIN
	Gerencia sessões
- login_user
- logout-user
- login_required -> valida se esta logado para efetuar uma transação (usado em /produtos)
  
•	SQLITE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db"
