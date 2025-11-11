import java.io.*;

class mdt {
    String stmnt = "";
}

class mnt {
    String name;
    int addr;
    int argStart;
    int argCount;

    mnt(String name, int addr) {
        this.name = name;
        this.addr = addr;
        this.argStart = 0;
        this.argCount = 0;
    }
}

class arglist {
    String argname;
    String value;

    arglist(String argname) {
        this.argname = argname;
        this.value ="";
    }
}

public class Pass1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br1 = new BufferedReader(new FileReader("input.txt"));
        String line;

        mdt[] MDT = new mdt[50];
        mnt[] MNT = new mnt[20];
        arglist[] ARGLIST = new arglist[50];

        boolean macro_start = false, macro_end = false, fill_arglist = false;
        int mdt_cnt = 0, mnt_cnt = 0, arglist_cnt = 0;

        while ((line = br1.readLine()) != null) {
            if (line.trim().isEmpty()) continue;
            line = line.replaceAll(",", " ");
            String[] tokens = line.trim().split("\\s+");

            String stmnt = "";

            for (int i = 0; i < tokens.length; i++) {
                if (tokens[i].equalsIgnoreCase("mend")) {
                    MDT[mdt_cnt] = new mdt();
                    MDT[mdt_cnt++].stmnt = "\t" + tokens[i];
                    macro_end = true;
                    continue;
                }

                if (tokens[i].equalsIgnoreCase("macro")) {
                    macro_start = true;
                    macro_end = false;
                    continue;
                }

                if (!macro_end) {
                    if (macro_start) {
                        MNT[mnt_cnt] = new mnt(tokens[i], mdt_cnt);
                        MNT[mnt_cnt].argStart = arglist_cnt;
                        mnt_cnt++;
                        macro_start = false;
                        fill_arglist = true;
                        continue;
                    }

                    if (fill_arglist) {
                        MDT[mdt_cnt] = new mdt();
                        MDT[mdt_cnt].stmnt = "\t" + MNT[mnt_cnt - 1].name;
                        stmnt = MDT[mdt_cnt].stmnt;

                        while (i < tokens.length) {
                            String tok = tokens[i];
                            MDT[mdt_cnt].stmnt += "\t" + tok;
                            stmnt += "\t" + tok;

                            String formal = tok.contains("=") ? tok.substring(0, tok.indexOf('=')) : tok;
                            if (formal.matches("&[a-zA-Z][a-zA-Z0-9]*")) {
                                ARGLIST[arglist_cnt++] = new arglist(formal);
                            }
                            i++;
                        }

                        MNT[mnt_cnt - 1].argCount = arglist_cnt - MNT[mnt_cnt - 1].argStart;

                        mdt_cnt++;
                        fill_arglist = false;
                    } else {
                        MDT[mdt_cnt] = new mdt();

                        for (; i < tokens.length; i++) {
                            String token = tokens[i];

                            if (token.matches("&[a-zA-Z][a-zA-Z0-9]*")) {
                                boolean found = false;

                                for (int j = 0; j < arglist_cnt; j++) {
                                    if (token.equals(ARGLIST[j].argname)) {
                                        MDT[mdt_cnt].stmnt += "\t#" + j;
                                        stmnt += "\t" + j;
                                        found = true;
                                        break;
                                    }
                                }
                                if (!found) {
                                    MDT[mdt_cnt].stmnt += "\t" + token;
                                    stmnt += "\t" + token;
                                }
                            } else {
                                MDT[mdt_cnt].stmnt += "\t" + token;
                                stmnt += "\t" + token;
                            }
                        }
                        if (!stmnt.equals("")) {
                            mdt_cnt++;
                        }
                    }
                }
            }
        }

        br1.close();

        BufferedWriter bw = new BufferedWriter(new FileWriter("MNT.txt"));
        System.out.println("\n\t******* MACRO NAME TABLE *******");
        System.out.println("\n\tINDEX\tNAME\tMDT_INDEX\tARG_COUNT");

        for (int i = 0; i < mnt_cnt; i++) {
            System.out.println("\t" + i + "\t" + MNT[i].name + "\t" + MNT[i].addr + "\t" + MNT[i].argCount);
            bw.write(i + "\t" + MNT[i].name + "\t" + MNT[i].addr + "\t" + MNT[i].argCount + "\n");
        }
        bw.close();


        bw = new BufferedWriter(new FileWriter("arglist.txt"));
        System.out.println("\n\n\t******** ARGUMENT LIST **********");
        System.out.println("\n\tINDEX\tNAME");

        for (int i = 0; i < arglist_cnt; i++) {
            System.out.println("\t" + i + "\t" + ARGLIST[i].argname);
            bw.write(ARGLIST[i].argname + "\n");
        }
        bw.close();

        bw = new BufferedWriter(new FileWriter("MDT.txt"));
        System.out.println("\n\t******** MACRO DEFINITION TABLE **********");
        System.out.println("\n\tINDEX\t\tSTATEMENT");

        for (int i = 0; i < mdt_cnt; i++) {
            System.out.println("\t" + i + "\t" + MDT[i].stmnt);
            bw.write(MDT[i].stmnt + "\n");
        }
        bw.close();
    }
}

