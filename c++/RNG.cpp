#include <iostream>
#include <typeinfo>
#include <vector>
#include <cmath>
#include <iomanip>
#include <stdio.h>
//using namespace std;
#include <random>
#include <chrono>
#include <functional>

int main() {
    //int seed = 17865;
    /*
    std::mt19937 mt_rand(time(nullptr));
    std::cout << time(0) << std::endl;
    std::cout << mt_rand() << std::endl;
    */
    //mt19937::result_type seed = chrono::high_resolution_clock::now().time_since_epoch().count();
    //std::mt19937 mt_rand(seed);
    //mt19937::result_type seed = mt_rand(seed);
    //auto real_rand = bind(std::uniform_real_distribution<double>(0,1), mt19937(seed));
    std::mt19937::result_type seed = std::chrono::high_resolution_clock::now().time_since_epoch().count();
    auto real_rand = bind(std::uniform_real_distribution<double>(0,1),std::mt19937(seed));
    for (int i =0; i<6; i++){
      std::cout << real_rand(0) << '\n';
    }
    return 0;
}

/* g++ firstcode -o run_code -std=c++11 */
