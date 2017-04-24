import java.io;
import java.util.ArrayList;

class Problem53{
  private static int winner(String hands){
    String[] tolkens = hands.split(" "); //first 5 are to player 1 next 5 to player 2
    String[] P1 = Array.copyOfRange(tolkens,0,4);
    String[] P2 = Array.copyOfRange(tolkens,5,10);
  }


  public static void main(String args[]){
    Reader file_reader = new FileReader("/Users/danielthornton/Dropbox/code/Practice/projectEuler/51-75/54.txt");
    int data = file_reader.read();
    ArrayList strArray = new ArrayList();
    String current;
    while(data!= -1){
      if(data != '\n'){
        current = current + data
      }
      else{
        strArray.add(current);
        current = "";
      }
    }
    if(current){
      strArray.add(current);
    }
    // now we should have read our entire list

  }
}
