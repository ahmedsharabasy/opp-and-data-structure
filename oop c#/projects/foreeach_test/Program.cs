using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace foreeach_test
{
    class Program
    {
        static void Main(string[] args)
        { 
            int[] array = { 55, 58, 24, 254, 255, 2 };
            int total = 0;

            foreach (int i in array)
                total += i;
            Console.WriteLine("total of array elements: {0}", total);

        }
    }
}
