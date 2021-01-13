#include <stdio.h>
#include <math.h>

int main() {
	int a1 = 1, b1 = 1, n, i;
	scanf("%d", &n);
	//знаходимо всі b і a
	int a_list[n - 1], b_list[n - 1];
	a_list[0] = a1;
	b_list[0] = b1;
	for (i = 1; i < n; i++) {
		a_list[i] = 3 * b_list[i - 1] + 2 * a_list[i - 1];
		b_list[i] = 2 * a_list[i - 1] + b_list[i - 1];
	}
  /*for (i =0; i < n; i++) {
		printf("%d ", a_list[i]);
	}
	printf("\n");
	for (i =0; i < n; i++) {
		printf("%d ", b_list[i]);
	}
  	printf("\n"); */
	//знаходимо факторілали для всіх k
	int j, k = 2, fact, k_fact[n - 1]; 
	k_fact[0] = 1;
	for (i = 1; i < n; i++ ) {
		fact = 1;
		j = k;
		while (j > 1) {
			fact *= j;
			j -= 1;
		}
		k_fact[i] = fact;
		k++;
	}
/*	for (i = 0; i < n; i++) {
		printf("%d ", k_fact[i]);
	}
	printf("\n"); */
	//обчислюємо суму
	int z = 0;
	float sum = 0;
	for (k = 1; k < n + 1; k++) {
		sum += pow(2, k) / ((1 + pow(a_list[z], 2) +pow(b_list[z], 2)) * k_fact[z]);
		z++;
	}
	printf("S=%f", sum);
return 0;
}

