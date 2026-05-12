package java;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class EMS {
    public static void main(String[] args){
        System.out.println("Employee Management System");
        List<Employee> empListtt = new LinkedList<>();
        populate(empListtt);
        displayAllEmployees(empListtt);
    }

    private static void displayAllEmployees(List<Employee> empListtt){
        for (Employee emp: empListtt){
            System.out.println(emp);
        }
    }

    private static void populate(List<Employee> empListtt){
        Department d1 = new Department(1, "HR");

        Employee e1 = new Employee(101, "eric", 900000, d1)

        empListtt.add(e1);
    }
}

class Employee extends Object{
    private int id;
    private String name;
    private double salary;
    private Department dept;

    // Constructor
    public Employee(int id, String name, double salary, Department dept){
        this.id = id;
        this.name = name;
        this.salary = salary;
        this.dept = dept;
    }

    // Setters and Getters

    public int getId() {
        return id;
    }
    public void setId(int id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public double getSalary() {
        return salary;
    }
    public void setSalary(double salary) {
        this.salary = salary;
    }
    public Department getDept() {
        return dept;
    }
    public void setDept(Department dept) {
        this.dept = dept;
    }
}

class Department{
    private int id;
    private String deptName;

    // Constructor
    public Department(int id, String dept){
        this.id = id;
        this.deptName = dept;
    }

    // Setters and Getters

    public int getID(){
        return id;
    }

    public String getDeptName(){
        return deptName;
    }

    public void setID(int id){
        this.id = id;
    }

    public void setDeptName(String dept){
        this.deptName = dept;
    }
}
