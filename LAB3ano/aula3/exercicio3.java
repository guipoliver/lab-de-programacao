import java.util.Scanner;

public class exercicio3 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);

        System.out.println("Digite um primeiro valor:");
        int A = sc.nextInt();
        System.out.println("Digite um segundo valor:");
        int B = sc.nextInt();
        System.out.println("Digite um terceiro valor:");
        int C = sc.nextInt();

        if (A > B && A > C) {
            System.out.println("A é o maior entre eles");
        } else if (B > A && B > C) {
            System.out.println("B é o maior entre eles");
        } else {
            System.out.println("C é o maior entre eles");
        }
    }
}