import java.time.LocalDate;
import java.util.Scanner;

public class exe1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite seu ano de nascimento: ");
        int nasc = sc.nextInt();

        LocalDate hoje = LocalDate.now();
        int ano = hoje.getYear();
        
        int idade;
        idade = ano - nasc;

        System.out.printf("sua idade é: %s", idade);
    }
}