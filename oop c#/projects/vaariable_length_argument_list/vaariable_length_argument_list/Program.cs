using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace vaariable_length_argument_list
{
    class Program
    {
        static void Main(string[] args)
        {
            int num1 = 56;
            int num2 = 178;
            int num3 = 354;
            int num4 = 17;
            int num5 = 55;

            Console.WriteLine("sum of{0} and{1} is {2}", num1, num2, product(num1, num2));
            Console.WriteLine("sum of{0} and{1} and{2} is {3}", num1, num2, num3, product(num1, num2, num3));
            Console.ReadKey();
        }
        public static int product(params int[] numbers)
        {
                int total = 0;
                 foreach(var i in numbers)
                 {
                    total += i;
                 }
                return total;
        }
    }
}


