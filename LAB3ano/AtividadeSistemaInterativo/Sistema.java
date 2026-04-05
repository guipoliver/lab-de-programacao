import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Scanner;
public class Sistema {
    public static void main(String[] args) {
        String[] nomes = new String[5];
        Integer[] idades = new Integer[5]; 
        //Integer é um Wrapper diferentemente do int,
        //No int o valor padrão é 0 e guarda valores primitivos 
        //Enquanto no Integer o valor padrão é null e guarda objetos
        Scanner sc =  new Scanner(System.in);
        int posicao = 0;
        int encerrar = 0;
        String nome;
        int idade;
        String busca;
        double media = 0;
        int idadeTemp = 0;
        int tam = 0;
        boolean encontrado = false;

        //A diferença entre While e Do-While 
        //É que o Do-While verifica o bloco antes da condição 
        //Portanto mesmo que a condição seja falsa ele vai executar o bloco ao menos uma vez
        do {
            System.out.println("1 - Cadastrar aluno \n2 - Listar alunos \n3 - Buscar aluno por nome \n4 - Calcular media de idade \n5 - Exibir data/hora atual \n6 - Sair");
            System.out.print("Digite a opcao que quer:");
            int opcao = sc.nextInt();
            sc.nextLine();

            if(opcao == 1) {
                System.out.println("Digite seu nome:");
                nome = sc.nextLine();
                nomes[posicao] = nome;
                System.out.println("Digite sua idade:");
                idade = sc.nextInt();
                idades[posicao] = idade;
                posicao++;
            } else if(opcao == 2) {
                for(int i = 0; i < nomes.length; i++) {
                    if(nomes[i] == null) {
                        break;
                    }
                    System.out.println(nomes[i]);
                    System.out.println(idades[i]);
                }
            } else if(opcao == 3) {
                System.out.println("Digite o nome do aluno que deseja buscar:");
                busca = sc.nextLine();
                for(int i = 0; i < nomes.length; i++) {
                    if(nomes[i] != null && nomes[i].equals(busca)) {
                        System.out.println("Nome: " + nomes[i] + ", Idade: " + idades[i]);
                        encontrado = true;
                        break;
                    }
                }
                if(!encontrado){
                    System.out.println("nenhum aluno foi encontrado");
                }
            } else if (opcao == 4) {
                idadeTemp = 0;
                tam = 0;
                for(int i = 0; i < idades.length; i++) {
                    if(nomes[i] != null) {
                        idadeTemp += idades[i];
                        tam++;
                    }
                }
                media = (idadeTemp / tam);
                System.out.println(media);
            } else if(opcao == 5) {
                LocalDate hoje = LocalDate.now();
                System.out.printf("hoje e: %s\n", hoje);
                LocalTime hora = LocalTime.now();
                System.out.printf("agora sao: %s\n", hora);
            } else if(opcao == 6) {
                System.out.println("Tchau!");
                encerrar += 1;
            }
        } while(encerrar == 0);
    }
}