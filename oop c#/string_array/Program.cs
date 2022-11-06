using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace string_array
{
    class Program
    {
        static void Main(string[] args)
        {
            string[] arr = { "a", "b" };
            printStringArray psa =new printStringArray(arr);

            psa.printStrArr(",,\n");
        }
    }
}
