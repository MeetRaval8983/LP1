import java.util.Scanner;

public class worstfit {
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

        System.out.println("\n--- Worst Fit Allocation ---");

        for (int i = 0; i < p; i++) {
            int worstIndex = -1;
            int maxWaste = -1;

            for (int j = 0; j < b; j++) {
                if (!used[j] && block[j] >= process[i]) {
                    int waste = block[j] - process[i];
                    if (waste > maxWaste) {
                        maxWaste = waste;
                        worstIndex = j;
                    }
                }
            }

            if (worstIndex != -1) {
                used[worstIndex] = true;
                System.out.println("Process " + (i+1) + " (size " + process[i] +
                    ") allocated to Block " + (worstIndex+1) +
                    " (size " + block[worstIndex] + ")");
            } else {
                System.out.println("Process " + (i+1) + " (size " + process[i] + ") NOT allocated.");
            }
        }

        sc.close();
    }
}
