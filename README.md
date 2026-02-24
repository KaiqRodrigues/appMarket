# Sistema Web de Compra e Venda de Produtos

Sistema web desenvolvido em curso da Udemy, com foco em autenticação, segurança e transações dinâmicas de produtos.
O projeto utiliza Flask, SQLAlchemy e WTForms, com suporte a modais dinâmicos para confirmação de transações e proteção contra ataques CSRF.
No repositório também está incluído um relatório de desenvolvimento, detalhando funcionalidades e decisões do projeto.


## Funcionalidades Principais
- Registro e autenticação de usuários
-	Proteção contra ataques CSRF
-	Transações com confirmação via modais dinâmicos
-	Armazenamento em Banco de Dados SQLite
-	Validação de formulários no backend e frontend
-	Criptografia de senhas com Bcrypt
-	Controle de sessões de usuário (login/logout)
________________________________________
## Requisitos
Antes de executar a aplicação, é necessário:
1.	Criar o banco de dados e as tabelas conforme abstração definida em forms.py.
2.	Instalar dependências do projeto:
pip install -r requirements.txt
3.	Rodar a aplicação:
python app.py
________________________________________
## Estrutura do Projeto
- app.py – Arquivo principal da aplicação Flask
- forms.py – Abstração dos formulários e modelos de tabelas
- templates/ – Arquivos HTML, podendo usar Bootstrap ou estilos diretos
- static/ – CSS, JS e assets opcionais
- relatorio.pdf – Relatório de desenvolvimento e funcionalidades
________________________________________
## Ferramentas e Tecnologias Utilizadas

Formulários
- WTForms: Abstração de formulários em classes Python, com validação
- FlaskForm: Classe base do Flask-WTF, que integra Flask e WTForms

Banco de Dados
- SQLAlchemy: ORM para abstração do banco de dados
- SQLite: Banco de dados local (app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mercado.db")

Segurança
- Flask-Bcrypt: Hash de senhas e valores sensíveis
- Flask-Login: Gerenciamento de sessões e autenticação
- login_user – Loga usuário
- logout_user – Desloga usuário
- login_required – Valida acesso a rotas protegidas (ex.: /produtos)

Frontend
- Bootstrap – Framework CSS para estilização rápida
- Estilos diretos – Possível mesclar com Bootstrap conforme necessidade
________________________________________

