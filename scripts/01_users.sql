CREATE ROLE project_admin 
SUPERUSER 
LOGIN 
PASSWORD 'root';
SELECT 'CREATE DATABASE rasa WITH OWNER project_admin'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'rasa')\gexec
