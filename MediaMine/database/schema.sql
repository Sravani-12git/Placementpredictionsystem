-- MediaMine Database Schema (PostgreSQL)

CREATE TABLE IF NOT EXISTS category (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    media_category VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS media (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    media_type VARCHAR(50) NOT NULL, -- NEWS, VIDEO, AUDIO, TRANSCRIPT
    content TEXT,
    transcript TEXT,
    caption TEXT,
    source VARCHAR(255),
    published_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS media_categories (
    media_id BIGINT NOT NULL REFERENCES media(id) ON DELETE CASCADE,
    category_id BIGINT NOT NULL REFERENCES category(id) ON DELETE CASCADE,
    PRIMARY KEY (media_id, category_id)
);

CREATE TABLE IF NOT EXISTS search_query (
    id BIGSERIAL PRIMARY KEY,
    query_text VARCHAR(255) NOT NULL,
    algorithm VARCHAR(100) NOT NULL,
    result_count INT DEFAULT 0,
    searched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS media_event (
    id BIGSERIAL PRIMARY KEY,
    media_id BIGINT REFERENCES media(id) ON DELETE CASCADE,
    event_type VARCHAR(50) NOT NULL, -- VIEW, PLAY, PAUSE, LIKE, SHARE, SEARCH
    event_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
