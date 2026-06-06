import java.util.Scanner;

// Classe = molde
// Objeto = algo criado com a classe

class Pessoa {

    private String nome;
    private int idade;

    public Pessoa() {
        nome = "";
        idade = 0;
    }

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void exibirDados() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade);
    }
}

// extends serve para herdar atributos e métodos
// vantagem: reaproveitar código

class Aluno extends Pessoa {

    private String matricula;
    private double nota;

    public Aluno() {
        matricula = "";
        nota = 0;
    }

    // super chama o construtor da classe pai
    public Aluno(String nome, int idade,
                 String matricula, double nota) {

        super(nome, idade);

        this.matricula = matricula;
        this.nota = nota;
    }

    public String getMatricula() {
        return matricula;
    }

    public double getNota() {
        return nota;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    public void setNota(double nota) {
        this.nota = nota;
    }

    public void verificarAprovacao() {

        if (nota >= 6) {
            System.out.println("Aluno aprovado");
        } else {
            System.out.println("Aluno reprovado");
        }
    }
}

class Professor extends Pessoa {

    private String disciplina;
    private double salario;

    public Professor() {
        super();
        disciplina = "";
        salario = 0;
    }

    public Professor(String nome,
                     int idade,
                     String disciplina,
                     double salario) {

        super(nome, idade);

        this.disciplina = disciplina;
        this.salario = salario;
    }

    public String getDisciplina() {
        return disciplina;
    }

    public double getSalario() {
        return salario;
    }

    public void setDisciplina(String disciplina) {
        this.disciplina = disciplina;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public void calcularSalarioAnual() {
        System.out.println(
            "Salario anual: " + (salario * 13)
        );
    }
}

public class sistemaEscolaControl {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Aluno[] alunos = new Aluno[5];
        Professor[] professores = new Professor[5];

        int totalAlunos = 0;
        int totalProfessores = 0;

        int opcao = 0;

        while (opcao != 8) {

            System.out.println("\n1 - Cadastrar aluno");
            System.out.println("2 - Cadastrar professor");
            System.out.println("3 - Listar alunos");
            System.out.println("4 - Listar professores");
            System.out.println("5 - Buscar aluno");
            System.out.println("6 - Buscar professor");
            System.out.println("7 - Exibir dados completos");
            System.out.println("8 - Sair");

            opcao = sc.nextInt();
            sc.nextLine();

            if (opcao == 1) {

                if (totalAlunos < 5) {

                    System.out.print("Nome: ");
                    String nome = sc.nextLine();

                    System.out.print("Idade: ");
                    int idade = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Matricula: ");
                    String matricula = sc.nextLine();

                    System.out.print("Nota: ");
                    double nota = sc.nextDouble();
                    sc.nextLine();

                    alunos[totalAlunos] =
                        new Aluno(nome,
                                  idade,
                                  matricula,
                                  nota);

                    totalAlunos++;

                    System.out.println("Aluno cadastrado");
                }

            }

            else if (opcao == 2) {

                if (totalProfessores < 5) {

                    System.out.print("Nome: ");
                    String nome = sc.nextLine();

                    System.out.print("Idade: ");
                    int idade = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Disciplina: ");
                    String disciplina = sc.nextLine();

                    System.out.print("Salario: ");
                    double salario = sc.nextDouble();
                    sc.nextLine();

                    professores[totalProfessores] =
                        new Professor(
                            nome,
                            idade,
                            disciplina,
                            salario
                        );

                    totalProfessores++;

                    System.out.println(
                        "Professor cadastrado"
                    );
                }

            }

            else if (opcao == 3) {

                for (int i = 0; i < totalAlunos; i++) {

                    alunos[i].exibirDados();

                    System.out.println(
                        "Matricula: "
                        + alunos[i].getMatricula()
                    );

                    System.out.println(
                        "Nota: "
                        + alunos[i].getNota()
                    );

                    alunos[i].verificarAprovacao();

                    System.out.println();
                }

            }

            else if (opcao == 4) {

                for (int i = 0; i < totalProfessores; i++) {

                    professores[i].exibirDados();

                    System.out.println(
                        "Disciplina: "
                        + professores[i].getDisciplina()
                    );

                    System.out.println(
                        "Salario: "
                        + professores[i].getSalario()
                    );

                    System.out.println();
                }

            }

            else if (opcao == 5) {

                System.out.print("Nome: ");
                String busca = sc.nextLine();

                boolean achou = false;

                for (int i = 0; i < totalAlunos; i++) {

                    if (alunos[i]
                        .getNome()
                        .equalsIgnoreCase(busca)) {

                        alunos[i].exibirDados();

                        achou = true;
                    }
                }

                if (!achou) {
                    System.out.println(
                        "Aluno não encontrado"
                    );
                }

            }

            else if (opcao == 6) {

                System.out.print("Nome: ");
                String busca = sc.nextLine();

                boolean achou = false;

                for (int i = 0; i < totalProfessores; i++) {

                    if (professores[i]
                        .getNome()
                        .equalsIgnoreCase(busca)) {

                        professores[i].exibirDados();

                        achou = true;
                    }
                }

                if (!achou) {

                    System.out.println(
                        "Professor não encontrado"
                    );
                }

            }

            else if (opcao == 7) {

                System.out.println(
                    "Alunos cadastrados: "
                    + totalAlunos
                );

                System.out.println(
                    "Professores cadastrados: "
                    + totalProfessores
                );
            }

        }

        sc.close();
    }
}