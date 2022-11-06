using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EmployeeTest
{
    class Employee
    {
        public string fname { get; set; }    
        public string lname { get; set; }
        public decimal monthlySalary;

        public Employee(string fname,string lname,decimal monthlySalary)
        {
            this.fname = fname;
            this.lname = lname;
            this.monthlySalary = monthlySalary;
        }

        public decimal salary
        {
            get { return monthlySalary; }
            set { if (value >= 0) salary = value; }
        }

        //encapsulation of method
        private string printdata()    //مخفية
        {
            return "ali";
        }
        public string printdata2()  //ظاهرة وجواها المستخبية الى محدش يعرف يوصلها
        {
            return printdata();
        }
    }
}
