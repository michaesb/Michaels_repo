#include <iostream>
#include <typeinfo>
#include <cmath>
using namespace std;

const double g = 9.81;

struct Position {
    double x;
    double y;
};

class Wave {
public:
      double Lambda;
      double frequency;
      double period;

      Wave(double l) {
          Lambda = l;

      }

        double velocity(){
            return (Lambda);
        }
};

int main() {
    Wave obj(1.);
    Position particle{100, 2.2};
    cout << obj.velocity() << endl;

    return 0;
}

class Circle{
    public:
        Circle(double r):
            radius(r)
        {
        }
        double re1(){
            return (1);
        }
    private:
        double radius;
};



// g++ firstcode -o run_code -std=c++11
