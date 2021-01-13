#include <iostream>

int* create_random_array(int size)
{
  int* A = new int [size];

  for(int i = 0; i < size; i++)
    A[i] = rand() % 15;
  
  return A;
}

void print_array(int* A, int size)
{
  std::cout << "Згенерований масив: ";

  for(int i = 0; i < size; i++)
    std::cout << A[i] << " ";
  
  std::cout << "\n";
}

int inner_find_max(int* A, int size, int low, int high)
{
  if(high == low)
    return A[high];

  int middle = low + (high - low) / 2;

  int left_max = inner_find_max(A, size, low, middle);
  int right_max = inner_find_max(A, size, middle + 1, high);

  if(left_max > right_max)
    return left_max;
  else
    return right_max;
}

int find_max(int* A, int size)
{
  return inner_find_max(A, size, 0, size - 1);
}

int main() 
{
srand(time(0));

int size = 10;
int* arr = create_random_array(size);

print_array(arr, size);

std::cout <<"Максимальний елемент - "<< find_max(arr, size); 
}