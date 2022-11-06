using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheretance
{
    sealed class Employee:person                   //sealed تمنع الوراثة            
    {

        public Employee(string type = "Employee") : base(type) { }         //constructor inherted



        public string EmployeeID;

     
        public void printEmployeeData()
        {
            Console.WriteLine(persondata() + "\n" + EmployeeID);
        }


        
        /// ////////////////////////////////////////////////////////////////////////////////////////////
                                      //(Over read)
        public new void printover()                  // new  حاطينا
        {
            Console.WriteLine("Employee");           //overread (اعادة كتابة او التعديل فى ال method)
        }

    }
}
