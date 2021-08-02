create table books (
	id integer not null primary key,
	title varchar(60) not null,
	isbn varchar(60) not null unique,
	year numeric(4) not null
);

create table stock (
	id_book integer not null primary key,
	amount integer not null,
	foreign key (id_book) references books (id)
);

create table sales (
	sale_date date not null,
	id_book intenger not null,
	amount integer not null,
	primary  key (sale_date, id_book),
	foreign key (id_book) references books (id)
);

-- Obtener libro por isbn
select * from books where isbn = 'sdfsdf';

-- Obtener lista de libros
SELECT * FROM books;

-- Obtener la cantidad de un libro en stock por su id
SELECT amount FROM stock WHERE id_book = 1;

-- Realizar venta
INSERT INTO sales (sale_date,id_book,amount) VALUES (datetime('now'),1,2);

-- Actualizar el stock
UPDATE stock SET amount = 8 WHERE id_book = 1;
