-- auto-generated definition
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

-- auto-generated definition
create table IF NOT EXISTS t_lottery_claim
(
    id         integer         not null
        constraint t_lottery_claim_pk
            primary key autoincrement,
    order_id   bigint unsigned not null,
    ip_address varchar(16)     not null,
    country    varchar(64)     not null,
    province   varchar(64)     not null,
    city       varchar(64)     not null,
    net        varchar(64)     not null,
    created_at bigint unsigned not null
);

create unique index IF NOT EXISTS t_lottery_claim_order_id_uindex
    on t_lottery_claim (order_id);

-- auto-generated definition
create table IF NOT EXISTS t_lottery_order
(
    id          INTEGER          not null
        constraint t_lottery_order_pk
            primary key autoincrement,
    trace_id    bigint unsigned  not null,
    prize_id    integer unsigned not null,
    order_code  varchar(64)      not null,
    status      tinyint unsigned not null,
    prize_level tinyint unsigned not null,
    created_at  bigint unsigned  not null,
    updated_at  bigint unsigned  not null
);

create index IF NOT EXISTS t_lottery_order_prize_id_index
    on t_lottery_order (prize_id);

create index IF NOT EXISTS t_lottery_order_prize_level_index
    on t_lottery_order (prize_level);

create index IF NOT EXISTS t_lottery_order_status_index
    on t_lottery_order (status);

create unique index IF NOT EXISTS t_lottery_order_trace_id_uindex
    on t_lottery_order (trace_id);

-- auto-generated definition
create table IF NOT EXISTS t_lottery_prize
(
    id         integer         not null
        constraint t_lottery_prize_pk
            primary key autoincrement,
    order_no   varchar(16)     not null,
    prize_code varchar(64)     not null,
    prize_pool bigint          not null,
    created_at bigint unsigned not null,
    expired_at bigint unsigned not null
);

alter table t_lottery_prize
    add order_date varchar(16) not null;

