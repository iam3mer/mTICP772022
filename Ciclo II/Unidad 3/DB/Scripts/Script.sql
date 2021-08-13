SELECT COUNT() as sale FROM sales s JOIN books b WHERE s.id_book = b.id AND b.isbn = 'dfgd8f7dfgd';

SELECT title, isbn, year, amount FROM books b JOIN stock s WHERE b.id = s.id_book AND amount > 0;

SELECT amount FROM stock s WHERE id_book = 2; 

---
SELECT * FROM sales s WHERE id_book = 2;

SELECT title, isbn, (SELECT SUM(amount) FROM sales s WHERE id_book = id) as total FROM books b;














