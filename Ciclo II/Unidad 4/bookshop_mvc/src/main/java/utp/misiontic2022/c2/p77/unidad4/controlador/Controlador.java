package utp.misiontic2022.c2.p77.unidad4.controlador;

import utp.misiontic2022.c2.p77.unidad4.modelo.vo.Book;
import utp.misiontic2022.c2.p77.unidad4.modelo.dao.BookDao;

import utp.misiontic2022.c2.p77.unidad4.modelo.vo.Stock;
import utp.misiontic2022.c2.p77.unidad4.modelo.dao.StockDao;

import java.sql.SQLException;

public class Controlador {
    private final BookDao bookDao;
    private final StockDao stockDao;

    public Controlador() {
        this.bookDao = new BookDao();
        this.stockDao = new StockDao();
    }

    public Book createBook(String title, String isbn, int year) throws SQLException {
        Book book = null;
        int band = 0;

        try {
            band = bookDao.validarISBN(isbn);
        } catch (Exception e) {
            System.err.println(e);
        }
        
        if (band == -1) {
            book = new Book();

            book.setTitle(title);
            book.setIsbn(isbn);
            book.setYear(year);

            try {
                book = bookDao.save(book);
            } catch (Exception e) {
                System.err.println(e);
            } 
        }
        return book;
    }

    public Book readBook(String isbn) throws SQLException {
        Book book = bookDao.read(isbn);
        return book;
    }

    public boolean updateBook(String isbn, String title, int year) throws SQLException {
        boolean update;

        Book book = new Book();

        book.setTitle(title);
        book.setIsbn(isbn);
        book.setYear(year);

        update = bookDao.update(book);

        return update;
    }

    public boolean deleteBook(String isbn) throws SQLException {
        boolean delete;

        return delete;
    }

    public void createStock(String isbn, int amount) throws SQLException {
        int id_book = readBook(isbn).getId();
        createStock(id_book, amount);
    }

    public void createStock(int id_book, int amount) throws SQLException {
        Stock stock = new Stock();

        stock.setId_book(id_book);
        stock.setAmount(amount);

        stockDao.save(stock);
    }
}
