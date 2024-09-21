CREATE TABLE IF NOT EXISTS sample_table(
    id char(36) NOT NULL PRIMARY KEY,
    content text,
    created_at datetime,
    updated_at datetime
);