import java.util.*;

public class SJF_NonPreemptive {
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
        boolean[] done = new boolean[n];

        for (int i = 0; i < n; i++) {
            pid[i] = i + 1;
            System.out.print("Enter AT and BT for P" + pid[i] + ": ");
            at[i] = sc.nextInt();
            bt[i] = sc.nextInt();
        }

        int time = 0, completed = 0;

        while (completed < n) {
            int idx = -1;
            int minBT = Integer.MAX_VALUE;

            // Find shortest burst among arrived processes
            for (int i = 0; i < n; i++) {
                if (!done[i] && at[i] <= time && bt[i] < minBT) {
                    minBT = bt[i];
                    idx = i;
                }
            }

            if (idx == -1) {
                time++; // No arrival yet
            } else {
                ct[idx] = time + bt[idx];
                time = ct[idx];
                done[idx] = true;
                completed++;
            }
        }

        // Compute TAT and WT
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
            System.out.println(pid[i] + "\t" + at[i] + "\t" + bt[i] + "\t" +
                               ct[i] + "\t" + tat[i] + "\t" + wt[i]);
        }

        System.out.printf("\nAverage TAT = %.2f", totalTAT / n);
        System.out.printf("\nAverage WT  = %.2f\n", totalWT / n);

        sc.close();
    }
}
