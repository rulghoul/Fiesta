#!/bin/bash
#Crear entorno virtual y descargar las librerias
python3 -m venv virtual
source virtual/bin/activate
pip3 install -r requirements.txt
cd fiestas
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py createsuperuser
python3 mage.py loaddata inicio.json
python3 mage.py loaddata catalogos02.json
cd ..
deactivate

#Crear Usuario y asignar permisos
groupadd --system webapps
useradd --system --gid webapps --home /var/www/python/Fiesta eventos

chown -R eventos:webapps /var/www/python/Fiesta
chmod +x gunicorn_eventos.bash

#Crear Base de datos

# Datos de conexión a la base de datos
DB_HOST="localhost"
DB_USER="root"
DB_PASSWORD=""
echo "Ingrese la contraseña para la conexión a la base de datos:"

#Eventos
EVENTOS_SQL_DATABASE="eventos"
EVENTOS_SQL_USER="eventos"
EVENTOS_SQL_PASSWORD="eventosdjango"

read -s DB_PASSWORD

# Comandos SQL para crear bases de datos y usuarios
SQL1="CREATE DATABASE IF NOT EXISTS $EVENTOS_SQL_DATABASE;"
SQL1+="GRANT ALL PRIVILEGES ON $EVENTOS_SQL_DATABASE.* TO '$EVENTOS_SQL_USER'@'$DB_HOST' IDENTIFIED BY '$EVENTOS_SQL_PASSWORD';"

echo "Bases de datos y usuarios creados correctamente."

mysql -h $DB_HOST -u $DB_USER -p$DB_PASSWORD -e "$SQL1" || exit 1

#Instalar supervisor

cp eventos.conf /etc/supervisor/conf.d/eventos.conf
#Actualizar supervisor
supervisorctl reread
supervisorctl update
supervisorctl status


#Configuracion de Nginx
cp nginx /etc/nginx/sites-available/eventos
#Activar sitio Nginx
ln -s /etc/nginx/sites-available/eventos /etc/nginx/sites-enabled/eventos
service nginx restart


