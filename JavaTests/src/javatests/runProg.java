package javatests;

import java.sql.*;

public class runProg {
    public static void inheritance(){
        Parent p1 = new Parent();
        Child c1 = new Child();
        c1.name();
        p1.name();
        p1.sign();
        c1.sign();        
    }
    
    public static void main(String[] args) {
        try {
            // load driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // creating connection
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/db1", "root", "12345");

            if(con.isClosed()){
                System.out.println("Connection closed!");
            }
            else{
                System.out.println("Connection created :)");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }   
}