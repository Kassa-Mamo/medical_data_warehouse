-- database/schema.sql
CREATE TABLE IF NOT EXISTS medical_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    channel TEXT,
    text TEXT,
    date DATETIME
);
