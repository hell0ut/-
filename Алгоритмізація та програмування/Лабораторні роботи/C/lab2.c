#include <stdio.h>
#include <math.h>
int main() {
	
	float a = 5.1, x = -2, y, dx = 0.2;
	while( x <= 2 ) {	
		if(x <= 1) {		
			y =	1.7 * pow(cos(x),2);	
		}
		if(1 < x && x < 2) {		
			y = pow(x-4, 2) + a;	
		}
		if (x = 2) {
			y = 5 * tan(x);
		}
		x += dx;
		printf("\ny=%f, x=%1.1f", y, x);
	}
return 0;
}

