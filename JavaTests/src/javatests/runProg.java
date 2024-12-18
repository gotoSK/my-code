package javatests;

// import java.io.FileInputStream;
// import java.io.FileOutputStream;
// import java.io.FileWriter;
// import java.io.IOException;
import java.io.*;
import java.sql.*;

public class runProg {
    public static void inheritance() {
        Parent p1 = new Parent();
        Child c1 = new Child();
        c1.name();
        p1.name();
        p1.sign();
        c1.sign();        
    }

    public static void dbcon() {
        try {
            // load driver
            Class.forName("com.mysql.cj.jdbc.Driver");
            
            // creating connection
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/db1", "root", "12345");
    
            if(con.isClosed()) {
                System.out.println("Connection closed!");
            }
            else {
                System.out.println("Connection created :)");
    
                // create table
                String q = "create table table1(tID int(20) primary key auto_increment, tName varchar(200) not null, tCity varchar(400))";
                // create statement
                Statement stmt = con.createStatement();
                stmt.executeUpdate(q);
                System.err.println("Table Created in database.");
                con.close();
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void fileByte() {
        try {
            FileInputStream in = new FileInputStream("input.txt");
            FileOutputStream out = new FileOutputStream("output.txt");
            int data;
            while ((data = in.read()) != -1) {
                out.write(data);
                System.out.println(data);
            }
            in.close();
            out.close();
        }
        catch (IOException e){
            System.out.println(e);
        }
    }
    
    public static void fileCharCopyFile(){
        try {
            FileReader in = new FileReader("input.txt");
            FileWriter out = new FileWriter("output.txt");
            int data;
            while ((data = in.read()) != -1) {
                out.write(data);
                System.out.println(data);
            }
            in.close();
            out.close();
        }
        catch (IOException e) {
            System.out.println(e);
        }
    }

    public static void fileCharReadWrite(){
        
    }

    public static void main(String[] args) {
        // inheritance();
        // dbcon();
        // fileByte();
        // fileCharCopyFile();

    }   
}