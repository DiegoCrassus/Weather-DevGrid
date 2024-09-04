CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    lon FLOAT NOT NULL,
    lat FLOAT NOT NULL,
    weather_id INT,
    weather_main VARCHAR(50),
    weather_description VARCHAR(100),
    weather_icon VARCHAR(5),
    temp FLOAT NOT NULL,
    feels_like FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    pressure INT,
    humidity INT,
    sea_level INT,
    grnd_level INT,
    visibility INT,
    wind_speed FLOAT,
    wind_deg INT,
    wind_gust FLOAT,
    clouds_all INT,
    dt INT,
    sys_type INT,
    sys_id INT,
    sys_country VARCHAR(2),
    sys_sunrise INT,
    sys_sunset INT,
    timezone INT,
    city_id INT,
    city_name VARCHAR(100),
    cod INT
);