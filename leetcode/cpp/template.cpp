#include <iostream>
using namespace std;


class Solution {
public:
    int reverse(int x) {
       
           int newN =0, left =0;  
            while(x != 0)  
            {  
                 if (newN>214748364 || newN<-214748364) {
                     return 0;
                     break;
                 }
                 left = x%10;  
                 newN = newN*10 + left;  
                 x = x/10;  
            }  
            return newN;  
            
    }
};



int main () {
  Solution test;
  
  cout << "result: " << test.reverse(12315312) << endl;
  cout << "";
  return 0;
}