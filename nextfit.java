import java.util.Scanner;

public class nextfit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter total no. of processes: ");
        int p = sc.nextInt();
        System.out.print("Enter total no. of blocks: ");
        int b = sc.nextInt();
        int[] process = new int[p];
        int[] block = new int[b];
        boolean[] alloc = new boolean[b];
        int tbs = 0, tps = 0;
        int ptr = 0;
        System.out.println("Enter the size of blocks: ");
        for(int i = 0; i < b; i++) {
            block[i] = sc.nextInt();
            tbs += block[i];
        }
        System.out.println("Enter the size of processes: ");
        for(int i = 0; i < p; i++) {
            process[i] = sc.nextInt();
        }
        for(int i = 0; i < p; i++) {
            int count = 0;
            for(int j = ptr; count < b; j = (j + 1) % b, count++) {
                if(process[i] <= block[j] && !alloc[j]) {
                    alloc[j] = true;
                    tps += process[i];
                    ptr = (j + 1) % b;
                 
                    System.out.println("Process " + (i + 1) + " of size " + process[i] + " allocated to block " + (j + 1) + " of size " + block[j]);
                    break;
                }
            }
        }
        System.out.println("Total block size: " + tbs);
        System.out.println("Total process size: " + tps);
        float f = (float)(tps)/(float)(tbs);
        System.out.println("Next fit: " + f);
    }
}
