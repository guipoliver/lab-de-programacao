import java.time.LocalDate;
import java.util.Scanner;
public class exe4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Digite a data do seu aniversario para saber quantos dias faltam(use o modelo (ano-mes-dia)): ");
        String aniversario = sc.nextLine();
        LocalDate hoje = LocalDate.now();
        int dias = hoje.getDayOfYear();
        LocalDate aniversarioParse = LocalDate.parse(aniversario);
        int aniversarioDias = aniversarioParse.getDayOfYear();
        int restante;
        Boolean bissexto = (aniversarioParse.isLeapYear());
        if (bissexto = true) 
            aniversarioDias = aniversarioDias - 1;       
        if (aniversarioDias > dias) 
            restante = aniversarioDias - dias;
        else 
            restante = (365 - dias) + aniversarioDias;        
        System.out.println(restante);
    }
}