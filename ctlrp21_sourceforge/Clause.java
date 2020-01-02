import java.util.*;
import java.io.*;
import java.util.regex.*;

public class Clause{
  int number = 0;
  String content = null;
  //ArrayList<Integer> parents = new ArrayList<Integer>();
  private TreeSet<Integer> parents = new TreeSet<Integer>();
  String origin = null;
  boolean used = false;

  final static String INP = "Inp";
  final static String RES = "Res";
  final static String RED = "Red";
  final static String ERES1 = "ERES1";
  final static String ERES2 = "ERES2";
  public static void main(String[] args) throws Exception{
  }

  public TreeSet<Integer> getParents(){
    return parents;
  }

  public void addParents(Collection<Integer> pms){
    parents.addAll(pms);
    /* To avoid loops when trace the proof, remove itself from its parents. */
    parents.remove(this.number);
  }

  public String toString(){
    StringBuffer sb = new StringBuffer();
    sb.append(this.number+"["+this.origin+":");
    Iterator<Integer> it = this.parents.iterator();
    while(it.hasNext()){
      sb.append(it.next()+",");
    }
    sb.append("] || "+this.content);
    return sb.toString();
  }
  public Clause(){}

  public void updateContent(String clsStr){
    if(this.content!=null) return;
    int index = clsStr.indexOf('|');
    this.content = clsStr.substring(index+3);
  }

  public Clause(int number, String clsStr){
    this.number = number;
    int index = clsStr.indexOf('|');
    this.content = clsStr.substring(index+3);

    if(clsStr.contains(Clause.INP)){
      this.origin = Clause.INP;
    }else if(clsStr.contains(Clause.RES)){
      this.origin = Clause.RES;
    }else{
      this.origin = Clause.RED;
    }

    int index1 = clsStr.lastIndexOf(':'), index2 = clsStr.lastIndexOf(']');
    //System.out.println(clsStr);
    String parStr = clsStr.substring(index1+1, index2);
    if(Character.isDigit(parStr.charAt(0))){
      //System.out.println(parStr);
      String[] parArr = parStr.split(",");
      for(int i=0; i< parArr.length; i++){
	int onePar = (int) Math.floor(Double.parseDouble(parArr[i]));
	this.parents.add(onePar);
	//System.out.println(onePar);
      }
    }

  }
}

