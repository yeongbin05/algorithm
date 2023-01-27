#include <stdio.h>

int main(){
    int a;
    int Arr[10];
    scanf("%d %d %d",&Arr[0],&Arr[1],&Arr[2]);
    for(int j=0; j<2;j++)
    {
    for(int i=0; i<2 ; i++)
    {
        if(Arr[i]<Arr[i+1])
        {
            a=Arr[i];
            Arr[i]=Arr[i+1];
            Arr[i+1]=a;
                        
        }      
    }
    }
    printf("%d",Arr[1]);
    return 0;
}