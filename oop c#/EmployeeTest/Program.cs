using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmployeeTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Employee e1 = new Employee("ahmed", "Elsharabasy", 3000);
            Employee e2 = new Employee("mohamed", "fayed", 4000);

            Console.WriteLine("employee 1 first name is " + e1.fname);
            Console.WriteLine("employee 1 last name is " + e1.lname);
            Console.WriteLine("employee 1 salary is " + e1.salary);

            Console.WriteLine();

            Console.WriteLine("employee 2 first name is " + e2.fname);
            Console.WriteLine("employee 2 last name is " + e2.lname);
            Console.WriteLine("employee 2 salary is " + e2.salary);

            Console.WriteLine();

            Console.WriteLine("rasing 10%");
            e1.salary = e1.salary + e1.salary * .1m;
            Console.WriteLine("new salary is " + e1.salary);


        }
    }
}
