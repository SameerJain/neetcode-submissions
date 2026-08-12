class DynamicArray {
public:

    DynamicArray(int capacity) {

    if(capacity <= 0){
        return;
    }
    
        int length = -1;
        int capacity = capacity;
        int *arr = new int[capacity];
        
    }
    DynamicArray(){};
    int get(int i) {
        
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        
        arr[length++] = n;
    }

    int popback() {
    length--;
    }

    void resize() {

        capacity = capacity * 2;
        

    }

    int getSize() {
    
        return length;
    }

    int getCapacity() {

        return capacity;
    }
};
