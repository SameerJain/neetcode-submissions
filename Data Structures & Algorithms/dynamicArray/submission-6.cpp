class DynamicArray {
public:

    DynamicArray(int capacity) {
    int lastIdx = -1;
    int arrSize = 0;
    int capacity = capacity;
    int *arr = new int[capacity]
    }

    DynamicArray(){};
    int get(int i) {
        return arr[i]; 
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
    if(length+1 == capacity){
        resize();
    }
    arr[length++] = n;
    }

    int popback() {
    length--;
    }

    void resize() {
        capacity = 2 * capacity;
        int *newArr = new int[capacity];

        for(int i = 0; i < length + 1; i++){
            newArr[i] = arr[i];
        }

        arr = newArr;
    }

    int getSize() {
    return length + 1;
    }

    int getCapacity() {
    return capacity;
    }
};
