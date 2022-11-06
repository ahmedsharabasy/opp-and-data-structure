using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            
                /*for (int i = 0; i < 10; i++)
                   {
                       for (int j = 0; j < 10; j++)
                       {                   
                           Console.WriteLine("*");

                       }
                       Console.WriteLine();
                   }
                   Console.ReadKey();*/

                var stars = from I in Enumerable.Range(0, 10)
                            from y in Enumerable.Range(0, 10)
                            select new { I, y };

                foreach (var star in stars)
                {
                    Console.WriteLine("*");                   
                }
            Console.ReadKey();
        }
    }
}
