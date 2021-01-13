/*
12. Задано натуральне число n, символи S1, .., Sn. Виключити з цієї послідовності усі групи букв виду "abсd".
*/
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>

int main() {
  int size;
  printf("Уведіть розмір рядка.\n");
  scanf("%d", &size);
  char string[size], bad_str[5] ="abcd", final_str[size];
  printf("Уведіть рядок.\n");
  scanf("%s", string);
  char *pointer, *pointer2;
  while(true) {
    pointer = strstr(string, bad_str);
    if(pointer == NULL) {
      break;
    }
    else {
      pointer2 = pointer;
      pointer2 += 4;
      while(true) {
        *pointer = *pointer2;
        pointer++;
        pointer2++;
        if(strcmp(pointer2, "\0") == 0) {
           *pointer = *pointer2;
           break;
        }
      }
    }
  }
  printf("%s", string);
  return 0;
}
