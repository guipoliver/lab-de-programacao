public class Exerciciodois {
    public static void main(String[] args) {
        Integer A = 30;
        Integer B = 30;

        if (A.compareTo(B) != 0 ) {
            System.out.println("não são iguais");
        } else {
            System.out.println("eles são iguais");
        }

        if (A.compareTo(B) == 1) {
            System.out.println("A é maior que B");
        } else if(A.compareTo(B) == -1){
            System.out.println("B é maior que A");
        }
    }
}