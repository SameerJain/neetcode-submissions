class DynamicArray
{
public:
    int lastIdx, arrSize, capacity;
    int *arr;
    DynamicArray(int cap)
    {
        lastIdx = -1;
        arrSize = 0;
        capacity = cap;
        arr = new int[capacity];
    };

    int get(int i)
    {
        return arr[i];
    }

    void set(int i, int n)
    {
        arr[i] = n;
    }

    void pushback(int n)
    {
        if (arrSize == capacity)
        {
            resize();
        }
        arr[++lastIdx] = n;
        arrSize++;
    }

    int popback()
    {
        arrSize--;
        return arr[lastIdx--];
    }

    void resize() {
        int newCapacity = 2 * capacity;
        int *newArr = new int[newCapacity];
        
        for (int i = 0; i < arrSize; i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
        capacity = newCapacity;
    }

    int getSize()
    {
        return arrSize;
    }

    int getCapacity()
    {
        return capacity;
    }
};