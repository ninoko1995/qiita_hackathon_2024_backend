CREATE TABLE IF NOT EXISTS users(
    id serial PRIMARY KEY,
    email text,
    password text,
    nickname text,
    interested_in text,
    twitter_screenname text,
    icon text,
    created_at datetime,
    updated_at datetime
);
