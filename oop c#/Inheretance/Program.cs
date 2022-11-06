using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheretance
{
    class Program
    {
        static void Main(string[] args)
        {
            person p1 = new person();
            p1.name = "Ahmed Khaled Abdo Elaharabassy";
            p1.adress = "damietta";
            p1.phone = "01004094344";
            p1.printdata();
            
            Console.WriteLine(40*'*');

            customer c1 = new customer();
            c1.name = "Mohamed";
            c1.shipmentadress = "sanania";
            c1.phone = "012512151154";
            c1.adress = "zarqa";
            c1.printShipmentData();


            Employee e1 = new Employee();
            e1.EmployeeID = "800167472";
            e1.printEmployeeData();


            ////////////////////////////////////////////////////////////////////////////////////////////
            //  (overloding processing)

            person p2 = new person();
            p2.name = "rhy";
            p2.phone = "015257555";
            p2.adress = "enania";
            Console.WriteLine( p2.persondata("this is person data"));
            Console.WriteLine(p2.persondata("this is person data", "$"));

            Console.WriteLine("************************************");

            //(over read)
            p1.printover();
            e1.printover();
            c1.printover();
            


            /////////////////////////////////////////////////////////////////////////////
            doctor d1 = new doctor();

            Console.WriteLine("//////////////////////////////////////////////////////");

            //////////////////////////////////////////////////////////////////////////////

            student s1 = new student();
            Console.WriteLine(s1.GetType().Name);
            Console.WriteLine(s1.GetType().FullName);   
            Console.WriteLine(s1.GetType().IsClass);
            Console.WriteLine(s1.GetType().BaseType);   //الكلاس الوارث منه 
            Console.WriteLine(s1.GetType().Assembly);
            Console.WriteLine(s1.GetType().Attributes);
            Console.WriteLine(s1.GetType().Namespace);


            StreamWriter sw = new StreamWriter("test.txt");
            Console.WriteLine(sw.GetType().FullName);

            Console.ReadKey();
          
        }
    }
}
