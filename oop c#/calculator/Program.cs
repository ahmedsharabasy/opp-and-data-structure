using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    class Program
    {
        static void Main(string[] args)
        {
            char c = '+';

            double num1=0;
            double num2=0;
            int[] nums = {5,5,5,5,5,5,5 };
            calc clc1 = new calc(num1, num2,c);
                

            Console.WriteLine("enter number 1: ");
            clc1.number1 = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("enter number 2: ");
            clc1.number2 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("***********************");

            clc1.printadd();
            clc1.printsub();
            clc1.printmulti();

            Console.WriteLine("***********************");

            // clc1.printSumIntArr(nums);
            calc sumarr = new calc(num1,num2,c);
            sumarr.printSumIntArr(nums);
            Console.ReadKey();

            Console.WriteLine("***********************");
            calc cc = new calc(num1, num2,c);

            int[] array1 = { 8, 27, 255, 2, 54525, 4 };
            int[] array2 = { 95, 22545, 415, 5, 545, 4 };
            Console.WriteLine("Enter operation: ");
            cc.c =Convert.ToChar( Console.ReadLine());
            cc.printResultArr(array1, array2, c);
        }
    }
}
