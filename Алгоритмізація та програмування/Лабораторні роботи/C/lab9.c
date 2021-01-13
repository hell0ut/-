#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>
struct Pupils_data {
	char surname[50];
	int mark;
};

void input(struct Pupils_data *data, int size) {
	int i, temp1;
 	char temp[50];
	for (i = 0; i < size; i++) {
		scanf("%s", temp);
		strcpy( data[i].surname, temp);
		scanf("%d", &temp1);
		data[i].mark = temp1;
	}
}

void print(struct Pupils_data *data, int size) {
	int i;
	for (i = 0; i < size; i++) {
		printf("%s - " ,data[i].surname);
		printf("%d" ,data[i].mark);
		if (i == size - 1) {
			printf(".\n");
		}
		else {
			printf(", ");
		}
	}
}
 int main() {
 	int mark, size, size1, i;
 	int surname;
 	scanf("%d", &size);
	struct Pupils_data data1[size];
	input(data1, size);
	print(data1, size);
	scanf("%d", &mark);
	for(i = 0; i < size; i++) {
		if (mark == data1[i].mark) {
			printf("%s\n", data1[i].surname);
		}
	}
	return 0;
 }
