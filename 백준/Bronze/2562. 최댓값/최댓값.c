#include <stdio.h>

int main()
{   
    int a = 0;
    int c = 0;
    int j = 0;
    int b[9];
    for (int k = 0; k < 9; k++)
    {
        scanf("%d", &b[k]);
    }
    for (int i = 0; i < 8; i++)
    {
        for (int j = 1; j < 9-i; j++)
        {
            if (b[i] <= b[i+j])
            {
                b[i] = 0;
            }
            else if (b[i] > b[i + j])
            {
                b[i + j] = 0;
            }

        }
        
    }
   
        
            while (b[c] == 0)
            {
                a++;
                c++;
            }
          
        
        

        printf("%d\n%d", b[a], a+1);
        
        return 0;
    }

	


