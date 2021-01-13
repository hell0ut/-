#include <stdio.h>
#include <math.h>


int main () {

	float a, b, c, x, y;
	scanf("%f %f %f", &a, &b, &c );
	x = pow(2, pow(b, 4)) + pow(3, a * b);
	y = fabs(a - b) * (1 + pow(sin(c),2) / (a + b)) / (exp(fabs(a - b)) + a / 2); 
	printf("\n x=%f y=%f", x, y);

	return 0;
}

