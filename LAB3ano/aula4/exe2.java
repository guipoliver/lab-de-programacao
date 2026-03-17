import java.time.LocalDate;
import java.util.Scanner;

public class exe2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite uma data para saber se o ano é bissexto ou não (use o modelo (ano-mes-dia)): ");
        String entrada = sc.nextLine();

        LocalDate ano = LocalDate.parse(entrada);

        System.out.println(ano.isLeapYear());
    }
}
