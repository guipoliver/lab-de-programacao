import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {
        String[] nomes = new String[5];
        int[] idades = new int[5];
        Scanner sc =  new Scanner(System.in);
        int posição = 0;
        int encerrar = 0;
        String nome;
        int idade;

        while(encerrar == 0) {
            System.out.println("1 - Cadastrar aluno \n 2 - Listar alunos \n 3 - Buscar aluno por nome \n 4 - Calcular média de idade \n 5 - Exibir data/hora atual \n 6 - Sair");
            System.out.print("Digite a opcao que quer");
            int opcao = sc.nextInt();
            sc.nextLine();

            if(opcao == 1) {
                System.out.println("Digite seu nome:");
                nome = sc.nextLine();
                nomes[posição] = nome;
                System.out.println("Digite sua idade:");
                idade = sc.nextInt();
                idades[posição] = idade;
                posição++;
            } else if(opcao == 2) {
                for(int i = 0; i < nomes.length; i++) {
                    if(nomes[i] == null) {
                        return;
                    }
                    System.out.println(nomes[i]);
                    System.out.println(idades[i]);
                }
            } else if(opcao == 3) {
                System.out.println("Voce escolheu 3");
            } else if(opcao == 4) {
                System.out.println("Voce escolheu 4");
            } else if(opcao == 5) {
                System.out.println("Voce escolheu 5");
            } else if(opcao == 6) {
                System.out.println("Tchau!");
                encerrar += 1;
            }
        }
    }
}
