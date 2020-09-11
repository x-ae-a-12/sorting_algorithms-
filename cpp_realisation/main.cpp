#include<iostream>

using namespace std;

class Sorter {
public:
    int simple_sorter (long int * array, int size) {
        bool flag = true;
        while (flag) {
            flag = false;
            for (int i = 0; i < size; i++) {
                if (array[i] > array[i+1]) {
                    int current = array[i];
                    array[i] = array[i+1];
                    array[i+1] = current;
                    flag = true;
                } else {
                    continue;
                }
            }
        }
        return * array;
    }
};

int main() {
    unsigned int size;
    cout << "Enter array size: " << endl;
    cin >> size;
    cout << endl;
    long int array[size];
    cout << "Input numbers: " << endl;
    for (int i = 0; i < size; i++) {
        cin >> array[i];
    }
    cout << endl;
    Sorter sorter;
    sorter.simple_sorter(array, size);
    cout << "Sorted array: " << endl;
    for (int i = 0; i < size; i++) {
        cout << array[i] << ' ';
    }
    cout << endl;
    cin.get();
    return 0;
};
