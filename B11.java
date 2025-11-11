import java.util.*;

class B11 {
    static {
        System.loadLibrary("B11"); // Load the native library (B11.dll or libB11.so)
    }

    // Native method declarations
    private native void add1(int a, int b);
    private native void sub1(int a, int b);
    private native void mult1(int a, int b);
    private native void div1(int a, int b);

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        B11 obj = new B11();

        System.out.print("\nEnter value of a: ");
        int a = sc.nextInt();

        System.out.print("Enter value of b: ");
        int b = sc.nextInt();

        int ch;
        do {
            System.out.println("\n----- MENU -----");
            System.out.println("1. Addition");
            System.out.println("2. Subtraction");
            System.out.println("3. Multiplication");
            System.out.println("4. Division");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            ch = sc.nextInt();

            switch (ch) {
                case 1:
                    obj.add1(a, b);
                    break;
                case 2:
                    obj.sub1(a, b);
                    break;
                case 3:
                    obj.mult1(a, b);
                    break;
                case 4:
                    obj.div1(a, b);
                    break;
                case 5:
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        } while (ch != 5);
        sc.close();
    }
}
