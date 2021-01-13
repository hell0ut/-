
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
int size() {
    int size;
    scanf("%d", &size);
    return size;
}
int* define_matrix(int size) {
    int *matrix, *mtr;
    matrix = (int*) malloc(pow(size,2));
    mtr = matrix;
    int i, rand_num, rand_sign;
    for(i = 0; i < pow(size, 2); i++) {
        rand_num = rand() % 10;
        rand_sign = rand() % 2;
        if (rand_sign == 0) {
            rand_num *= -1;
        }
        *mtr = rand_num;
        mtr++;
    }
    return matrix;
}
void print(int* matrix, int size) {
    int i, counter = 0;
    int *p = matrix;
    for(i = 0; i < pow(size, 2); i++) {
        printf("%d ", *(matrix+i));
        counter++;
        if(counter == size) {
            printf("\n");
            counter = 0;
        }
        //matrix++;
    }
}
int main() {
  srand(time(NULL));
    int s;
    int *matr;
    s = size();
    matr = define_matrix(s);
    print(matr, s);
    return 0;
}




