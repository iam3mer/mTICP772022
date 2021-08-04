package utp.misiontic2022.c2.p77.unidad4.modelo.dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import utp.misiontic2022.c2.p77.unidad4.util.JDBCUtilities;

import utp.misiontic2022.c2.p77.unidad4.modelo.vo.Stock;

public class StockDao {
    
    public void save(Stock stock) throws SQLException {
        String psql = "INSERT INTO stock (id_book,amount) VALUES (?, ?)";

        try (
            Connection conn = JDBCUtilities.getConnection();
            PreparedStatement pstmt = conn.prepareStatement(psql);
        ) {
            pstmt.setInt(1, stock.getId_book());
            pstmt.setInt(2, stock.getAmount());

            pstmt.executeUpdate();
        }
    }
}
