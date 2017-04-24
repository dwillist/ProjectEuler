import java.util.Arrays;

class Problem52{
  private static int[] digitMap(long number){
    int[] to_return = new int[10];
    String str = Long.toString(number);
    for(int i = 0; i < str.length(); ++i){
      to_return[(int)str.charAt(i) - '0']++;
    }
    return to_return;
  }
  public static void main(String[] args){
    long i = 1;
    while(true){
      //System.out.println(i);
      int current[] = digitMap(i);
      if(Arrays.equals(current,digitMap(i*2))
      && Arrays.equals(current,digitMap(i*3))
      && Arrays.equals(current,digitMap(i*4))
      && Arrays.equals(current,digitMap(i*5))
      && Arrays.equals(current,digitMap(i*6))){
        System.out.println(i);
        return;
      }

      i = i+1;
    }
  }
}
