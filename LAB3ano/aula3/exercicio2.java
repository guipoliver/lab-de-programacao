import java.util.Scanner;

public class exercicio2 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);

        System.out.println("Digite um ano:");
        int ano = sc.nextInt();

        if (ano % 4 == 0 && ano % 100 != 0) {
            System.out.println("O ano é bissexto!");
        } else {
            System.out.println("O ano não é bissexto!");
        }
    }
}