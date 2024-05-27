CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE Chats (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    chat TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES Users(id),
    chat_id INTEGER REFERENCES Chats(id),
    comment TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);