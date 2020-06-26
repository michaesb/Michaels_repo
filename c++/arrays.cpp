#include <iostream>
#include <typeinfo>
#include <vector>
#include <cmath>
#include <iomanip>
#include <stdio.h>

using namespace std;

class testlists{
private:
  int data[10]{0,1,2,3,4,5,6,7,8,9};
public:
  int get(int i){
    return data[i];
  }
};

class testlist{
private:
  int capacity = 10;
  int *data = new int[capacity];
  int size = 0;
public:
  int get(int i){
    return data[i];
  }
  void append(int n){
    data[size] = {n};
    size +=1;
  }
};


int run_example(){
    int myarray[3] = {10,20,30};

    for (int i=0; i<3; ++i){
      ++myarray[i];
    }
    for (int elem : myarray){
      cout << elem << '\n';
    }
    int *array = new int[10];
    for (int i= 0; i< 10; i++){
      array[i] = 1;
    }
    //just an example I found from the web
}
int main() {
    testlist object;
    for (int i= 0; i< 9; i++){
        object.append(i);
    }
    for (int i= 0; i< 8; i++){
        cout << object.get(i) << endl;
    }
    return 0;
}

/* g++ firstcode -o run_code -std=c++11 */
