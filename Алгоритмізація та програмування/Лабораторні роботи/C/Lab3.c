#include <stdio.h>
#include <math.h>
int main() {
float s = 1 , x, a = 1, eps1 = 0.01, eps2 = 0.000001, b = 4; 
scanf("%f", &x);
int n = 1;
do
{
	a = a * ((b - 3) / b) * x;
	b = b + 4;
	s = s + a;
	n = n + 1;
	
} while (fabs(a) > eps1);
printf("S=%.11f n=%d eps=%f ", s, n, eps1);
float s1 = pow((1-x), -0.25);
printf("s1=%.11f\n", s1);
s = 1 , a = 1, n = 1, b = 4; 
do
{
	a = a * ((b - 3) / b) * x;
	b = b + 4;
	s = s + a;
	n = n + 1;
	
} while (fabs(a) > eps2);
printf("S=%.11f n=%d eps=%f ", s, n, eps2);
float s2 = pow((1-x), -0.25);
printf("s2=%.11f\n", s1);
return 0;
}
