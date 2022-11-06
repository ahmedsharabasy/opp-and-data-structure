using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Employee_data
{
    class Employee
    {
        public int id;
        public string name;
        public string adress;
        public string phone;
        public double salary;
        public const double tax = 0.1;
        
        public double getNetSallary()
        {
            double netsall = salary - (salary * tax);
            return netsall;
        }

        public string getemloyeedata()
        {
            string alldata = "employee name: " + name + "\n" + "emloyee id: " + id + "\n" +
                "empolyee adress: " + adress + "\n" + "employee phone: " + phone + "\n" +
                "employee salary; " + salary + "\n" + "net salary: " + getNetSallary() + "\n";
            return alldata;
        }

        public void printEmpoyeeData()
        {
            Console.WriteLine(getemloyeedata());

        }
    }
}
