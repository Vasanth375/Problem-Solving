#include<stdio.h>
#include<math.h>
void main()
{
    int ar[]= {10, 20, 20, 10, 10, 30, 50, 10, 20};

    int match=0;
   
    int count=sizeof(ar)/sizeof(ar[0]);
    // printf("%d",count);
    for (int i = 0; i < count; i++)
    {
       for (int j = i+1; j < count; j++)
       {
          if (ar[i]==ar[j])
          {
            match++;
            break;
          }
        //break;
       }
       
    }
    printf("%d",match);
    printf("%d",sqrt(count));
}