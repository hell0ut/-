/*
Перевірити, чи є заданий рядок зашифрований за алгоритмом, що наведено у варіанті 11.
Якщо так - видати розшифрований рядок, якщо ні - вивести повідомлення про помилку і вивести перше помилкове слово.
Можливі символи - прописні українські букви; символ-роздільник '_'.
Приклади:
Зашифрований рядок:
НА__ДВВВВООООООРРРРІ_ОССССІІІІІІННННЬ
Результат розшифровки:
НА_ДВОРІ_ОСІНЬ
Зашифрований рядок:
НА_ДВВВВООООРРРРІ_ЗИИИМММА
Результат розшифровки:
Помилка, слово 'ДВВВВООООРРРРІ' не є зашифрованим.
(Варіант 11 :Маємо деяке речення, усі слова якого розділені символами підкреслення ('_').
Використовуючи трикутник Паскаля, зашифруйте вихідне речення за наступним правилом:
"	із пропозиції виділяється чергове слово;
"	із трикутника Паскаля вибирається рядок з номером, рівним числу букв у слові;
"	k-а буква вихідного слова заміняється на набір однакових букв у кількості, зазначеній у k-му стовпці обраного рядка трикутника Паскаля.
 )
*/
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
  }
  arr[number_of_words - 1] = sometext;
}

string decipher(string word)
{ 
  int size = 1;
  char symbol = word[0];
  for(int i = 0; i < word.size(); i++)
  {
    if(word[i] != symbol)
    {
      size++;
      symbol = word[i];
    }
  }
  int h = word.size() - size, waste[h], j = -1;
  symbol = word[0];
  string new_word = word;
  //cout << size << "\n";
  for(int i = 1; i < word.size(); i++)
  { 
    if(word[i] != symbol)
    {
      symbol = word[i];
    }
    else if(word[i] == symbol)
      {
        j++;
        waste[j] = i;
      } 
  }
  string temp = word;
  for(int i = 0; i < h; i++)
      temp[waste[i]] = '+';
  for(int i = 0; i < h; i++)
  {
    int index = temp.find('+');
    temp.erase(index, 1);
  }
  return temp;
}

void pascal_row(int counter, int *arr)
{
    for(int i = 0; i < counter; i++)
    {
      arr[i] = fact(counter - 1)/(fact(i)*fact((counter - 1) - i));
    }
}

string cipher(string word, int* pascal_array)
{ 
  string output_word;
  for(int i = 0; i < word.size(); i++)
  {
    output_word += string(pascal_array[i], word[i]);
  }
  return output_word;
}

int ciphered_correctly(string* cipher_arr, string* input_arr, int size)
{
  bool ciphered_correctly = true;
  int i;
  for(i = 0; i < size; i++)
  {
    if(cipher_arr[i] != input_arr[i])
    { 
      ciphered_correctly = false;
      break;
    }
  }
  if(!ciphered_correctly)
    return i;
  else
    return -1;
}

using namespace std;
int main()
{
  string input;
  cout << "Введіть речення для розшифрування:\n";
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
  convertion(input, words_array, number_of_words); // виділяємо слова
  string normal_words[number_of_words];
  for(int i = 0; i < number_of_words; i++)
    normal_words[i] = decipher(words_array[i]);
  string cipher_words[number_of_words];
  for(int i = 0; i < number_of_words; i++)
  {
    int pascal_nums[normal_words[i].size()];
    pascal_row(normal_words[i].size(), pascal_nums);
    cipher_words[i] = cipher(normal_words[i], pascal_nums);
    normal_words[i] = decipher(normal_words[i]);
    //string() веде себе якось дивно, модифікуючи початковий масив
  }
  int index = ciphered_correctly(cipher_words, words_array, number_of_words);
  if(index == -1)
  {
    cout << "Розшифроване речення:\n";
    string output; 
    for(int i = 0; i < number_of_words - 1; i++)
      output += normal_words[i] + '_';
    output += normal_words[number_of_words - 1];
    cout << output;
  }
  else
  {
    cout << "Помилка дешифрування: " <<"Слово "<< words_array[index] << " зашифроване неправильно";
  }
}
