import java.util.*;

public class lru {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of frames: ");
        int framesCount = sc.nextInt();

        System.out.print("Enter number of pages: ");
        int n = sc.nextInt();

        int[] pages = new int[n];
        System.out.println("Enter pages:");
        for (int i = 0; i < n; i++)
            pages[i] = sc.nextInt();

        int[] frames = new int[framesCount];
        Arrays.fill(frames, -1);

        int faults = 0;
        int hits = 0;

        System.out.println("\nPage\tFrames");

        for (int i = 0; i < n; i++) {
            int page = pages[i];
            boolean hit = false;

            // Check if page in frame
            for (int j = 0; j < framesCount; j++) {
                if (frames[j] == page) {
                    hit = true;
                    hits++;
                    break;
                }
            }

            if (!hit) {
                faults++;

                // If free space exists
                int emptyPos = -1;
                for (int j = 0; j < framesCount; j++) {
                    if (frames[j] == -1) {
                        emptyPos = j;
                        break;
                    }
                }

                if (emptyPos != -1) {  
                    frames[emptyPos] = page;
                } else {
                    // LRU replacement
                    int lruIndex = 0;
                    int oldest = i;

                    for (int j = 0; j < framesCount; j++) {
                        int lastUsed = -1;
                        for (int k = i - 1; k >= 0; k--) {
                            if (pages[k] == frames[j]) {
                                lastUsed = k;
                                break;
                            }
                        }
                        if (lastUsed < oldest) {
                            oldest = lastUsed;
                            lruIndex = j;
                        }
                    }

                    frames[lruIndex] = page;
                }
            }

            // Print frame state
            System.out.print(page + "\t");
            for (int j = 0; j < framesCount; j++) {
                if (frames[j] == -1) System.out.print("- ");
                else System.out.print(frames[j] + " ");
            }
            System.out.println();
        }

        System.out.println("\nTotal Hits = " + hits);
        System.out.println("Total Faults = " + faults);
        System.out.println("Hit Ratio = " + (float)hits / n);
    }
}
