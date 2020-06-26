

struct node{
    int data;
    node* next;
    node* prev;
};

int main {
    node* head // marks the front. to be pointed
    node *tail // marks the tail. to be pointed
    node* n   // a point in between. to be pointed
    n = new node; // n points to a new node. Called f.eks. Per
    n-> data = 1 //  assign value 1 to the node Per.
    n -> prev = NULL // prev pointer in Per points to nothingness
    head = n // points to Per
    tail = n // points to Per
    n = new node; // New node Ingunn with n pointing at Ingunn
    n->data = 2; //data in Ingunn assigned to 2 with the pointer n
    n -> prev = tail // prev pointer in Ingunn points at Per
    tail -> next = n // next pointer in Per points at Ingunn
    tail = n // tail now points at Ingunn.


}





    void pop(int index){
        /* remove one element in the list*/
        if (index>size_){
            throw std::out_of_range("index error");
        }
        if (index == 0){
            Node* remover = head; //the remover node to deleted
            Node* beta = head -> next; //the remover node to deleted
            beta -> prev = nullptr; // beta is disconnected from remover node
            int value = remover -> data; //extracting the data
            delete remover;
            head = beta; // assinging new head node
        }
        else if (index ==size_){
            Node* remover = tail; //the remover node to deleted
            Node* alpha = tail -> prev; //the remover node to deleted
            alpha -> next = nullptr; // alpha is disconnected from remover node
            delete remover;
            tail = alpha; //assinging new tail node
        }
        else {
            Node* alpha; // will point to the node before inserted node
            if (index < size_/2){ // check what is the quickest way to the index is
                alpha = head;
                for (int i=0; i<index-1; i++){
                    alpha = alpha -> next;
                }
            }
            else {
                alpha = tail; // will point to the node before inserted node
                for (int i=0; i<(size_-index+1); i++){
                    alpha = alpha -> prev;
                }
            }
            Node* remover = alpha -> next; // points to the node after the inserted node
            Node* beta = remover -> next;
            delete remover;
            alpha -> next = beta;
            beta -> prev = alpha;
        }
        size_ --;
    }
