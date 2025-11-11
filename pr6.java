import java.util.concurrent.Semaphore;

public class pr6 {
    static int readCount = 0;
    static Semaphore mutex = new Semaphore(1);
    static Semaphore wrt = new Semaphore(1);

    static class Reader extends Thread {
        int id;

        Reader(int id) {
            this.id = id;
        }

        public void run() {
            try {
                mutex.acquire();
                readCount++;
                if (readCount == 1) {
                    wrt.acquire();
                }
                mutex.release();
                System.out.println("Reader " + id + " is READING...");
                Thread.sleep(500);
                mutex.acquire();
                readCount--;
                if (readCount == 0) {
                    wrt.release();
                }
                mutex.release();
                System.out.println("Reader " + id + " has FINISHED READING.");
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    static class Writer extends Thread {
        int id;

        Writer(int id) {
            this.id = id;
        }

        public void run() {
            try {
                wrt.acquire();
                System.out.println("Writer " + id + " is WRITING...");
                Thread.sleep(800);
                System.out.println("Writer " + id + " has FINISHED WRITING.");

                wrt.release();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        new Reader(1).start();
        new Writer(1).start();
        new Reader(2).start();
        new Writer(2).start();
        new Reader(3).start();
    }
}