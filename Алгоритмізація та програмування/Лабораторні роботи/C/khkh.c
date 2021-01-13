#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main(){
	int size;
	scanf("%d", &size);
	int given_array[size], i;
	for (i = 0; i < size; i++) {
		given_array[i] = rand() % 200;
	}
	for (i = 0; i < size; i++) {
		printf("%d ", given_array[i]);
	}
	printf("\n");
	int counter = 0;
	float temp;
	for (i = 0; i < size; i++) {
		temp = (float)given_array[i];
		if (sqrtf(temp) == round(temp)) {
			int temp1 = (int)sqrt(given_array[i]);
			if (temp1 % 2 == 0) {
				counter++;
				printf("%d ", given_array[i]);
				printf("%d ", counter);
			}
		}
	}
	
	return 0;
}
