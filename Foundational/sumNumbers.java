'''
Given a string, return the sum of the numbers appearing in the string, ignoring all other characters. A number is a series of 1 or more digit chars in a row. (Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. Integer.parseInt(string) converts a string to an int.)


sumNumbers("abc123xyz") → 123
sumNumbers("aa11b33") → 44
sumNumbers("7 11") → 18
'''
public int sumNumbers(String str) {
    char []a = str.toCharArray();
    int t = 0;
    int sum = 0;
    int n = str.length();
    int j,l;
    for(int i=0 ; i<n; i++){
      j = i;
      while(j<n && Character.isDigit(a[j])){
        j++;
      }
      if(j!=i){
        l = i;
        t = Integer.parseInt(Character.toString(a[l]));
        l = l+1;
        while(l<j){
          t = t*10+Integer.parseInt(Character.toString(a[l]));
          l++;
        }
        sum = sum+t;
        i=j;
      }
    }
    return sum;
}
