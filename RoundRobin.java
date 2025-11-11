import java.util.*;

public class RoundRobin {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] pid = new int[n];
        int[] bt = new int[n];
        int[] rt = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];

        for (int i = 0; i < n; i++) {
            pid[i] = i + 1;
            System.out.print("Enter burst time for P" + pid[i] + ": ");
            bt[i] = sc.nextInt();
            rt[i] = bt[i];
        }

        System.out.print("Enter time quantum: ");
        int tq = sc.nextInt();

        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) q.add(i);

        int time = 0;

        while (!q.isEmpty()) {
            int idx = q.poll();

            if (rt[idx] > tq) {
                time += tq;
                rt[idx] -= tq;
                q.add(idx);
            } else {
                time += rt[idx];
                rt[idx] = 0;
                tat[idx] = time;
                wt[idx] = tat[idx] - bt[idx];
            }
        }

        // Output
        System.out.println("\nPID\tBT\tWT\tTAT");
        float totalWT = 0, totalTAT = 0;

        for (int i = 0; i < n; i++) {
            System.out.println(pid[i] + "\t" + bt[i] + "\t" + wt[i] + "\t" + tat[i]);
            totalWT += wt[i];
            totalTAT += tat[i];
        }

        System.out.printf("\nAverage WT  = %.2f", totalWT / n);
        System.out.printf("\nAverage TAT = %.2f\n", totalTAT / n);

        sc.close();
    }
}
