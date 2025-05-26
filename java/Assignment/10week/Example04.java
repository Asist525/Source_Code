import java.util.Scanner;

public class Example04 {
    public static void add(double x, double y) {
        System.out.printf("%.1f + %.1f = %.1f\n", x, y, x + y);
    }

    public static void subtract(double x, double y) {
        System.out.printf("%.1f - %.1f = %.1f\n", x, y, x - y);
    }

    public static void multiply(double x, double y) {
        System.out.printf("%.1f * %.1f = %.1f\n", x, y, x * y);
    }

    public static void divide(double x, double y) {
        System.out.println(x + " / " + y + " = " + x/y);
    }

    public static void modulo(double x, double y) {
        System.out.printf("%.1f %% %.1f = %.1f\n", x, y, x % y); 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("실수 두 개를 입력하세요: ");
        double a = sc.nextDouble();  
        double b = sc.nextDouble();
        add(a, b);
        subtract(a, b);
        multiply(a, b);
        divide(a, b);
        modulo(a, b);
    }
}
