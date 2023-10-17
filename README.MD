# API REST - Autenticação por Token

Aplicação Python - Flask de API REST

Dentro da pasta classes/db , temos o arquivo 'criarDB.py' que ira criar um banco de dados na pasta raiz dataBase, utilizando a biblioteca sqlite3.
Este banco de dados conta com uma tabela usuarios, e um registro 'admin' com a senha criptografada.
Esta pasta 'classes/db' também contem o arquivo conexao.py, utilizado para realizar qualquer conexão na base de dados.

O diretorio BluePrint, contém as rotas da aplicação, que neste caso são dois caminhos principais:
    Rotas de Autenticação.
    Rotas para utilização da Aplicação.

Ou seja, já tem uma base organizada para continuação do projeto para qualquer aplicação, necessitando apenas continuar a partir deste ponto pois toda a Autenticação já esta pronta. E as outras rotas pre-organizadas, para manter a qualidade da  organização da aplicação.

Por fim, no diretorio classes tenho outros arquivos do sistema como:
Criptografia, Gerenciamento dos Token, e Verificação de Login na base de dados.

Por tanto, creio que este projeto esta razoavelmente organizado para a execução de qualquer fim, sendo esta uma API REST.

# Arquivo .env

É necessario criar o arquivo .env na raiz do projeto com as seguintes variaveis
<code>
CHAVE='senha-da-app-para-o-TOKEN'
ALGORITIMO='HS256'
nomeApp='Estudio de Tatuagem'
</code>
