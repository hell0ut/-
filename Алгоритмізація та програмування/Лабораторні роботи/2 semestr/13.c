/*
12. Створити текстовий файл, який містить додатні, від'ємні, нульові числа та довільні символи.
Визначити кількість додатних, від'ємних, нульових чисел та слів у кожному рядку файлу.
Записати отримані значення з відповідними коментарями в інший текстовий файл.
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

int generate_num()
{
  int number = rand() % 51;
  int sign = rand() % 2;
  if(sign == 1)
  {
    number *= -1;
  }
  return number;
}
int length(int range)
{   int len;
    while(1)
    {
        len = rand() % range + 1;
        if(len != 0)
        {
            break;
        }
    }
    return len;
}

void count(int* count_array, char* str)
{
	char *word;
	word = strtok(str, "_");
	int num;
	while(word != NULL)
	{	
		num = atoi(word);
		if(num == 0)
		{
			if(*word == '0')
				*count_array++;
			else
				*(count_array + 3) += 1;
		}
		else if(num > 0)
			*(count_array+1) += 1;
		else
			*(count_array + 2) += 1;
		word = strtok(NULL, "_");
	}
}
void count1(int* count_array, char* str)
{
  char nums[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
  char *pointer; 
  int space = 32, i;
  while(1)
  {  
    int determined = 0;
    pointer = strchr(str, space);
    if(pointer == NULL)
    {
      break;
    }
    if(*(pointer + 1) != ' ')
    {
        if(*(pointer + 1) == '0')
      {
        determined = 1;
        *count_array += 1;
      }
      if(determined == 0 && *(pointer + 1) == '-')
      {
        determined = 1;
        *(count_array + 2) += 1;
      }
      for(i = 0; i < 5; i++)
      {
        if(determined == 0 &&  *(pointer + 1) == nums[i])
        {
          determined = 1;
          *(count_array+1) += 1;
          break;
        }
      }
      if(determined == 0)
      {
        *(count_array + 3) += 1;
      }
    }
    pointer++;
    str = pointer;  
  }
}

int main() 
{  
  srand(time(NULL));
  FILE *file;
  char name[] = "main_file.txt", alphabet[50] = "abcdeifghrtyuopxzcvnm";
  file = fopen(name, "w");
  int i = 0, j = 0, stop = rand() % 15, len = length(15);
  while(i < len)
  {  
    j = 0;
    int len1 = length(15);
    while(j < len1)
    {
      int number, sign, word_or_num, num;
      word_or_num = rand() % 2; //neiai ?e ?enei
      if(word_or_num == 1)
      {//aaia?aoi? ?enae
        num = generate_num();
        fprintf(file, "_%d", num);
      }
      else
      {  int size = length(7);
        char word[size];
        int h, *pointer;
        for(h = 0; h < size; h++)
        {
          int ran = rand() % 23;
          word[h] = alphabet[ran];
        }
        fprintf(file, "_%s", word);
      }
      j++;
    }
    if(i != len - 1)
    {
    fprintf(file, "\n");
    }
    i++;
  }
  fclose(file);
  char string[100], result[] = "result_file.txt";
  file = fopen(name, "r");
  FILE *result_file;
  result_file = fopen(result, "w");
  int string_count = 0;
  while(!feof(file))
  {  
    fgets(string, 100, file);
    string_count++;
    int *str_result, count_array[4] = {0, 0, 0, 0}; // 0 - 0, 1 - aiaaoi?, 2 - a?a'?ii?, 3 - neiaiee
    count(count_array, string);
    fprintf(result_file, "Рядок %d: нулів - %d, додатніх чисел - %d, від'ємних чисел - %d,слів - %d\n", string_count, count_array[0], count_array[1], count_array[2], count_array[3]);
  }
  return 0;
}
