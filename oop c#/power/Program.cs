using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace power
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the base number:");
            var basenumber = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter an exponent:");
            var exponent = Convert.ToInt32(Console.ReadLine());

            var resultCalc = Integerpower(basenumber, exponent);
            Console.WriteLine(resultCalc);
            Console.ReadKey();
        }

        private static int Integerpower (int basenum ,int expo)
        {
            var result = 1;               //حطينا الريزلت =1 عشان جوا الفور مينفعش نضربها فى صفر
            for (int i=0; i<expo; i++)
            {
                result *= basenum;
            }
            return result;
        }
    }
}
