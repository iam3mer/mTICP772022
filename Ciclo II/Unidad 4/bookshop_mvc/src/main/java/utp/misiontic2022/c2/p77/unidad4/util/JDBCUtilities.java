package utp.misiontic2022.c2.p77.unidad4.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class JDBCUtilities {

    private static final String DATABASE_LOCATION = "BookShop.db";
    
    public static Connection getConnection() throws SQLException {
        String url = "jdbc:sqlite:" + DATABASE_LOCATION;

        return DriverManager.getConnection(url);
    }
    
}
