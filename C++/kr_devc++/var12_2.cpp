#include <iostream>
#include <stdlib.h>
#include <string>
#include <vector>

/*Насікан Дмитро Юрійовий ДА-93 repl.it*/

using namespace std;

char** make_words(string line)
{
  std::vector<string> words;

  while(true) // виокремлюємо слова
  { 
    int index;
    index = line.find(' ');
    if(index == -1)
    {
      words.push_back(line);
      break;
    }
    words.push_back(line.substr(0, index));
    line.erase(0, index + 1);
  }

  char **words_array = new char* [words.size()];
  for(int i = 0; i < words.size(); i++)
  {
    words_array[i] = new char [words[i].size()];
  }

// розміщуємо їх у рядках масиву
  for(int i = 0; i < words.size(); i++)
  {
    for(int j = 0; j < words[i].size(); j++)
    {
      words_array[i][j] = words[i][j];
    }
  }

  for(int i = 0; i < words.size(); i++)
  {
    for(int j = 0; j < words[i].size(); j++)
    {
      cout << words_array[i][j] << " ";
    }
    cout << "\n";
  }

  return words_array;
}

int main() {
  string line;
  getline(cin, line);
  char **words;
  words = make_words(line);
  return 0;
}
