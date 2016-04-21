#include <iostream>
#include <math.h> 
using namespace std;


class Solution {
public:
  bool isPalindrome(int x) {
    /*
        if(x<0){
            return false;
        }
        if(x<10){
            return True;
        }
        int size = 0;
        while(x/((int)pow(10,size+1)) != 0){
          size = size+1;
        }
        
        while(size >= 1){
          if (x%10 != x/((int)pow(10,size))){
            return false;
          }
          x = (x/10)%((int)pow(10,size-1));
          size = size-2;
        }

        return true;
    */
        if (x<0){
          return false;
        }
        if (x < 10){
          return true;
        }

        int size = 0;
        int rands = 0;
        int result = 0;
        bool final ;

        size = (int)log10(x);

        rands = (size+1)/2;
        for(int i = 0 ; i < rands ;i++){
          result = result * 10 + x%10;
          
          x = x/10;
        }

        if (size%2 == 0){
          x = x /10;
        }
        return x==result;


    }
};



int main () {
  Solution test;
  
  cout << "result: " << test.isPalindrome(11) << endl;
  cout << "";
  return 0;
}