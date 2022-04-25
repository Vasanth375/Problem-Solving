
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main() {

    long long ArrayA[100][100],ArrayB[100][100],sum[100][100]={0};
    int i,j,n,m;
    scanf("%d %d",&n,&m);
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          scanf("%lld",&ArrayA[i][j]);  
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          scanf("%lld",&ArrayB[i][j]);  
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          sum[i][j]=ArrayA[i][j]+ArrayB[i][j]; 
        }
    }
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
          printf("%lld ",sum[i][j]);
            if(j==m-1)
                printf("\n");
        }
    }
}