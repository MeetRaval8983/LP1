import java.util.*;

public class Priority_NonPreemptive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n];
        int[] bt = new int[n];
        int[] pr = new int[n];
        int[] wt = new int[n];
        int[] tat = new int[n];

        // Input
        for (int i = 0; i < n; i++) {
            pid[i] = i + 1;
            System.out.print("Enter BT and Priority for P" + pid[i] + ": ");
            bt[i] = sc.nextInt();
            pr[i] = sc.nextInt();
        }

        // Sort by priority (ascending)
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (pr[j] > pr[j + 1]) {
                    int temp;

                    temp = pr[j]; pr[j] = pr[j + 1]; pr[j + 1] = temp;
                    temp = bt[j]; bt[j] = bt[j + 1]; bt[j + 1] = temp;
                    temp = pid[j]; pid[j] = pid[j + 1]; pid[j + 1] = temp;
                }
            }
        }

        // Waiting & Turnaround Time
        wt[0] = 0;
        tat[0] = bt[0];

        for (int i = 1; i < n; i++) {
            wt[i] = wt[i - 1] + bt[i - 1];
            tat[i] = wt[i] + bt[i];
        }

        // Output
        System.out.println("\nPID\tBT\tPR\tWT\tTAT");
        float totalWT = 0, totalTAT = 0;

        for (int i = 0; i < n; i++) {
            System.out.println(pid[i] + "\t" + bt[i] + "\t" + pr[i] +
                               "\t" + wt[i] + "\t" + tat[i]);
            totalWT += wt[i];
            totalTAT += tat[i];
        }

        System.out.printf("\nAverage WT  = %.2f", totalWT / n);
        System.out.printf("\nAverage TAT = %.2f\n", totalTAT / n);

        sc.close();
    }
}
