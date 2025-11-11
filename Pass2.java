import java.io.*;
import java.util.*;

public class Pass2 {
    public static void main(String[] args) throws Exception {
        Map<Integer, String> sname = new HashMap<>();
        Map<Integer, Integer> saddress = new HashMap<>();
        BufferedReader st = new BufferedReader(new FileReader("symboltab.txt"));
        String line;
        while ((line = st.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            String[] p = line.split("\\s+");
            if (p.length >= 3) {
                int idx = Integer.parseInt(p[0]);
                String name = p[1];
                int addr = Integer.parseInt(p[2]);
                sname.put(idx, name);
                saddress.put(idx, addr);
            }
        }
        st.close();

        Map<Integer, String> liLit = new HashMap<>();
        Map<Integer, Integer> liAddr = new HashMap<>();
        BufferedReader lt = new BufferedReader(new FileReader("literaltab.txt"));
        while ((line = lt.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            String[] p = line.split("\\s+");
            if (p.length >= 3) {
                int idx = Integer.parseInt(p[0]);
                String lit = p[1]; 
                int addr = Integer.parseInt(p[2]);
                liLit.put(idx, lit);
                liAddr.put(idx, addr);
            }
        }
        lt.close();

        BufferedReader icPre = new BufferedReader(new FileReader("intermediate.txt"));
        while ((line = icPre.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            if (line.contains(" AD ")) continue;

            String[] tok = line.split("\\s+");
            if (tok.length < 2) continue;
            int lc;
            try {
                lc = Integer.parseInt(tok[0]);
            } catch (Exception e) { continue; }

            String type = tok[1];
            if ("DL".equals(type)) {
                for (int i = 2; i < tok.length - 1; i++) {
                    if ("S".equals(tok[i])) {
                        String next = tok[i+1];
                        try {
                            int sidx = Integer.parseInt(next);
                            saddress.put(sidx, lc);
                        } catch (NumberFormatException ex) {
                            for (Map.Entry<Integer,String> e : sname.entrySet()) {
                                if (e.getValue().equalsIgnoreCase(next)) {
                                    saddress.put(e.getKey(), lc);
                                    break;
                                }
                            }
                        }
                    }
                }
            }
        }
        icPre.close();

        BufferedReader ic = new BufferedReader(new FileReader("intermediate.txt"));
        BufferedWriter mc = new BufferedWriter(new FileWriter("machinecode.txt"));

        while ((line = ic.readLine()) != null) {
            line = line.trim();
            if (line.isEmpty()) continue;
            if (line.contains(" AD ")) continue;

            String[] tok = line.split("\\s+");
            if (tok.length < 2) continue;
            int lc;
            try { lc = Integer.parseInt(tok[0]); }
            catch (Exception e) { continue; }
            String type = tok[1];

            if ("IS".equals(type)) {
                // [opcode] [reg or C or S or L ...]
                String opcode = (tok.length > 2) ? tok[2] : "00";
                int regCode = 0;
                int addr = 0;

                int i = 3;
                if (i < tok.length && tok[i].matches("\\d+")) {
                    regCode = Integer.parseInt(tok[i]);
                    i++;
                } else if (i < tok.length && ("C".equals(tok[i]) || "S".equals(tok[i]) || "L".equals(tok[i]))) {
                } else if (i < tok.length && tok[i].matches("\\d+")) {
                    regCode = Integer.parseInt(tok[i]);
                    i++;
                }

                while (i < tok.length) {
                    String t = tok[i];
                    if ("C".equals(t) && i+1 < tok.length) {
                        try { addr = Integer.parseInt(tok[i+1]); } catch(Exception ex){ addr = 0; }
                        break;
                    } else if ("S".equals(t) && i+1 < tok.length) {
                        try {
                            int sidx = Integer.parseInt(tok[i+1]);
                            addr = saddress.getOrDefault(sidx, 0);
                        } catch (Exception ex) {
                            addr = 0;
                        }
                        break;
                    } else if ("L".equals(t) && i+1 < tok.length) {
                        try {
                            int lidx = Integer.parseInt(tok[i+1]);
                            addr = liAddr.getOrDefault(lidx, 0);
                        } catch (Exception ex) {
                            addr = 0;
                        }
                        break;
                    } else if (t.matches("\\d+")) {
                        addr = Integer.parseInt(t);
                        break;
                    }
                    i++;
                }

                mc.write(lc + " " + opcode + " " + regCode + " " + addr);
                mc.newLine();
            }
            else if ("DL".equals(type)) {
                if (tok.length >= 3 && "01".equals(tok[2])) { // DC
                    if (tok.length > 3 && "C".equals(tok[3]) && tok.length > 4) {
                        mc.write(lc + " " + tok[4]);
                        mc.newLine();
                    } else if (tok.length > 3 && "S".equals(tok[3]) && tok.length > 4) {
                        try {
                            int sidx = Integer.parseInt(tok[4]);
                            int sval = saddress.getOrDefault(sidx, 0);
                            mc.write(lc + " " + sval);
                            mc.newLine();
                        } catch (Exception ex) {
                            mc.write(lc + " 0");
                            mc.newLine();
                        }
                    } else if (tok.length > 3) {
                        // maybe literal like ='5'
                        String v = tok[3];
                        if (v.startsWith("='") && v.endsWith("'")) {
                            String num = v.replace("='","").replace("'","");
                            mc.write(lc + " " + num);
                            mc.newLine();
                        } else {
                            String num = v.replaceAll("[^0-9]","");
                            if (num.isEmpty()) num = "0";
                            mc.write(lc + " " + num);
                            mc.newLine();
                        }
                    } else {
                        mc.write(lc + " 0");
                        mc.newLine();
                    }
                } else if (tok.length >= 3 && "02".equals(tok[2])) { // DS
                    mc.write(lc + " 0");
                    mc.newLine();
                }
            }
        }

        ic.close();
        mc.close();
    }
}
