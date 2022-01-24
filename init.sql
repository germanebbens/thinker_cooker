--table for the clean recipess
CREATE TABLE IF NOT EXISTS recetas(
    id_receta INT PRIMARY KEY,
    titulo VARCHAR(80) NOT NULL,
    nro_receta INT NOT NULL,
    url_ VARCHAR(80) NOT NULL,
    pasos VARCHAR(300),
    ingredientes VARCHAR(300) NOT NULL,
    autor VARCHAR(30),
    dificultad VARCHAR(10),
    tiempo INT,
    created TIMESTAMP NOT NULL
);

--table for clean ingredients
CREATE TABLE IF NOT EXISTS ingredientes(
    id_ingrediente INT PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL,
    unidad_de_medida VARCHAR(80)
);

--table for raw recipes, before downloaded
CREATE TABLE IF NOT EXISTS recetas_raw(
    index_ INT PRIMARY KEY,
    recipe_id INT NOT NULL,
    url_ VARCHAR(120) NOT NULL,
    title VARCHAR(300) NOT NULL,
    ingredients VARCHAR,
    steps VARCHAR,
    duration TIMESTAMP,
    difficulty VARCHAR(10),
    donwloaded_time TIMESTAMP NOT NULL
);

