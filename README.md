# CNAB-sprint2-anacarla

**Dados CNAB**

Consiste em parsear dados CNAB e salvar suas informações no banco de dados.
<br>

**Instalação**

Foi necessário a utilização do framework Django escrito em Python.
<br>
<br>
<ol>
<li> Clone do repositório</li>
<li> Iniciar e ativar do ambiente virtual(venv)
<p>bash</p>
<p> python -m venv venv  </p>
<p> source venv/bin/activate  </p>
</li>
<li>Gerar as tabelas do banco de dados </li>
<p>bash</p>
<p> python manage.py makemigrations  </p>
<p> python manage.py migrate  </p>
<li> Instalar as dependências </li>
<p>bash</p>
<p> pip install -r requirements.txt </p>
</ol>
<br>

**Uso**

Arquivo desejado precisa estar salvo na sua maquina, e após o upload, seus dados ficarão salvos no banco de dados (sqite3) em que será exibido de acordo com o que foi passado na sua construção.
<br>
A tabela que referencia o tipo de cada transação será exibida em outra página definida na URL e será acessada usando /tabela_dados
<br>
**Observação**

Esse projeto foi criado com base em um arquivo CNAB(https://github.com/Kenzie-Academy-Brasil-Developers/desafio-backend-m6/blob/main/CNAB.txt) caso sejá passado um outro arquivo, o projeto não funcionará de forma desejada. Foi utilizado o Django seguindo a documentação de File Upload. 


