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
create unique index IF NOT EXISTS t_user_name_uindex
    on t_user (name);
