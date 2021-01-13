using System;
using System.Diagnostics;
using System.IO;

namespace PAOA_Lab2
{
    class Program
    {
        static void PrintArray(int[] arr)
        {
            foreach (int num in arr)
            {
                Console.Write(num + ' ');
            }

            Console.WriteLine('\n');
        }

        static int GetNewGap(int currentGap)
        {
            double newGap = currentGap / 1.3;
            newGap = Math.Floor(newGap);

            if (newGap <= 1)
                return 1;

            return (int)newGap;
        }


        static void CombSort(int[] arr, int length, out int numOfComparisons, out int numOfReplacements, out double timeOfWork)
        {
            numOfComparisons = 0;
            numOfReplacements = 0;

            int gap = length;
            bool swapped = true;

            Stopwatch timeCounter = new Stopwatch();

            timeCounter.Start();
            while (gap > 1 || swapped)
            {
                swapped = false;
                gap = GetNewGap(gap);
                for(int i = 0; i < length - gap; i++)
                {
                    numOfComparisons++;

                    if (arr[i] > arr[i + gap])
                    {

                        int temp = arr[i];
                        arr[i] = arr[i + gap];
                        arr[i + gap] = temp;

                        swapped = true;
                        numOfReplacements++;
                    }
                }
            }

            timeCounter.Stop();

            timeOfWork = timeCounter.Elapsed.TotalMilliseconds;
        }

        static void SaveResults(string fileName, int numOfComparisons, int numOfReplacements, double timeOfWork, string comment)
        {
            File.AppendAllText(fileName, $"Файл {comment}:\nПорівнянь - {numOfComparisons}\nОбмінів - {numOfReplacements}\nЧас роботи - {timeOfWork} мс\n\n");
        }

        static int[] GetArrayFromFile(string fileName)
        {
            string allText = File.ReadAllText(fileName);
            string[] allNums = allText.Split(',');
            int[] result = new int[allNums.Length];

            for(int i = 0; i < allNums.Length; i++)
            {
                result[i] = int.Parse(allNums[i]);
            }

            return result;
        }

        static double getAverageTime(double[] arr)
        {
            double time = 0;
            for(int i = 0; i < arr.Length; i++)
            {
                time += arr[i];
            }

            return time / arr.Length;
        }


        static void Main(string[] args)
        {
            string filePath = @"D:\Університет\2 курс\ПАОА\Лабораторні роботи\Лабораторна робота 2\Код\PAOA Lab2\";
            string resultsFileName = filePath + "results.txt";

            string[] files = { 
                "constant100",
                "constant1000",
                "constant10000",
                "random100",
                "random1000",
                "random10000",
                "reversed100",
                "reversed1000",
                "reversed10000",
                "sorted100",
                "sorted1000",
                "sorted10000"
            };

            foreach(string file in files)
            {

                int comparisons, swaps, cycleSize = 100;
                double time;

                double[] timeArr = new double[cycleSize];

                for(int i = 0; i < cycleSize; i++)
                {
                    int[] arr1 = GetArrayFromFile(filePath + file + ".txt");

                    CombSort(arr1, arr1.Length, out comparisons, out swaps, out time);
                    timeArr[i] = time;
                }

                int[] arr = GetArrayFromFile(filePath + file + ".txt");
                CombSort(arr, arr.Length, out comparisons, out swaps, out time);

                
                SaveResults(resultsFileName, comparisons, swaps, getAverageTime(timeArr), file);
            }
        }
    }
}
