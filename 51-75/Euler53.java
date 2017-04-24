import java.math.BigInteger;

class Problem53{
  public static void main(String[] args){
    BigInteger[][] nCkArray = new BigInteger[101][101];
    int largeCount = 0;
    BigInteger mil = new BigInteger("1000000");
    for(int i = 0; i < 101;++i){
      for(int j = 0; j <= i; ++j){
        if(j == 0 || j == i){
          nCkArray[i][j] = new BigInteger("1");
        }
        else{
          nCkArray[i][j] = nCkArray[i-1][j-1].add(nCkArray[i-1][j]);
        }
        if(nCkArray[i][j].compareTo(mil) == 1 ){
          largeCount++;
        }
      }
    }
    System.out.println(largeCount);
  }
}
