CREATE ROLE project_admin
SUPERUSER
LOGIN
PASSWORD 'root';
SELECT 'CREATE DATABASE rasa WITH OWNER project_admin'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'rasa')\gexec
CREATE TABLE IF NOT EXISTS public.users(
    email varchar(255) PRIMARY KEY,
    name varchar(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    app_Names text[][]
);
