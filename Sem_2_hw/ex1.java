// Урок 2. Почему вы не можете не использовать API

// 1 . Дана строка sql-запроса "select * from students where ". 
// Сформируйте часть WHERE этого запроса, используя StringBuilder. 
// Данные для фильтрации приведены ниже в виде json строки.

// Параметры для фильтрации: {"name":"Ivanov", "country":"Russia", "city":"Moscow", "age":"null"}



package Sem_2_hw;

public class ex1 {

    public static void main(String[] args) {
        StringBuilder sql = new StringBuilder("SELECT * FROM STUDENTS WHERE ");
        StringBuilder builde = new StringBuilder();
        builde.append("{\"name\":\"Ivanov\", \"country\":\"Russia\", \"city\":\"Moscow\", \"age\":\"null\"}");
        builde.deleteCharAt(0).deleteCharAt(builde.length()-1);
        System.out.println(builde.toString());
        for (int i = 0; i < builde.length(); i++) {
            switch (builde.charAt(i)){
                case ',':
                    builde.replace(i, i+1, " and"); 
                    break;
                case ':':
                    builde.setCharAt(i, '=');
                    break;
                }
        }
        sql.append(builde);
        System.out.println(sql.toString());
        }
    }