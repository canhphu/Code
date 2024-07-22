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
    int n,i,k,j;
    int count=0;
    int a[max][max];
    scanf("%d",&n);
    for(int i =0;i<n;i++) {
        for(int j=0;j<n;j++) {
            scanf("%d",&a[i][j]);
        }
    }
    for(int i =0;i<n;i++) {
        for(int j=0;j<n;j++) {
            if(a[i][j]==1) {
                count++;
            }
        }
    }
    if(count>=n) {
        printf("-1");
        exit(-1);
    } else if(check(a,n)==0) {
        printf("-1");
        exit(-1);
    }
    while(i<n) {
        try1:
        i++;
        while(j<n) {
            try2:
            j++;
            if (a[i][j] == 0) {
                for(int k=0;k<n;k++) {
                if(a[i+k][j]==1) {
                    goto try1;
            }  if(a[i][j+k]==1) {
                goto try2;
            }   if(a[i+k][j+k]==1) {
                goto try1;
            } 
             
                }
            }
           
        }
        a[i][j]=1;
            goto next; 
    }
    next:
    for(int i =0;i<n;i++) {
        printf("\n");
        for(int j=0;j<n;j++) {
            printf("%d ",a[i][j]);
        }
    }
    
}