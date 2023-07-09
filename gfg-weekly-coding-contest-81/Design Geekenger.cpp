//User function Template for C++
class Node {
    public: 
    Node* next;
    Node* prev;
    string num;
    deque<string> chat;
    
    Node(string num) {
        this -> num = num;
    }
    
    void add_data(string s) {
        chat.emplace_back(s);
        if (chat.size() > 20) {
            chat.pop_front();
        }
    }
};

class DoublyLinkedList {
    public: 
    Node *head;
    DoublyLinkedList() {
        head = new Node("null");
        head->next = head->prev = head;
    }
    
    void append(Node *node) {
        Node *tail = head->prev;
        tail->next = node;
        node->prev = tail;
        node->next = head;
        head->prev = node;
    }
    
    void remove(Node *node) {
        Node *prev = node->prev;
        prev->next = node->next;
        node->next->prev = prev;
    }
    
    Node* pop() {
        Node *item = head->next;
        remove(item);
        return item;
    }
};

class Geekenger
{
public:

    // Version 1: Doubly linked list
    // TC: O(|message|), SC: O(|message| * |number|)
    unordered_map<string, Node*> data;
    int screenSize;
    DoublyLinkedList list;
    Geekenger(int screenSize){
        // Constructor
        data.clear();
        this -> screenSize = screenSize;
    }

    void send(string number, string message){
         // Send Message to "number"
         newMessage(number, message);
    }

    void receive(string number, string message){
        // Receive message from "number".
        newMessage(number, message);
    }
    
    void newMessage(string number, string message) {
        if (data.find(number) != data.end()) {
            list.remove(data[number]);
        } else {
            data[number] = new Node(number);
        }
        list.append(data[number]);
        if (data.size() > screenSize) {
            Node *item = list.pop();
            int res = data.erase(item -> num);
        }
        data[number]->add_data(message);
    }
    
    vector<string> findLastKMessage(string number, int K){
        // Return list of lask K messages in the chat 
        // of "number" arranged in top to down order.

        vector<string> ans;
        if (data.find(number) == data.end() || data[number] -> chat.size() < K) {
            ans.emplace_back("ERROR");
        } else {
            int m = data[number] -> chat.size();
            for (int i = 0; i < K; i++) {
                ans.emplace_back(data[number]->chat[m - K + i]);
            }
        }
        return ans;
    }

    
};