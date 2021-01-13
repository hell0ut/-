#include <iostream>
#include <stdlib.h> 
#include <time.h>  

int* create_array(int size)
{
  int* arr = new int [size];

  for(int i = 0; i < size; i++)
    arr[i] = rand() % 50;
  
  return arr;
}

int find_max(int* arr, int size, int low, int hight)
{ 

  if(hight == low)
  {
    return arr[low];
  }
  else{
    int mid = low + (hight - low)/2;
    
    int value1 = find_max(arr, size, low, mid);
    int value2 = find_max(arr, size, mid + 1, hight);
    
    if(value1 > value2)
      return value1;
    else
      return value2;
  }
}

void print_array(int* arr, int size)
{
  for(int i = 0; i < size; i++)
   std::cout << arr[i] << ' ';
  std::cout << '\n';
}

int main() {
  srand(time(0));
  int size = 10;
  int* arr = create_array(size);
  print_array(arr, size);
  std::cout << find_max(arr, size, 0, size - 1);
}