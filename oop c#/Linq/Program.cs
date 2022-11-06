using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Linq
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] numbers = { 1, 9, 7, 6, 4, 45, 82, 96, 74 };
            var lessnumber = from number in numbers where number < 9 select number;
            foreach (var item in lessnumber)
                {
                Console.WriteLine(lessnumber);
                }
            Console.ReadKey();

        }
    }
}
