#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

void main(){
    char *ptr;
    char *dangerptr;
    
    ptr = (char *)malloc(5*sizeof(char));
    dangerptr = (char *)malloc(5*sizeof(char));

    printf("Address of Pointer:%d\n", ptr);
    printf("Address of Danger Pointer:%d\n", dangerptr);
    
    printf("Enter String:");
    gets(ptr);
    printf(ptr);

    system(dangerptr);
}
