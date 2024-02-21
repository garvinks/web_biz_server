CREATE TABLE IF NOT EXISTS t_user
(
    id         INTEGER not null
        constraint t_user_pk
            primary key autoincrement,
    name       varchar(32),
    remark     varchar(64),
    created_at bigint unsigned,
    updated_at bigint unsigned
);