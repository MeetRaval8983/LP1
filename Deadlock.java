import java.util.Scanner;

public class Deadlock {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter number of processes:");
        int p = sc.nextInt();
        System.out.println("Enter number of resources:");
        int r = sc.nextInt();
        int[][] max = new int[p][r];
        int[][] alloc = new int[p][r];
        int[][] avail = new int[p][r];
        int[][] need = new int[p][r];
        boolean[] finish = new boolean[p];
        System.out.println("Enter the maximum resources for each process:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                max[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter the allocated resources for each process:");
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                alloc[i][j] = sc.nextInt();
            }
        }
        System.out.println("Enter the available resources:");
        for (int j = 0; j < r; j++) {
            avail[0][j] = sc.nextInt();
        }
        for (int i = 0; i < p; i++) {
            for (int j = 0; j < r; j++) {
                need[i][j] = max[i][j] - alloc[i][j];
            }
        }
        int count =  0;
        boolean d = false;
        while(count < p) {
            boolean f = false;
            for(int i = 0; i < p; i++) {
                if(!finish[i]) {
                    int j;
                    for(j = 0; j < r; j++) {
                        if(need[i][j] > avail[0][j]) {
                            break;
                        }
                    }
                    if(j == r) {
                        for(int k = 0; k < r; k++) {
                            avail[0][k] += alloc[i][k];
                        }
                        finish[i] = true;
                        f = true;
                        count++;
                        System.out.println("Process " + i + " has finished.");
                    }
                }
            }
            if(!f) {
                d = true;
                break;
            }
        }
        if(d) {
            System.out.println("Deadlock has occurred.");
        } else {
            System.out.println("No deadlock.");
        }
    }
}