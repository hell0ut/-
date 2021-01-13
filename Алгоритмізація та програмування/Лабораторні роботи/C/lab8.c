#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int main() {
	int size;
	scanf("%d", &size);	
	int matrix[size][size], i, j;
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++) {
			matrix[j][i] = rand() % 10;
		}
	}
	int result_matrix[size][size], diagonal_element;
	for (i = 0; i < size; i++) {
		diagonal_element = matrix[i][i];
		for (j = 0; j < size; j++) {
			if (matrix[j][i] > diagonal_element) {
				result_matrix[j][i] = 1;
			}
			else {
				result_matrix[j][i] = 0;
			}
		}
	}
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", matrix[j][i]);
			}
			else {
				printf("%d)", matrix[j][i]);
			}
		}
		printf("\n");	
	}
	printf("\n");
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", result_matrix[j][i]);
			}
			else {
				printf("%d)", result_matrix[j][i]);
			}
		}
		printf("\n");	
	}
	printf("\n");
return 0;
}
