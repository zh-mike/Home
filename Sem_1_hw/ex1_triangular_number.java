// 1 Вычислить n-ое треугольного число(сумма чисел от 1 до n), n! (произведение чисел от 1 до n)

package Sem_1_hw;

import java.util.Scanner;

public class ex1_triangular_number {

    public static int factorial(int n) {
        if (n == 0){
            return 1;
        }
        return n * factorial(n-1);
        
    }
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("=>");
        int num = scan.nextInt();
        System.out.println("n-ое треугольного число: " + (num*(num+1))/2);
        System.out.println("Факториал = " + factorial(num));
        scan.close();
        
    }
}
