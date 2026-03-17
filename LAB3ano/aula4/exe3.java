import java.util.Scanner;
import java.time.LocalDate;

public class exe3 {
    public static void main(String[] args) {
        LocalDate hoje = LocalDate.now();
        int dias = hoje.getDayOfYear();

        Boolean bissexto = (hoje.isLeapYear());

        int resultado;

        if (bissexto = false) {
            resultado = 365 - dias;
        } else {
            resultado = 366 - dias;
        }

        System.out.println(resultado);
    }
}
