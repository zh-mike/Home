// Вывести все простые числа от 1 до 1000

package Sem_1_hw;

public class ex2_prime_numbers {


    public static void main(String[] args) {

        for (int i = 2; i <= 1000; i++) {
            boolean isPrime = true;

            for (int j = 2; j < i; j++) {
                if (i % j == 0){
                    isPrime = false;
                    break;
                }
            }

            if (isPrime)
                System.out.print(i + " ");

        }
        
    }
    
}

