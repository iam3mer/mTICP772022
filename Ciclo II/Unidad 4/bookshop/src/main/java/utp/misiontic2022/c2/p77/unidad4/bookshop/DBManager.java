package utp.misiontic2022.c2.p77.unidad4.bookshop;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class DBManager implements AutoCloseable {
    private Connection connection;

    public DBManager() throws SQLException {
        connect();
    }

    private void connect() throws SQLException {
        String url = "jdbc:sqlite:BookShop.db";
        connection = DriverManager.getConnection(url);
    }

    /**
     * Close the connection to the database if it is still open.
     *
     */
    public void close() throws SQLException {
        if (connection != null) {
            connection.close();
        }
        connection = null;
    }

     /**
     * Return the number of units in stock of the given book.
     *
     * @param book The book object.
     * @return The number of units in stock, or 0 if the book does not
     *         exist in the database.
     * @throws SQLException If somthing fails with the DB.
     */
    public int getStock(Book book) throws SQLException {
        return getStock(book.getId());
    }

    /**
     * Return the number of units in stock of the given book.
     *
     * @param bookId The book identifier in the database.
     * @return The number of units in stock, or 0 if the book does not
     *         exist in the database.
     */
    public int getStock(int bookId) throws SQLException {

        int amount = 0;

        String sql = "SELECT amount FROM stock WHERE id_book = "+bookId+";";
        
        try (
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            if (rs.next()) {
                amount = rs.getInt("amount");
            }
        }

        return amount;
    }

    /**
     * Search book by ISBN.
     *
     * @param isbn The ISBN of the book.
     * @return The Book object, or null if not found.
     * @throws SQLException If somthing fails with the DB.
     */
    public Book searchBook(String isbn) throws SQLException {
        Book book = null;
        String sql = "select * from books where isbn = '"+ isbn +"';";

        try (
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {

            if (rs.next()) {
                book = new Book();

                book.setId(rs.getInt("id"));
                book.setTitle(rs.getString("title"));
                book.setIsbn(rs.getString("isbn"));
                book.setYear(rs.getInt("year"));
            }
            
        } catch (Exception e) {
            System.out.println(e);
        }

        return book;
    }

    /**
     * Sell a book.
     *
     * @param book The book.
     * @param units Number of units that are being sold.
     * @return True if the operation succeeds, or false otherwise
     *         (e.g. when the stock of the book is not big enough).
     * @throws SQLException If somthing fails with the DB.
     */
    public boolean sellBook(Book book, int units) throws SQLException {
        return sellBook(book.getId(), units);
    }

    /**
     * Sell a book.
     *
     * @param book The book's identifier.
     * @param units Number of units that are being sold.
     * @return True if the operation succeeds, or false otherwise
     *         (e.g. when the stock of the book is not big enough).
     * @throws SQLException If something fails with the DB.
     */
    public boolean sellBook(int book, int units) throws SQLException {

        int amount = getStock(book);
        int amountUD;

        // Comprobar el suficiente stock
        if (amount >= units) {
            // Insertar la venta
            try (
                Statement stmt = connection.createStatement();
            ) {
                String ins = "INSERT INTO sales (sale_date,id_book,amount) VALUES (datetime('now'),"+book+","+units+");";
                stmt.executeUpdate(ins);

                amountUD = amount - units;
                String ud = "UPDATE stock SET amount = "+amountUD+" WHERE id_book = "+book+";";
                stmt.executeUpdate(ud);
            }
            return true;
        }
        return false;
    }

    /**
     * Return a list with all the books in the database.
     *
     * @return List with all the books.
     * @throws SQLException If something fails with the DB.
     */
    public List<Book> listBooks() throws SQLException {
        List<Book> books = new ArrayList<>();

        String sql = "SELECT * FROM books;";

        try (
            Statement stmt = connection.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        ) {
            while (rs.next()) {
                Book book = new Book();

                book.setId(rs.getInt("id"));
                book.setIsbn(rs.getString("isbn"));
                book.setTitle(rs.getString("title"));
                book.setYear(rs.getInt("year"));

                books.add(book);
            }
        }

        return books;
    }
}
