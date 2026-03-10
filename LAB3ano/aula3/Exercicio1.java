import java.util.Scanner;
public class Exercicio1 {
    public static void main(String[] args) {
       Scanner sc =  new Scanner(System.in);

       System.out.print("Digite sua nota de 0 a 10: ");
       int nota = sc.nextInt();

       if (nota >10 || nota <0) {
        System.out.println("Digite um valor entre 0 e 10!");
       } else if (nota < 6){
        System.out.println("Reprovado!");
       } else {
        System.out.println("Aprovado!");
       }
    }
}