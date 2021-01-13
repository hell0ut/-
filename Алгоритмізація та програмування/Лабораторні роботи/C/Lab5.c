#include <stdio.h>
#include <math.h>
void sort(int *arr, int size){
  int i, j;
  for (i = 0; i < size - 1; i++) {
      for (j = 0; j < size - 1; j++) {
        if (arr[j] < arr[j + 1]) {
          int x = arr[j];
          arr[j] = arr[j + 1];
          arr[j + 1] = x;
        }
      }
    }
}

int main() {
	int size, k, i, j, z = 0;
	//створюємо матриці розміру, що задається
	scanf("%d", &size);
	int matrix_1[size][size], matrix_2[size][size];
	// заповнюємо матрицю 1 елементами.
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++){
			scanf("%d", &matrix_1[j][i]);
		}
	}
	// заповнюємо матрицю 2 елементами.
	for (i = 0; i < size; i++) {
		for (j = 0; j < size; j++){
			scanf("%d", &matrix_2[j][i]);
		}
	}
	printf("matrices:\n");
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", matrix_1[j][i]);
			}
			else {
				printf("%d)", matrix_1[j][i]);
			}
		}
		printf("\n");	
	}
	printf("\n");
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", matrix_2[j][i]);
			}
			else {
				printf("%d)", matrix_2[j][i]);
			}
		}	
		printf("\n");
	}
	printf("\n");
	// переписуємо елементи діагоналі матриці 1 в масив
	int array_1[size], array_2[size];
	for (i = 0; i < size; i++) {
		array_1[i] = matrix_1[i][i];			
	}
	// переписуємо елементи діагоналі матриці 2 в масив
	for (i = 0; i < size; i++) {
		array_2[i] = matrix_2[i][i];			
	}
	// сортуємо масиви та записуємо нові діагоналі
	sort(array_1, size);
	for (i = 0; i < size; i++) {
		matrix_2[i][i] = array_1[i];			
	}
	sort(array_2, size);
	for (i = 0; i < size; i++) {
		matrix_1[i][i] = array_2[i];			
	}
	printf("Sorted diagonals:\n");
	for (i = 0; i < size; i++) {
		printf("%d ", array_1[i]);
	}
	printf("\n");
	for (i = 0; i < size; i++) {
		printf("%d ", array_2[i]);
	}
	/*for (i = 0; i < size; i++) {
		printf("%d ", array[i]); 	
	} */
	// виводимо матриці
	printf("\n");
	printf("Sorted metrices:\n");
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", matrix_1[j][i]);
			}
			else {
				printf("%d)", matrix_1[j][i]);
			}
		}
		printf("\n");	
	}
	printf("\n");
	for (i = 0; i < size; i++) {
		printf("(");
		for (j = 0; j < size; j++) {
			if(j < size - 1) {
				printf("%d ", matrix_2[j][i]);
			}
			else {
				printf("%d)", matrix_2[j][i]);
			}
		}	
		printf("\n");
	}
	
return 0;
}

