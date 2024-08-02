#include<bits/stdc++.h>
using namespace std;
long algo1(int a[], int n) {
    long max = a[0];
    for(int i=0;i<n;i++) {
        for(int j=i;j<n;j++) {
            int s=0;
            for(int k=i;k<=j;k++) {
                s+=a[k];
                max = max<s? s : max;
            }
        }
    }
    return max;
}

int main () {
    int a[] = {1,2,3,4,5};
    int n = sizeof(a)/sizeof(a[0]);
    cout << algo1(a,3);
    return 0;
}