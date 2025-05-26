class Swapper {
    void swapArr(int[] ab) {
        int temp = ab[0];
        ab[0] = ab[1];
        ab[1] = temp;
    }

    void swapVal(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
        System.out.println("swapVal() 내부: a = " + a + ", b = " + b);
    }
}

public class Test {
    public static void main(String[] args) {
        Swapper s = new Swapper();

        int[] ab = {33, 55};
        int a = 33;
        int b = 55;

        System.out.println("=== 배열 swap ===");
        System.out.println("전: " + ab[0] + ", " + ab[1]);
        s.swapArr(ab);
        System.out.println("후: " + ab[0] + ", " + ab[1]);

        System.out.println("\n=== 변수 swap ===");
        System.out.println("전: a = " + a + ", b = " + b);
        s.swapVal(a, b);
        System.out.println("후: a = " + a + ", b = " + b);
    }
}
