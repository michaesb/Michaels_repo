#include <iostream>
#include <typeinfo>
#include <vector>
#include <cmath>
#include <iomanip>

struct node{
    int data;
    node* next;
    node* prev;
};

node obj;




int main() {
    node* head; //marks the front
    node* tail; // marks the end
    node* n;
    n = new node; //n points at the new node
    n->data = 1; // give it value one to data (value)
    n->prev = nullptr; // points to nothing
    head = n; // points to same obj as n
    tail = n; // points to same obj as n
    ////////////////////////////////////////
    n = new node; // new pointer location
    n->data = 2; // new data
    n->prev = tail; // point to the previous (tail)
    tail ->next = n; // tail next points to n
    tail = n

    return 0;
}
/* g++ firstcode -o run_code -std=c++11 */
