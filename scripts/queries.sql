CREATE TABLE IF NOT EXISTS public.users(
    email varchar(255) PRIMARY KEY,
    name varchar(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    app_Names text[][]
);
