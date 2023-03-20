# Task Manager

## DESCRIÇÃO

 Task Manager é um aplicativo de gerenciamento de tarefas que podem ser marcadas como concluídas, podem ser deletadas ou até mesmo editadas utilizando Django, Python, PostgreSQL e o framework css Bulma.

## VERSÕES

- Python: 3.10.6.
- Django: 4.1.7.
- psycopg2: 2.9.5.
- Database: PostgreSQL 14.06 AWS.

## COMO CONFIGURAR

1. Clone o projeto em uma pasta.
2. Caso ainda nao tenha pipenv instalado, digite `sudo apt install pipenv` no terminal.
3. Dentro da pasta onde estão todos os arquivos crie um ambiente virtual com Django. Você pode fazer isso com pipenv digitando `pipenv install django` no seu terminal.
4. Ative o ambiente virtual que você acabou de criar digitando `pipenv shell` no terminal.
5. Instale o psycopg2 (necessário para rodar em banco de dados PostgreSQL) com `pip install psycopg2-binary`, você deve receber umas mensagem dizendo que a depencência já está instalada.
6. Em **task-manager/todomanager/settings.py** na variável _DATABASE_ configure as variáveis a seguir com os valores referentes ao nome da sua tabela no seu banco de dados, seu usuário do banco de dados, a repectiva senha do usuário do banco de dados e o host do seu banco.
   - [YOUR_DB_NAME_HERE].
   - [YOUR_USER_HERE].
   - [YOUR_PASSWORD_HERE].
   - [YOUR_HOST_HERE].
7. Em seguida, na mesma pasta que está **task-manager/manager.py**, com o ambiente ativado, digite `python manage.py runserver` em seu terminal.
8. Caso siga esses passos corretamente você deverá receber uma mensagem de sucesso no seu terminal dizendo que o projeto já está rodando em http://localhost:8000 ou http://127.0.0.1:8000.
9. Para fechar, vá até o terminal e aperte Ctrl+C.
