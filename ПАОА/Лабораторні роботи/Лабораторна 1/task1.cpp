#include <iostream>
#include <stdlib.h> 
#include <time.h>  

int** create_matrix()
{
  int** matrix = new int *[3];

  for(int i = 0; i < 3; i++)
    matrix[i] = new int [3];
  
  return matrix;
}

void fill_matrix(int** matrix)
{
  for(int i = 0; i < 3; i++)
  {
    for(int j = 0; j < 3; j++)
    {
      matrix[i][j] = rand() % 50;
    }
  }
}

void delete_matrix(int** matrix)
{
  for(int i = 0; i < 3; i++)
    delete [] matrix[i];
  
  delete [] matrix;
}

void print_matrix(int** matrix)
{
  for(int i = 0; i < 3; i++)
  { 
    for(int j = 0; j < 3; j++)
    {
      std::cout << matrix[i][j] << ' ';
    }
    std::cout << '\n';
  }
}

int find_determinant(int** matrix)
{
  return matrix[0][0] * matrix[1][1] * matrix[2][2] +
  matrix[1][0] * matrix[2][1] * matrix[0][2] +
  matrix[0][1] * matrix[1][2] * matrix[2][0] -
  matrix[0][2] * matrix[1][1] * matrix[2][0] -
  matrix[0][0] * matrix[2][1] * matrix[1][2] - 
  matrix[2][2] * matrix[1][0] * matrix[0][1];
}

int main() {
  srand(time(0));
  int** matr = create_matrix();
  fill_matrix(matr);
  print_matrix(matr);
  std::cout << find_determinant(matr);
  delete_matrix(matr);
  return 0;
}