package javatests;

class Parent{
    public void sign(){
        System.out.println("parent.");
    }
    public void name(){
        System.out.println("Parent");
    }
}

class Child extends Parent{
    public void name(){
        System.out.println("Child");
    }
}

public class runProg {
    
    public static void main(String[] args) {
        Parent p1 = new Parent();
        Child c1 = new Child();
        c1.name();
        p1.name();
        p1.sign();
        c1.sign();
    }   
}