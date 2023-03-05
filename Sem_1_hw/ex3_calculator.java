// Реализовать простой калькулятор
package Sem_1_hw;

import java.util.Scanner;


public class ex3_calculator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Введите первое чисо: ");
        float num1 =  scan.nextFloat();
        System.out.print("Введите второе чисо: ");
        float num2 =  scan.nextFloat();
        System.out.print("Введите действие (+, -, *, /): ");
        scan.nextLine();
        String act =  scan.nextLine();
        System.out.println(act);
        switch (act) {
            case "+":
                System.out.println(num1+num2);
                break;
            case "-":
                System.out.println(num1-num2);
                break;
            case "*":
                System.out.println(num1*num2);
                break;
            case "/":
                if (num2 == 0) {
                    System.out.println("На 0 делить нельзя!");
                } else {    
                    System.out.println(num1/num2);
                }
                break;
        }
        scan.close();
    }
}
