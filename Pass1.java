import java.io.*;
import java.util.*;

public class Pass1 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new FileReader("sample.txt"));
        BufferedWriter icw = new BufferedWriter(new FileWriter("intermediate.txt"));
        BufferedWriter stw = new BufferedWriter(new FileWriter("symboltab.txt"));
        BufferedWriter ltw = new BufferedWriter(new FileWriter("literaltab.txt"));

        Map<String,String> IS = new HashMap<>();
        IS.put("STOP","00"); IS.put("ADD","01"); IS.put("SUB","02"); IS.put("MUL","03");
        IS.put("DIV","04"); IS.put("MOVER","04"); IS.put("MOVEM","05"); IS.put("COMP","06");
        IS.put("BC","07"); IS.put("READ","08"); IS.put("PRINT","09");

        Map<String,String> AD = new HashMap<>();
        AD.put("START","01"); AD.put("END","02"); AD.put("ORIGIN","03");
        AD.put("EQU","04"); AD.put("LTORG","05");

        Map<String,String> DL = new HashMap<>();
        DL.put("DC","01"); DL.put("DS","02");

        Map<String,String> REG = new HashMap<>();
        REG.put("AX","1"); REG.put("BX","2"); REG.put("CX","3"); REG.put("DX","4");
        REG.put("AREG","1"); REG.put("BREG","2"); REG.put("CREG","3"); REG.put("DREG","4");

        List<String> symlist = new ArrayList<>();              
        Map<String,Integer> symaddr = new LinkedHashMap<>();   
        List<String> litlist = new ArrayList<>();              
        Map<String,Integer> litAddr = new LinkedHashMap<>();  

        int LC = 0;
        String raw;
        while ((raw = br.readLine()) != null) {
            String line = raw.trim();
            if (line.isEmpty()) continue;

            line = line.replace(",", " ").replaceAll("\\s+", " ").trim();

            String[] parts = line.split("\\s+");
            String label = null, opcode = null, op1 = null, op2 = null;
            if (parts.length == 0) continue;

            if (parts[0].endsWith(":")) {
                label = parts[0].substring(0, parts[0].length()-1);
                if (parts.length > 1) opcode = parts[1];
                if (parts.length > 2) op1 = parts[2];
                if (parts.length > 3) op2 = parts[3];
            } else {
                String fupper = parts[0].toUpperCase();
                if ( (parts.length > 1) && !(IS.containsKey(fupper) || AD.containsKey(fupper) || DL.containsKey(fupper)) ) {
                    label = parts[0];
                    opcode = (parts.length > 1)? parts[1] : null;
                    op1 = (parts.length > 2)? parts[2] : null;
                    op2 = (parts.length > 3)? parts[3] : null;
                } else {
                    opcode = parts[0];
                    op1 = (parts.length > 1)? parts[1] : null;
                    op2 = (parts.length > 2)? parts[2] : null;
                }
            }

            if (opcode == null) continue;
            opcode = opcode.toUpperCase();
            if (op1 != null) op1 = op1.toUpperCase();
            if (op2 != null) op2 = op2.toUpperCase();
            if (label != null) label = label;

            if (label != null) {
                if (!symaddr.containsKey(label)) {
                    symlist.add(label);
                    symaddr.put(label, LC);
                } else {
                    symaddr.put(label, LC);
                    if (!symlist.contains(label)) symlist.add(label);
                }
            }

            if ("START".equals(opcode)) {
                if (op1 != null && op1.matches("\\d+")) {
                    LC = Integer.parseInt(op1);
                    icw.write(LC + " AD " + AD.get("START") + " C " + op1);
                    icw.newLine();
                } else {
                    LC = 0;
                    icw.write(LC + " AD " + AD.get("START"));
                    icw.newLine();
                }
                continue;
            }

            if ("END".equals(opcode)) {
                for (int i = 0; i < litlist.size(); i++) {
                    String lit = litlist.get(i);
                    if (!litAddr.containsKey(lit)) {
                        litAddr.put(lit, LC);
                        icw.write(LC + " DL " + DL.get("DC") + " " + lit);
                        icw.newLine();
                        LC++;
                    }
                }
                icw.write("    AD " + AD.get("END"));
                icw.newLine();
                break;
            }

            if ("LTORG".equals(opcode)) {
                icw.write(LC + " AD " + AD.get("LTORG"));
                icw.newLine();
                for (int i = 0; i < litlist.size(); i++) {
                    String lit = litlist.get(i);
                    if (!litAddr.containsKey(lit)) {
                        litAddr.put(lit, LC);
                        icw.write(LC + " DL " + DL.get("DC") + " " + lit);
                        icw.newLine();
                        LC++;
                    }
                }
                continue;
            }

            if ("ORIGIN".equals(opcode)) {
                icw.write(LC + " AD " + AD.get("ORIGIN") + " " + (op1==null? "" : op1));
                icw.newLine();
                if (op1 != null) {
                    if (op1.contains("+")) {
                        String[] s = op1.split("\\+");
                        String sym = s[0];
                        int offset = Integer.parseInt(s[1]);
                        if (symaddr.containsKey(sym) && symaddr.get(sym) != null) LC = symaddr.get(sym) + offset;
                        else LC = offset;
                    } else if (op1.matches("\\d+")) {
                        LC = Integer.parseInt(op1);
                    } else if (symaddr.containsKey(op1)) {
                        LC = symaddr.get(op1);
                    }
                }
                continue;
            }

            if ("EQU".equals(opcode)) {
                if (label != null && op1 != null) {
                    if (op1.matches("\\d+")) {
                        symaddr.put(label, Integer.parseInt(op1));
                        if (!symlist.contains(label)) symlist.add(label);
                    } else if (symaddr.containsKey(op1)) {
                        symaddr.put(label, symaddr.get(op1));
                        if (!symlist.contains(label)) symlist.add(label);
                    } else {
                        if (!symaddr.containsKey(label)) {
                            symaddr.put(label, -1);
                            symlist.add(label);
                        }
                    }
                    icw.write(LC + " AD " + AD.get("EQU") + " " + label + " " + op1);
                    icw.newLine();
                }
                continue;
            }

            if (DL.containsKey(opcode)) {
                if ("DC".equals(opcode)) {
                    if (op1 != null && op1.startsWith("=")) {
                        if (!litlist.contains(op1)) litlist.add(op1);
                        icw.write(LC + " DL " + DL.get("DC") + " " + op1);
                        icw.newLine();
                        LC++;
                    } else if (op1 != null && op1.matches("\\d+")) {
                        icw.write(LC + " DL " + DL.get("DC") + " C " + op1);
                        icw.newLine();
                        LC++;
                    } else if (op1 != null) {
                        if (!symaddr.containsKey(op1)) {
                            symlist.add(op1);
                            symaddr.put(op1, -1);
                        }
                        int sidx = symlist.indexOf(op1) + 1;
                        icw.write(LC + " DL " + DL.get("DC") + " S " + sidx);
                        icw.newLine();
                        LC++;
                    } else {
                        icw.write(LC + " DL " + DL.get("DC"));
                        icw.newLine();
                        LC++;
                    }
                } else {
                    int size = 1;
                    if (op1 != null && op1.matches("\\d+")) {
                        size = Integer.parseInt(op1);
                        icw.write(LC + " DL " + DL.get("DS") + " C " + op1);
                        icw.newLine();
                    } else if (op1 != null) {
                        if (!symaddr.containsKey(op1)) {
                            symlist.add(op1);
                            symaddr.put(op1, -1);
                        }
                        int sidx = symlist.indexOf(op1) + 1;
                        icw.write(LC + " DL " + DL.get("DS") + " S " + sidx);
                        icw.newLine();
                    } else {
                        icw.write(LC + " DL " + DL.get("DS"));
                        icw.newLine();
                    }
                    LC += size;
                }
                continue;
            }

            if (IS.containsKey(opcode)) {
                StringBuilder sb = new StringBuilder();
                sb.append(LC).append(" IS ").append(IS.get(opcode));

                if (op1 != null) {
                    if (REG.containsKey(op1)) {
                        sb.append(" ").append(REG.get(op1));
                    } else if (op1.matches("\\d+")) {
                        sb.append(" C ").append(op1);
                    } else if (op1.startsWith("=")) {
                        if (!litlist.contains(op1)) litlist.add(op1);
                        int lidx = litlist.indexOf(op1) + 1;
                        sb.append(" L ").append(lidx);
                    } else {
                        if (!symaddr.containsKey(op1)) {
                            symlist.add(op1);
                            symaddr.put(op1, -1);
                        }
                        int sidx = symlist.indexOf(op1) + 1;
                        sb.append(" S ").append(sidx);
                    }
                }

                if (op2 != null) {
                    if (REG.containsKey(op2)) {
                        sb.append(" ").append(REG.get(op2));
                    } else if (op2.matches("\\d+")) {
                        sb.append(" C ").append(op2);
                    } else if (op2.startsWith("=")) {
                        if (!litlist.contains(op2)) litlist.add(op2);
                        int lidx = litlist.indexOf(op2) + 1;
                        sb.append(" L ").append(lidx);
                    } else {
                        if (!symaddr.containsKey(op2)) {
                            symlist.add(op2);
                            symaddr.put(op2, -1);
                        }
                        int sidx = symlist.indexOf(op2) + 1;
                        sb.append(" S ").append(sidx);
                    }
                }

                icw.write(sb.toString());
                icw.newLine();
                LC++;
                continue;
            }

            icw.write("; Skipped (unknown opcode) " + line);
            icw.newLine();
        }

        for (int i = 0; i < symlist.size(); i++) {
            String sym = symlist.get(i);
            int addr = symaddr.containsKey(sym) ? symaddr.get(sym) : -1;
            stw.write((i+1) + " " + sym + " " + addr);
            stw.newLine();
        }

        for (int i = 0; i < litlist.size(); i++) {
            String lit = litlist.get(i);
            Integer a = litAddr.get(lit);
            int addr = (a == null) ? -1 : a;
            ltw.write((i+1) + " " + lit + " " + addr);
            ltw.newLine();
        }

        br.close();
        icw.close();
        stw.close();
        ltw.close();
    }
}
