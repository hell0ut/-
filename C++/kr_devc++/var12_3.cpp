#include <iostream>
#include <math.h> 

/*Насікан Дмитро ДА-93 repl.it*/

int factorial(int n)
{
  if(n > 1)
      return n * factorial(n - 1);
  else
      return 1;
}

float recursive_sum(int n, int x)
{
  if(n > 1)
  {
  return pow(x, n)/factorial(n) + recursive_sum(n - 1, x);
  }
  else if(n == 1)
  {
    return x;
  }
}

int cycle_factorial(int n)
{
  int num = 1;
  for(int i = 1; i <= n; i++)
  {
    num *= i;
  }
  return num;
}

float cycle_sum(int n, int x)
{
  float sum = x;
  while(n > 1)
  {
    float local_sum = pow(x, n) / cycle_factorial(n);
    sum += local_sum;
    n--;
  }
  return sum;
}

int main() {
  int n, x;
  std::cout << "Уведіть n та x.\n";
  std::cin >> n;
  std::cin >>x;
  float rec_sum = recursive_sum(n, x), cy_sum = cycle_sum(n, x);
  std::cout << "Рекурсивно обчислена сума ряду:\n" << rec_sum << "\nІтераційно обчислена сума ряду:\n" << cy_sum;
  return 0;
}
