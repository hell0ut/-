
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include <string.h>
#include <stdbool.h>

int main() {
  int size;
  printf("������ ������� ��� � ������.\n");
  scanf("%d", &size);
  char string[size], bad_str[5] ="abcd", final_str[size];
  printf("������ �������.\n");
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
