import java.util.Scanner;

public class exercicio5 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);
        int num = 1;
        int joao = 0;
        while (num != 0) {
            System.out.println("Digite um numero:");
            num = sc.nextInt();
            joao = num + joao;
            if (num == 0) {
                System.out.printf("A soma dos valores digitados foi: %s", joao);
            }
        }
    }
}