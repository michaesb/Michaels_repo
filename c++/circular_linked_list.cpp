
struct Node{
    int data;
    Node* next;
    Node* prev;
};
class CircLinkedList{

private:
    int size_;
    Node* head;
    Node* tail;

public:

    CircLinkedList(){
        head = nullptr;
        tail = nullptr;
        size_ = 0;
    }
    CircLinkedList(std::vector<int> n){
      /*take a vector as input and append it to a list.*/
      head = nullptr;
      tail = nullptr;
      size_ = 0;
      for (int i = 0; i <n.size(); i++){
         append(n[i]);
         size_ ++;
      }
   }

    ~LinkedList(){
        Node* temp = head;
        Node* deleter = head;
        while (temp != nullptr){
            deleter = temp;
            temp = temp-> next;
            delete deleter;
        }
    }

    int length(){
        return size_;
    }
    void append(int q){
        /*append an integer to the linked list.*/
        Node* new_node;
        if (size_ == 0){
            new_node = new Node; // new_node points to a new node alpha.
            new_node-> data = q; // assign value 1 to the node alpha.
            new_node -> prev = new_node; // prev pointer in alpha points to nothingness
            new_node -> next = new_node;  //next pointer in aplha points to nothingness
            head = new_node; // points to alpha. Will constantly point at the beginning node
            tail = new_node; // points to alpha
            }
        else {
            new_node = new Node; // New node beta with new_node pointing at Beta
            new_node -> data = q; //data in beta node assigned to q
            new_node -> prev = tail; // prev pointer in Beta points at Alpha
            new_node -> next = nullptr; // next points to nullptr
            tail -> next = new_node; // next pointer in alpha points at beta
            tail = new_node; // tail now points at Beta.
            }

        size_ ++;
        }
    void insert(int val, int index){
        /* insert a value in a specific spot in the list*/
        if (index>size_+1){
            throw std::out_of_range("index error");
        }

        if (index == 0){ // if it is inserted at the head
            Node* alpha = head; // creating a pointer directed at the old head node
            Node* inserted_node = new Node; //creating new node
            inserted_node -> data = val; // inserting value in node
            inserted_node -> next = alpha; // points to the previous head
            inserted_node -> prev = nullptr; // points to nothing
            head = inserted_node; //setting new head
            alpha -> prev = inserted_node; // linking the new node on the list
        }
        if (index == size_+1){ // if it is inserted at the tail
            Node* alpha = tail; // creating a pointer directed at the old tail node
            Node* inserted_node = new Node; // creating the inserted node
            inserted_node -> data = val; //inserting value in the new node
            inserted_node -> next = nullptr; // points to nothing
            inserted_node -> prev = alpha; //points to the old tail node
            tail = inserted_node; // new tail
            alpha -> next = inserted_node; // alpha now points to the new tail node
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
            Node* beta = alpha -> next; // points to the node after the inserted node
            Node* inserted_node = new Node; // New node beta with n pointing at beta
            inserted_node -> data = val; //data in inserted_node assigned to val
            inserted_node -> prev = alpha; // prev pointer in inserted_node points at alpha
            inserted_node -> next = beta; // next pointer in inserted_node points at beta
            alpha -> next = inserted_node; // next points to nullptr
            beta -> prev = inserted_node; // next pointer in alpha points at beta
            }

        size_ ++;
    }
    void remove(int index){
        /* remove one element in the list*/
        if (index>size_){
            throw std::out_of_range("index error");
        }

        if (index == 0){
            Node* remover = head; //the remover node to deleted
            Node* beta = head -> next; //the remover node to deleted
            beta -> prev = nullptr; // beta is disconnected from remover node
            delete remover;
            head = beta; //
        }
        else if (index ==size_){
            Node* remover = tail; //the remover node to deleted
            Node* alpha = tail -> prev; //the remover node to deleted
            alpha -> next = nullptr; // beta is disconnected from remover node
            delete remover;
            tail = alpha;
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
    int pop(int index){
        /* remove one element in the list*/
        if (index>size_){
            throw std::out_of_range("index error");
        }
        int value;
        if (index == 0){
            Node* remover = head; //the remover node to deleted
            Node* beta = head -> next; //the remover node to deleted
            beta -> prev = nullptr; // beta is disconnected from remover node
            value = remover -> data; //extracting the data
            delete remover;
            head = beta; // assinging new head node
        }
        else if (index ==size_){
            Node* remover = tail; //the remover node to deleted
            Node* alpha = tail -> prev; //the remover node to deleted
            alpha -> next = nullptr; // alpha is disconnected from remover node
            value = remover -> data; //extracting the data
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
            value = remover -> data; //extracting the data
            delete remover;
            alpha -> next = beta;
            beta -> prev = alpha;
        }
        size_ --;
        return value;
    }
    int pop(){
        /* remove one element in the list*/
        Node* remover = tail; //the remover node to deleted
        Node* alpha = tail -> prev; //the remover node to deleted
        alpha -> next = nullptr; // alpha is disconnected from remover node
        int value = remover -> data; //extracting the data
        delete remover;
        tail = alpha; //assinging new tail node
        size_ --;
        return value;
    }
    int operator[](int index)const {
        /*make it possible to get values using the format obj[i].*/
        if(index>size_||index<0){
            throw std::out_of_range("index out of range");
        }
        Node* alpha = head; // will point to the node before inserted node
        for (int i =0; i<index; i++){
            alpha = alpha -> next;
        }
        return alpha-> data;
    }
    int &operator[](int index){
        /*make it possible to assign values using the format obj[i] = a.*/
        if(index>size_||index<0){
            throw std::out_of_range("index out of range");
        }

        Node* alpha = head;
        for (int i =0; i<index; i++){
            alpha = alpha -> next;
        }
        return alpha-> data;
    }
    void print(){
        /*print the list in the format [a,b,c,].*/
        Node* temp = head;
        std:: cout << "[ ";
        while (temp != nullptr){
            std::cout << temp-> data <<' ';
            temp = temp-> next;
        }
        std:: cout << " ]" <<"\n";
    }
};
