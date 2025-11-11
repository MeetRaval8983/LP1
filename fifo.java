import java.util.*;

public class fifo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of frames: ");
        int frames = sc.nextInt();

        System.out.print("Enter number of pages: ");
        int n = sc.nextInt();

        int[] pages = new int[n];
        System.out.println("Enter page reference string:");
        for (int i = 0; i < n; i++) {
            pages[i] = sc.nextInt();
        }

        int[] frame = new int[frames];
        Arrays.fill(frame, -1);  // initially all frames empty

        int pointer = 0;   // FIFO pointer
        int faults = 0;

        System.out.println("\nPage\tFrames");

        for (int i = 0; i < n; i++) {
            int page = pages[i];
            boolean hit = false;

            // Check if page is already present
            for (int j = 0; j < frames; j++) {
                if (frame[j] == page) {
                    hit = true;
                    break;
                }
            }

            // If NOT found → page fault
            if (!hit) {
                frame[pointer] = page;    // replace oldest page
                pointer = (pointer + 1) % frames;  // move in circular manner
                faults++;
            }

            // Print frame status
            System.out.print(page + "\t");
            for (int j = 0; j < frames; j++) {
                if (frame[j] == -1) System.out.print("- ");
                else System.out.print(frame[j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nTotal Page Faults = " + faults);
        sc.close();
    }
}
