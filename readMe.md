
python manage.py makemigrations

python manage.py migrate
# SmartFamily

python manage.py runserver

http://127.0.0.1:8000/api/home/login/


ctrl + F5 to update styles


http://127.0.0.1:8000/admin/login/?next=/admin/

Admin Account
admin_user
Password123!




sqlite3 db.sqlite3

sqlite3 is the command to start the SQLite shell.
db.sqlite3 is the name of the database file (replace it if your file name is different).



Step 4: Run SQL queries
Now that you’re in the SQLite shell, you can run SQL queries. For example:

Check all tables:

.tables
Show the schema of a specific table:

.schema table_name
Select all records from a table:


SELECT * FROM table_name;
Run any custom SQL query: For example:

SELECT * FROM auth_user;
List column names in a table:

PRAGMA table_info(table_name);
Exit the SQLite shell:

sql
Copy code
.exit



go to right directoy 
cd SmartFamily

to start server
http://127.0.0.1:8000/


python manage.py createsuperuser




to grab the new code new code from git repo

git pull

to add the new code to the git repo type

git add .

git commit -m 'new code'

git push 