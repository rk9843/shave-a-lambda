DROP TABLE IF EXISTS transactions;

CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    UUID NUMERIC NOT NULL UNIQUE,
    sender TEXT,
    recipient TEXT,
    amount REAL NOT NULL,
    note TEXT NOT NULL
);

DROP TABLE IF EXISTS balance;

CREATE TABLE balance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name INT NOT NULL UNIQUE,
    money_raised REAL NOT NULL
);

INSERT INTO balance (team_name, money_raised)
VALUES
   (1, 0.00),
   (2, 0.00),
   (3, 0.00),
   (-1, 0.00);
