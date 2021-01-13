#include <iostream>
#include <string>
#include <cstdbool>
#include <cstring>

using namespace std;
int fact(int n) { 
   if ((n==0)||(n==1))
      return 1; 
   else
      return n*fact(n-1);
}

void convertion(string sometext, string* arr, int number_of_words)
{ 
  int low_index = 0;
  for(int i = 0; i < number_of_words - 1; i++)
  {
    int high_index = sometext.find('_');
    arr[i] = sometext.substr(low_index, high_index - low_index);
    sometext.erase(0, high_index + 1);
    cout << sometext<< "\n";
  }
  arr[number_of_words] = sometext;
}

using namespace std;
int main()
{
  string input;
  cin >> input;
  int number_of_words = 1;
  for(int i = 0; i < input.size(); i++)
  {
    if(input[i] == '_')
    {
      number_of_words++;
    }
  }
  string words_array[number_of_words];
  convertion(input, words_array, number_of_words);
  for(int i = 0; i <= number_of_words; i++)
  {
    cout << words_array[i] << i<<"\n";
  }
}

