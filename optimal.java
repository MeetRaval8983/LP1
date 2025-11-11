import java.util.*;

public class optimal {
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

        int faults = 0, hits = 0;

        System.out.println("\nPage\tFrames");

        for (int i = 0; i < n; i++) {
            int page = pages[i];
            boolean hit = false;

            // HIT check
            for (int j = 0; j < framesCount; j++) {
                if (frames[j] == page) {
                    hit = true;
                    hits++;
                    break;
                }
            }

            if (!hit) {
                faults++;

                int replaceIndex = -1;
                int farthest = -1;

                // Check if empty frame exists
                for (int j = 0; j < framesCount; j++) {
                    if (frames[j] == -1) {
                        replaceIndex = j;
                        break;
                    }
                }

                // If no empty frame → apply Optimal logic
                if (replaceIndex == -1) {
                    for (int j = 0; j < framesCount; j++) {
                        int nextUse = Integer.MAX_VALUE;

                        for (int k = i + 1; k < n; k++) {
                            if (frames[j] == pages[k]) {
                                nextUse = k;
                                break;
                            }
                        }

                        if (nextUse > farthest) {
                            farthest = nextUse;
                            replaceIndex = j;
                        }
                    }
                }

                frames[replaceIndex] = page;
            }

            // Print frames
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
