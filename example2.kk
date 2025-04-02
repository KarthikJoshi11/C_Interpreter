#include<stdio.h>
int main(){
    int j=0;
    int i;
    int k1=2;
   
     //if x=6 printf("Eveb");syntax error
    //char c='c';
     //char c='d';\semantic error
     char d;
     scanf("%c",&d);
     printf("%c\n",d);
    char st[200];
   
    
    scanf("%s",&st);
    printf("%s",st);

    for(i=0;i<184;i++){
        j+=i;
    }
    if(j%2==0){
        printf("\neven\n");
    }
    else{
        printf("odd");
       

    }
    printf("%d",j);
}