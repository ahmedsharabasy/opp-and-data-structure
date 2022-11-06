using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Employee_data
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee emp = new Employee();

            Console.WriteLine("Enter your name: ");
            emp.name = Console.ReadLine();

            Console.WriteLine("Enter your id: ");
            emp.id = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter your adress: ");
            emp.adress = Console.ReadLine();

            Console.WriteLine("Enter your phone: ");
            emp.phone = Console.ReadLine();

            Console.WriteLine("Enter your salary: ");
            emp.salary = Convert.ToDouble(Console.ReadLine());

            emp.printEmpoyeeData();
            Console.ReadKey();
        }
    }
}
