// UVA 10041 - Vito's Family
#include <stdio.h>
#include <stdlib.h>

int main()
{
    int r, s, si;
    for(int i = 0; i < r; i++)
    {
        scanf("%d", &s);
        int *arr = (int *)malloc(sizeof(int) * s);
        for(int j = 0; j < s; j++)
        {
            scanf("%d", &si);
            arr[j] = si;
        }

        // sort the array
        for(int j = 0; j < s; j++)
        {
            for(int k = j + 1; k < s; k++)
            {
                if(arr[j] > arr[k])
                {
                    int temp = arr[j];
                    arr[j] = arr[k];
                    arr[k] = temp;
                }
            }
        }
        int sum = 0;

        for(int j = 0; j < s; j++)
        {
            sum += abs(arr[j] - arr[s / 2]);
        }
        printf("%d\n", sum);
    }

}