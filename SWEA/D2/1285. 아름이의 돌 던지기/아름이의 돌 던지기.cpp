#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int main(){
    int T, N;
    vector<int> peoples;
    cin >> T;

    for (int test_case = 1; test_case <= T; test_case++){
        cin >> N;

        peoples.resize(N);
        int min = 1000001;
        for (int i = 0; i < N; i++){
            cin >> peoples.at(i);

            if (min > abs(peoples.at(i))){
                min = abs(peoples.at(i));
            }
        }

        int count = 0;
        for (int i = 0; i < N; i++){
            if (abs(peoples.at(i)) == min)
                count++; 
        }

        cout << "#" << test_case << " " << min << " " << count << "\n";
    }

    return 0;
}