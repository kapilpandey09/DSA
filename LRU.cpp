class Node {
public:
    int key, val;
    Node* prev;
    Node* next;

    Node(int k, int v) {
        key = k;
        val = v;
        prev = next = nullptr;
    }
};

class LRUCache {
private:
    int cap;
    unordered_map<int, Node*> mp;

    Node* head;
    Node* tail;

    void removeNode(Node* node) {
        Node* p = node->prev;
        Node* n = node->next;

        p->next = n;
        n->prev = p;
    }

    void insertAtEnd(Node* node) {
        Node* p = tail->prev;

        p->next = node;
        node->prev = p;

        node->next = tail;
        tail->prev = node;
    }

public:
    LRUCache(int capacity) {
        cap = capacity;

        head = new Node(-1, -1);
        tail = new Node(-1, -1);

        head->next = tail;
        tail->prev = head;
    }

    int get(int key) {

        if (mp.find(key) == mp.end())
            return -1;

        Node* node = mp[key];

        removeNode(node);
        insertAtEnd(node);

        return node->val;
    }

    void put(int key, int value) {

        if (mp.find(key) != mp.end()) {

            Node* node = mp[key];
            node->val = value;

            removeNode(node);
            insertAtEnd(node);

            return;
        }

        if (mp.size() == cap) {

            Node* lru = head->next;

            removeNode(lru);

            mp.erase(lru->key);

            delete lru;
        }

        Node* node = new Node(key, value);

        insertAtEnd(node);

        mp[key] = node;
    }
};