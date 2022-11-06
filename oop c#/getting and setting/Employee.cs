using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace getting_and_setting
{
    class Employee
    {                                              // عمل عملية  encapsulation
        private int id;
        private string name;
        private double salary;

        public int ID                               // عملية  properity
        {                                           //  تستخدم هذه العملية لاخفاء الvariables  الاصلية عن الclasses الاخري بينما تظهر الفاريبالز الى جواها فى الكلالسز الاخرى
            get { return id; }                    
            set { id = value; }
        }    

        public string Name
        {
            get { return name; }      //بترجع القيمه الى اليوز دخلها عشان اشتغل عليها فى الفانكشن
            set { this.name = value; }   //بتعطى  القيمه الى هتظهر للمسخدم ويمكن التعديل فيها واستخدام كوندشنز
        }
        
        public double Salary
        {
            get { return salary; }
            set { salary = value; }
        }
        private string printdata()
        {
            return id + "\n" + name + "\n" + salary;
        }

        public void printdata2()
        {
            Console.WriteLine(printdata());
        }

        

    }
}
