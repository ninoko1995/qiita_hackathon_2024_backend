CREATE TABLE IF NOT EXISTS spaces(
    id serial PRIMARY KEY,
    room_id text,
    maximum int,
    created_at datetime,
    updated_at datetime
);

CREATE TABLE IF NOT EXISTS space_users(
    id serial PRIMARY KEY,
    space_id bigint UNSIGNED,
    user_id bigint UNSIGNED,
    position int,
    status text,
    created_at datetime,

    FOREIGN KEY fk_space_users_to_space(space_id) REFERENCES spaces(id),
    FOREIGN KEY fk_space_users_to_user(user_id) REFERENCES users(id)
);
