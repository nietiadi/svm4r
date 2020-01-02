import java.util.*;
import java.io.*;
import java.util.regex.*;

public class ExtractProof02{
  static ArrayList<String> raw = new ArrayList<String>();
  static ArrayList<Clause> eresParents = new ArrayList<Clause>();
  static ArrayList<String> statistics = new ArrayList<String>();
  static ArrayList<Clause> clauses = new ArrayList<Clause>();
  static HashMap<String, Clause> map = new HashMap<String, Clause>();
  static int lineNum = 1;
  static int maxInput = 0;
  static int emptyClsNum = 0;
  static boolean foundProof = true;

  public static void main(String[] args) throws Exception{
    FileReader fr = new FileReader("tmp");
    BufferedReader br = new BufferedReader(fr);

    Pattern p = Pattern.compile(".*CTL-RP\\sversion.*");
    Matcher m = null;

    String line = "";
    boolean flag = false;
    for(;(line=br.readLine())!=null; lineNum++){
      m = p.matcher(line);
      if(m.matches()){
	addStatisics(br, line);
	DB.ol("==== Add statistics");
	continue;
	//break;
      }
	
      if(line.contains("This is a")){
	ignoreLines(10, br);
	continue;
      }

      if(line.matches("##ERES\\d:\\d+\\sbegin")){
	ArrayList<String> eres = addERES(br, line);
	if(eres!=null){
	  docERES(eres);
	}else{
	  continue;
	}
	DB.ol("==== One ERES");
      }

      raw.add(line);
      //System.out.println(lineNum+":"+line);
      //if(flag){
	//System.out.println(line);
	//bw.write(line, 0, line.length());
	//bw.write('\n');
      //}
      //*/
      //System.out.println(m.matches());
      //System.out.println(line);
    }
    br.close();

    if(foundProof){
      DB.ol("==== Proof found");
      createClauses();
      DB.ol("==== Clauses are created");
      HashSet<Integer> pfInd = traceProof(emptyClsNum, map);
      DB.ol("==== Traces are created");
      printProof(pfInd);
      //printClauses();
      //printStringList(raw);
    }
    printStringList(statistics);
    //System.out.println(map);
  }
  static void printProof(HashSet<Integer> pfInd){
    TreeSet<Integer> sorted = new TreeSet<Integer>(pfInd);
    //System.out.println(sorted);
    Iterator<Integer> it = sorted.iterator();
    while(it.hasNext()){
      int index = it.next();
      printSingleClause(map.get(String.valueOf(index)));
    }
  }

  static HashSet<Integer> traceProof(int clsNum, HashMap<String, Clause> trace){
    HashSet<Integer> nums = new HashSet<Integer>();
    ArrayList<Integer> stack = new ArrayList<Integer>();
    //stack.add(trace.get(String.valueOf(clsNum)).number);
    stack.add(clsNum);
    //System.out.println("trace:limit:"+limit);
    while(stack.size()!=0){
      Clause cls = trace.get(String.valueOf(stack.remove(0)));
      if(cls==null || cls.used){
	continue;
      }
      cls.used = true;
      //DB.o(cls.number+",");
      nums.add(cls.number);
      stack.addAll(cls.getParents());
    }
    return nums;
  }

  static void overwriteEresClauseParents(){
  }

