#include<stdio.h>
#include<stdlib.h>
#define max 100
int check(int a[max][max], int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (a[i][j] == 1) {
                for (int k = 1; k < n; k++) {
                if(a[i][j]==a[i+k][j]) {
                return 0;
            }   if( a[i][j]==a[i][j+k]) {
                return 0;    
            }   if(a[i+k][j+k]==a[i][j]) {
                return 0;
            }
                }
            }
        }
    }
    return 1;
}

int main () {
    int n;
    int a[max][max];
    scanf("%d",&n);
    for(int i =0;i<n;i++) {
        for(int j=0;j<n;j++) {
            scanf("%d",&a[i][j]);
        }
    }
    printf("%d",check(a,n));
}