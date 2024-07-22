#include<stdio.h>
#include<stdlib.h>

int main () {
    int n;
    scanf("%d",&n);
    int diem;
    char name[256];
    for(int i=0;i<n;i++) {
        scanf("%s%d",&name,&diem);
        if(diem<4) {
            printf("%s",name);
        }
    }
}