  static void createClauses(){
    //System.out.println("##last line:"+raw.get(raw.size()-1));
    String lastLine = raw.get(raw.size()-1);
    emptyClsNum = Integer.parseInt(lastLine.substring(0, lastLine.indexOf('[')));
    //System.out.println("##empty cls :"+emptyClsNum);
    int size = raw.size();
    int i = 0;
    for(i=0; i<size; i++){
      String line = raw.get(i);
      if(line==null ||
	  line.equals("") ||
	  line.startsWith("****") ||
	  line.startsWith("====")){
	continue;
      }else if(line.startsWith("##Input of determinate clauses")){
	break;
      }
    }

    String inputCls = null;
    while(true){
      inputCls = raw.get(++i);/* Read */
      if(inputCls==null || inputCls.equals("")){
	continue;
      }
      if(inputCls.startsWith("##Input of sometime clauses")){
	break;
      }
      Clause cls = new Clause();
      int index = inputCls.indexOf('[');
      //System.out.println(inputCls);
      cls.number = Integer.parseInt(inputCls.substring(0, index));
      index = inputCls.indexOf('|');
      cls.content = inputCls.substring(index+3);
      cls.origin = Clause.INP;
      map.put(String.valueOf(cls.number), cls);
    }
    maxInput = i;
    //printClauses();
    //break;
    while(true){
      inputCls = raw.get(++i);/* Read */
      if(inputCls == null || inputCls.equals("")){
	continue;
      }
      if(inputCls.startsWith("##Proof")){
	break;
      }
      Clause cls = new Clause();
      int index = inputCls.indexOf('.');
      //System.out.println(index);
      cls.number = Integer.parseInt(inputCls.substring(1, index));
      cls.number = cls.number*-1;/* sometime clause */
      cls.content = inputCls.substring(index+1);
      cls.origin = Clause.INP;
      map.put(String.valueOf(cls.number), cls);
    }
    //printClauses();
    //break;
    for(; i<size; i++){
      String line = raw.get(i);
      //if(line.matches(".*\\d[.*].*")){
      if(line.contains("->") && line.indexOf(']')>0){/* This line is a clause */
	int index1 = 0;
	for(; index1<line.length(); index1++){
	  if(Character.isDigit(line.charAt(index1))){
	    break;
	  }
	}
	int index2 = line.indexOf(']');
	for(; index2<line.length(); index2++){
	  if(line.charAt(index2)=='.'){
	    break;
	  }
	}
        //System.out.println(line.substring(index1, index2+1));
	
        String clsStr = line.substring(index1, index2+1);
	int index = clsStr.indexOf('[');
	int clsNum = Integer.parseInt(clsStr.substring(0, index));
	Clause cls = map.get(String.valueOf(clsNum));
	if(cls!=null){/* the clause exists */
	  if(cls.origin.equals(Clause.ERES1) || cls.origin.equals(Clause.ERES2)){
	    //System.out.println("Helloooooo:"+cls);
	    cls.updateContent(clsStr);
	    //System.out.println("Helloooooo:"+cls);
	  }
	  continue;
	}
	cls = new Clause(clsNum, clsStr);
	map.put(String.valueOf(cls.number), cls);
      }
    }
  }

  static void printClauses(){
    Set<String> keySet = map.keySet();
    Iterator<String> it = keySet.iterator();
    while(it.hasNext()){
      Clause cls = map.get(it.next());
      printSingleClause(cls);
    }
  }

  static void printSingleClause(Clause cls){
    StringBuffer sb = new StringBuffer();
    sb.append(cls.number+"["+cls.origin+":");
    Iterator<Integer> it = cls.getParents().iterator();
    while(it.hasNext()){
      sb.append(it.next()+",");
    }
    sb.deleteCharAt(sb.length()-1);/* remove the last comma */

    sb.append("] || "+cls.content);
    System.out.println(sb);
  }


  static void docERES(ArrayList<String> lines){
    /* Get origin */
    String line = lines.get(0);/* line 1 */
    String origin = line.substring(2, 7);

    /* Get sometime clause's number */
    StringBuffer numEres = new StringBuffer();
    for(int i=line.indexOf(':'); i<line.length() ; i++){
      if(Character.isDigit(line.charAt(i))){
	numEres.append(line.charAt(i));
      }
    }
    //System.out.println(numEres);

    /* Get current max clause number  */
    String max = lines.get(3);
    max = max.substring(max.lastIndexOf(' ')+1);
    int currentMaxClauseNumber = Integer.parseInt(max);
    //System.out.println(currentMaxClauseNumber);

    /* Get resolvents' numbers */
    String rsv = lines.get(lines.size()-1);
    rsv = rsv.substring(rsv.lastIndexOf(':')+1);
    String[] rsvArr = rsv.split(";");
    //System.out.println(rsvArr.length);

    /* Get premises of ERES */
    HashSet<Integer> pms = getERESPremises(lines, currentMaxClauseNumber);
    pms.add(Integer.parseInt(numEres.toString())*-1);
    //System.out.println(pms);
    //printStringList(lines);

    for(int i=0; i<rsvArr.length; i++){
      Clause cls = new Clause();
      cls.number = Integer.parseInt(rsvArr[i]);
      cls.addParents(pms);
      if(origin.equals(Clause.ERES1)){
	cls.origin = Clause.ERES1;
      }else if(origin.equals(Clause.ERES2)){
	cls.origin = Clause.ERES2;
      }
      map.put(String.valueOf(cls.number), cls);
      //printSingleClause(cls);
    }

  }

