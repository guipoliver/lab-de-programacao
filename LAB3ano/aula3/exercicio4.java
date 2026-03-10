import java.util.Scanner;

public class exercicio4 {
    public static void main(String[] args) {
        Scanner sc =  new Scanner(System.in);

        System.out.println("Digite uma letra do alfabeto:");
        String letra = sc.nextLine();

        if (letra.equals("a") || letra.equals("e") || letra.equals("i") || letra.equals("o") || letra.equals("u")) {
            System.out.println("A letra é uma vogal!");
        } else {
            System.out.println("Não é vogal!");
        }
    }
}