public class Exercicioum {
    public static void main(String[] args) {
        String num = "10";
        int numero = Integer.parseInt(num);

        if (numero % 2 == 0) {
            System.out.println(num + " é par");
        } else {
            System.out.println(num + " é impar");
        }
    }
}