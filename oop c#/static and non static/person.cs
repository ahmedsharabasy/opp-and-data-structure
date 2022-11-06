using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace static_and_non_static
{
    class person
    {
        public static int id;
        public static string name;
        

        public static void printdata()
        {
            Console.WriteLine(id + ";;;" + name);
        }

    }
}
