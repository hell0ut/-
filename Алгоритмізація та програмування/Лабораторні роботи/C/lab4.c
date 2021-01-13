#include <stdio.h>
#include <math.h>
 int main() {
	int input_array[20];
	int i, j, k = 0;
	for (i = 0; i < 20; i++)
	{
		scanf("%d", &input_array[i]);	
	}
	for (i = 0; i < 20; i++) {
		printf("%d ", input_array[i]);
	}
	int min = input_array[0], index;
	for (i = 0; i < 20; i++)
	{
		if (input_array[i] <= min)
		{
			min = input_array[i];
			j = i;
			k++;
			index = i;
		}
	}
	printf("min=%d, index=%d\n", min, index);
	int x = 0, result_array[20 - k];
	for (i = 0; i < 20; i++)
	{
		if (input_array[i] != min)
		{
			result_array[x] = input_array[i];
		}
		else
		{
			x -= 1;
		}
		x++;
	}
 	for(i = 0; i <= 20 - k; i++)
 	{
 		printf("%d ", result_array[i]);	
	}
	return 0;
 	
 }
