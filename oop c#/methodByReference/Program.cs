using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ref2
{
    class Program
    {
        static void printnum(ref int num)
        {
            num = 10;
            Console.WriteLine(num);

        }


        static void Main(string[] args)
        {
            int x = 70;
            Console.WriteLine("x: before using function: "+x);
            printnum(ref x);
            
            Console.WriteLine("x: after using function: "+x);
            Console.ReadKey();
        }
    }
}
