using System;
using System.Runtime.InteropServices;

namespace findLargest
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = [5, 56, 123, 31, 23, 1023, 32, 53];
            Console.WriteLine($"{findLargest(numbers)}");
        }

        static int findLargest(int[] nums)
        {
            int largest = 0;
            for (int i = 0; i < nums.Length; i++){
                if (nums[i] > largest){
                    largest = nums[i];
                }
            }

            return largest;
        }
    }
}