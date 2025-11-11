import java.util.*;

public class Priority_Preemptive {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n];
        int[] at = new int[n];
        int[] bt = new int[n];
        int[] rt = new int[n];   // remaining time
        int[] pr = new int[n];
        int[] ct = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];

        for (int i = 0; i < n; i++) {
            pid[i] = i + 1;
            System.out.print("Enter AT, BT, Priority for P" + pid[i] + ": ");
            at[i] = sc.nextInt();
            bt[i] = sc.nextInt();
            pr[i] = sc.nextInt();
            rt[i] = bt[i];
        }

        int time = 0, completed = 0;

        while (completed < n) {
            int idx = -1;
            int bestPriority = Integer.MAX_VALUE;

            // Find highest priority (lowest number)
            for (int i = 0; i < n; i++) {
                if (at[i] <= time && rt[i] > 0) {
                    if (pr[i] < bestPriority) {
                        bestPriority = pr[i];
                        idx = i;
                    }
                }
            }

            if (idx == -1) {
                time++;  // CPU idle
                continue;
            }

            rt[idx]--;   // Execute 1 unit
            time++;

            if (rt[idx] == 0) {
                ct[idx] = time;
                completed++;
            }
        }

        // Calculate TAT & WT
        float totalTAT = 0, totalWT = 0;

        for (int i = 0; i < n; i++) {
            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
            totalTAT += tat[i];
            totalWT += wt[i];
        }

        // Output
        System.out.println("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT");
        for (int i = 0; i < n; i++) {
            System.out.println(pid[i] + "\t" + at[i] + "\t" + bt[i] + "\t" +
                               pr[i] + "\t" + ct[i] + "\t" + tat[i] + "\t" + wt[i]);
        }

        System.out.printf("\nAverage TAT = %.2f", totalTAT / n);
        System.out.printf("\nAverage WT  = %.2f\n", totalWT / n);

        sc.close();
    }
}
