import java.util.Scanner;

public class Method02{
    public static int abs(int x){
        if (x > 0){
            return 1;
        }
        else{
            return 0;
        }
    }

    public static void main(String[] agrs) {
        Scanner sc = new Scanner(System.in);
        System.out.print("정수 한 개를 입력하세요: ");
        int num = sc.nextInt();
        if (num == 0){
            System.out.println("음수도 양수도 아닙니다.");
        }
        else{
            if (abs(num) == 1){
                System.out.print("양수입니다.");
            }
            else{
                System.out.print("음수입니다.");
            }
        }
        
    }
}