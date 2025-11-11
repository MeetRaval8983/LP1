import java.util.Scanner;

public class firstfit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int p = sc.nextInt();
        System.out.print("Enter number of blocks: ");
        int b = sc.nextInt();

        int[] process = new int[p];
        int[] block = new int[b];
        boolean[] used = new boolean[b];

        System.out.println("Enter block sizes:");
        for (int i = 0; i < b; i++)
            block[i] = sc.nextInt();

        System.out.println("Enter process sizes:");
        for (int i = 0; i < p; i++)
            process[i] = sc.nextInt();


        System.out.println("\n--- First Fit Allocation ---");
        for (int i = 0; i < p; i++) {
            boolean allocated = false;

            for (int j = 0; j < b; j++) {
                if (!used[j] && block[j] >= process[i]) {
                    used[j] = true;
                    System.out.println("Process " + (i+1) + " (size " + process[i] + 
                        ") allocated to Block " + (j+1) + " (size " + block[j] + ")");
                    allocated = true;
                    break;
                }
            }

            if (!allocated)
                System.out.println("Process " + (i+1) + " (size " + process[i] + ") NOT allocated.");
        }

        sc.close();
    }
}
