#include <iostream>
#include <fstream>
#include <cstdlib>

int main()
{
	int *a = new int[10];
	
	for(int i = 0; i < 10; i++)
	{
		a[i] = rand() % 10;
		std::cout << a[i] << " ";
	}
	
	std::ofstream file("c://binfiles//num1.bin", std::ios::binary);
	if(file.is_open())
		std::cout << "opened\n";
	for(int i = 0; i < 10; i++)
	{
		file.write((char*)&a[i], sizeof(int));
	}
	file.close();
	
	int b[10];
	std::ifstream file1("c://binfiles//num1.bin", std::ios::binary);
	file1.read((char*)b, sizeof(b));
	for(int i = 0; i < 10; i++)
	{
		std::cout << b[i] << " ";
	}
	
	return 0;
}
