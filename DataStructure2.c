#include <stdio.h>

int main()
{
  

    char string1[80];
    char string2[80];
    char *a = string1; 
    char *b = string2; 

    int i = -1;

    printf("Enter a string: ");
    scanf("%s", string1);

   
    while(*a)
    {
        a++;
        i++; 
    }

   
    for(i;i >= 0;i--)
    {
       
        a--; 
        *b = *a; 
        b++;
     
    }
    
    *b = '\0'; 
    b = string2; 
    while(*b)
    {
        *a = *b;
        a++;
        b++;
    }


    printf("\nResult: %s ", string1);

    return 0;
}
