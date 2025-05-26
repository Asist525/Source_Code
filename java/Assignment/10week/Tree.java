import java.util.Scanner;

public class Tree{

    public static void tree(int x){
        for (int i=0; i<x; i++){
            System.out.println("   *   ");
            System.out.println("  * *  ");
            System.out.println(" ***** ");
            System.out.println("*  *  *");
            System.out.println("   *   ");
        }
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.print("몇 개의 나무를 찍을까요? ");
        int num = sc.nextInt();
        tree(num);

    }
}