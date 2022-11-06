using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace polymorphism_تعدد_الاشكال
{
    class Program
    {
        static void allIam(person pall)
        {
            pall.Iam();

        }


        static void Main(string[] args)
        {
           

            person p = new person();
            customer c = new customer();
            Employee e = new Employee();

            //p.Iam();
            //c.Iam();
            //e.Iam();
            allIam(p);
            allIam(c);
            allIam(e);

            Console.ReadKey();
        }

        class person
        {
            public virtual void Iam()
            {
                Console.WriteLine("Iam a person");
            }
        }

        class customer:person
        {
            public override void Iam()
            {
                Console.WriteLine("Iam a customer");
            }
        }

        class Employee : person
        {
            public override void Iam()
            {
                Console.WriteLine("Iam a Employee");
            }
        }


    }
}
