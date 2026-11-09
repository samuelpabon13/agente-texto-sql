CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10,2) NOT NULL
);

CREATE TABLE ventas (
    id SERIAL PRIMARY KEY,
    producto_id INT REFERENCES productos(id),
    cantidad INT NOT NULL,
    fecha DATE NOT NULL
);

INSERT INTO productos (nombre, precio) VALUES
    ('Portátil', 2500000),
    ('Mouse', 45000),
    ('Teclado', 120000);

INSERT INTO ventas (producto_id, cantidad, fecha) VALUES
    (1, 2, '2026-03-05'),
    (2, 10, '2026-03-12'),
    (3, 4, '2026-04-01');