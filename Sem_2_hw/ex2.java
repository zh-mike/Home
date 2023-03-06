// 2. Реализуйте алгоритм сортировки пузырьком числового массива, 
// результат после каждой итерации запишите в лог-файл.

package Sem_2_hw;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;

public class ex2 {
    public static void main(String[] args) throws IOException {
        
        int[] arr = {5,3,2,4,1};
        boolean isSorted = false;
        int buf;
        while(!isSorted) {
            isSorted = true;
            for (int i = 0; i <arr.length-1; i++) {
                if(arr[i] > arr[i+1]){
                    isSorted = false;
 
                    buf = arr[i];
                    arr[i] = arr[i+1];
                    arr[i+1] = buf;
                }
            }
            writeArrayToFile(arr);
        }
    }
    public static void writeArrayToFile(int[] arr) {
        try {
            FileWriter writer = new FileWriter("log.txt", true);
            writer.write(Arrays.toString(arr) + "\n");
            writer.flush(); 
            writer.close();
        }  catch (IOException e) {
            e.printStackTrace();
        }
}
}
