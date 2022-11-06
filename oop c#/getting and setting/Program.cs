using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace getting_and_setting
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee emp1 = new Employee();

            emp1.ID= 800167472;
            emp1.Name = "Ahmed";
            emp1.Salary = 3000;

            emp1.printdata2();

            Console.ReadKey();
        }
    }
}