  static HashSet<Integer> getERESPremises(ArrayList<String> lines, int currentMaxClauseNumber){
    HashSet<Integer> pms = new HashSet<Integer>();
    int index = lines.size()-1;
    for(; index>0; index--){
      if(lines.get(index).contains("Number of saturation")){
	break;
      }
    }
    HashMap<String, Clause> tmpMap = new HashMap<String, Clause>();

    for(; index<lines.size(); index++){
      String line = lines.get(index);
      if(line.contains("->") && line.indexOf(']')>0){/* This line is a clause */
	int index1 = 0;
	for(; index1<line.length(); index1++){
	  if(Character.isDigit(line.charAt(index1))){
	    break;
	  }
	}
	int index2 = line.indexOf(']');
	for(; index2<line.length(); index2++){
	  if(line.charAt(index2)=='.'){
	    break;
	  }
	}
        //System.out.println(line.substring(index1, index2+1));
	
        String clsStr = line.substring(index1, index2+1);
	int indexNum = clsStr.indexOf('[');
	int clsNum = Integer.parseInt(clsStr.substring(0, indexNum));
	if(map.get(String.valueOf(clsNum))!=null){/* the clause exists */
	  continue;
	}
	Clause cls = new Clause(clsNum, clsStr);
	tmpMap.put(String.valueOf(cls.number), cls);
      }
    }

    ArrayList<Integer> goalCls = new ArrayList<Integer>();
    for(int i=lines.size()-1; i>0; i--){
      String line = lines.get(i);
      if(line.contains("====")){
	break;
      }else if(line.contains("T2")){
	goalCls.add(Integer.parseInt(line.substring(2, line.indexOf(' '))));
        //System.out.println(line.substring(2, line.indexOf(' ')));
      }else{
	continue;
      }
    }

    Iterator<Integer> it = goalCls.iterator();
    while(it.hasNext()){
      pms.addAll(traceEres(it.next(), tmpMap, currentMaxClauseNumber));
    }
    return pms;
  }

  static HashSet<Integer> traceEres(int clsNum, HashMap<String, Clause> trace, int limit){
    HashSet<Integer> nums = new HashSet<Integer>();
    ArrayList<Integer> stack = new ArrayList<Integer>();
    //stack.add(trace.get(String.valueOf(clsNum)).number);
    stack.add(clsNum);
    //System.out.println("trace:limit:"+limit);
    while(stack.size()!=0){
      Clause cls = trace.get(String.valueOf(stack.remove(0)));
      if(cls==null){
	continue;
      }
      if(cls.number<=limit){/* no need to trace */
	nums.add(cls.number);
      }else{/* need to trace more */
	stack.addAll(cls.getParents());
      }
    }
    return nums;
  }

  static ArrayList<String> addERES(BufferedReader br, String firstLine) throws Exception{
    ArrayList<String> eres = new ArrayList<String>();
    eres.add(firstLine);
    String line = null;
    while(true){
      line = br.readLine();
      if(line.contains("##ERES:")){
	if(line.contains("successful")){
	  eres.add(line);
	}else{
	  return null;
	}
	break;
      }else{
	eres.add(line);
      }
    }
    return eres;
  }

  static void ignoreLines(int num, BufferedReader br) throws Exception{
    lineNum=lineNum+num;
    for(int i=0; i<num; i++){
      br.readLine();
    }
  }
  static void printStringList(ArrayList<String> list){
    System.out.println();
    for(int i=0; i<80; i++){
      System.out.print("*");
    }
    System.out.println();
    int size = list.size();
    for(int i=0; i<size; i++){
      System.out.println(list.get(i));
    }
  }

  static void addStatisics(BufferedReader br, String firstLine) throws Exception{
    lineNum=lineNum+15;
    statistics.add(firstLine);
    for(int i=0; i<15; i++){
      String line = br.readLine();
      if(i==2 && 
	  (line.contains("Satisfiable") || line.contains("Not")) ) {
	  foundProof = false;
      }
      statistics.add(line);
    }
  }
}

class DB{
  final static boolean display = false;
  final static void o(Object o){
    if(display) System.out.print(o);
  }

  final static void ol(Object o){
    if(display) System.out.println(o);
  }
}
