import java.util.*;

public class FCFS {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n];
        int[] at = new int[n];
        int[] bt = new int[n];
        int[] ct = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];

        // Input
        for (int i = 0; i < n; i++) {
            pid[i] = i + 1;
            System.out.print("Enter AT and BT for P" + pid[i] + ": ");
            at[i] = sc.nextInt();
            bt[i] = sc.nextInt();
        }

        // Sort by Arrival Time
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (at[j] > at[j + 1]) {
                    int t;

                    t = at[j]; at[j] = at[j + 1]; at[j + 1] = t;
                    t = bt[j]; bt[j] = bt[j + 1]; bt[j + 1] = t;
                    t = pid[j]; pid[j] = pid[j + 1]; pid[j + 1] = t;
                }
            }
        }

        // Calculate CT
        ct[0] = at[0] + bt[0];
        for (int i = 1; i < n; i++) {
            if (ct[i - 1] < at[i])
                ct[i] = at[i] + bt[i];   // CPU idle
            else
                ct[i] = ct[i - 1] + bt[i];
        }

        // Calculate TAT and WT
        float totalTAT = 0, totalWT = 0;

        for (int i = 0; i < n; i++) {
            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
            totalTAT += tat[i];
            totalWT += wt[i];
        }

        // Output
        System.out.println("\nPID\tAT\tBT\tCT\tTAT\tWT");
        for (int i = 0; i < n; i++) {
            System.out.println(pid[i] + "\t" + at[i] + "\t" + bt[i] +
                               "\t" + ct[i] + "\t" + tat[i] + "\t" + wt[i]);
        }

        System.out.printf("\nAverage TAT = %.2f", (totalTAT / n));
        System.out.printf("\nAverage WT = %.2f\n", (totalWT / n));

        sc.close();
    }
}
