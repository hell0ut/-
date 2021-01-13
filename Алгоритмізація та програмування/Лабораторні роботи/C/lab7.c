#include <stdio.h>
#include <math.h>

int main() {
	int k = 1, n, counter = 0;
	while(k < 100) {
		if (pow(sin(3 * k + 5), 2) - cos(pow(k, 2) - 15) < 0.25) {
			counter += 1;
			n = k;
		} 
		k *= 2;
	}
	printf("%d (k = %d)", counter, n);
return 0;
}
