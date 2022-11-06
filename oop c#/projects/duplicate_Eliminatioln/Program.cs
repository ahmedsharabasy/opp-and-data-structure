using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace duplicate_Eliminatioln
{
    class Program
    {
        static void Main(string[] args)
        {
            int counter = 0;
            bool numberin = false;
            int number = 0;
            int[] numbers = new int[5];

            while (counter < 5)
            {
                numberin = false;
                Console.WriteLine("Enter a number between 10 and 100:");
                number = Convert.ToInt32(Console.ReadLine());


                while (number < 10 || number > 100)
                {
                    Console.WriteLine("Enter a number between 10 and 100:");
                    number = Convert.ToInt32(Console.ReadLine());
                }

                for(int i=0;i<numbers.Length;i++)
                {
                    if (number == numbers[i])
                        numberin = true;
                }
                if (!numberin)
                    numbers[counter] = number;

                Console.WriteLine("distinct number is: ");
                foreach (int element in numbers)
                {
                    if (element >= 10)
                        Console.WriteLine(element +" " );

                }
                counter++;
            }
        }
    }
}
