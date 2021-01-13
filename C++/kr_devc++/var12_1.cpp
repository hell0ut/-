#include <iostream>
#include <cstdlib>
#include <ctime>
/*Насікан Дмитро Юрійович repl.it*/
int** matrix_creator(int M, int N)
{
  int **matrix = new int* [M];
  for(int i = 0; i < M; i++)
  {
    matrix[i] = new int [N];
  }
  
  for(int i = 0; i < M; i++)
  {
    for(int j = 0; j < N; j++)
    {
      matrix[i][j] = rand() % 20 + 1;
    }
  }
  return matrix;
}

void print_matrix(int** matrix, int M, int N)
{
  for(int i = 0; i < M; i++)
  {
    for(int j = 0; j < N; j++)
    {
      std::cout << matrix[i][j] << " ";
    }
    std::cout << "\n";
  }
}

int finder(int **matrix, int M, int N)
{
  int count = 0, max_count = -1, row = -1;
  bool flag = false;
  for(int i = 0; i < M; i++)
  {
    count = 0;
    for(int j = 0; j < N; j++)
    {
      if(matrix[i][j] % 2 == 0)
      {
        count++;
      }
    }
    if (count == max_count)
      {
        flag = true;
      }
    else if(count > max_count)
      {
        max_count = count;
        row = i;
        flag = false;
      }
  }
  if(flag == false)
  	return row + 1;
	else
	return M;
	
}

using namespace std;
int main() {
  srand (time(NULL)); 
  cout << "Введіть розміри матриці:";
  int N, M;
  cin >> M;
  cin >> N;
  
  int **matr = matrix_creator(M, N);
  
  print_matrix(matr, M, N);
  int row = finder(matr, M, N);

  cout <<"Найбільше парних чисел в рядку:"<< row;

  for(int i = 0; i < M; i++)
  {
    delete [] matr[i];
  }
  delete [] matr;
}
