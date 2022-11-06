using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Round_method
{
    class Program
    {
        static void Main(string[] args)
        {
            double x = 0;
            Console.WriteLine("Enter number to be rounded or negative number to quite this application:");
            x = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("the number to round is " + x);
            double y = 0;
            //y = Math.Round(x);
            y = round(x,1);
            Console.WriteLine("number rounded to the nearset integer " + y);

            y = round(x, 10);
            Console.WriteLine("number rounded to nearest tenth decimal place: " + y);
            
            y = round(x, 100);
            Console.WriteLine("number rounded to nearest hundredth decimal place: " + y);

            y = round(x, 1000);
            Console.WriteLine("number rounded to nearest thousands decimal place: " + y);

            Console.ReadKey();
        }

        static double round(double x,int decm_place)
        {
            double y = 0;
            y = Math.Floor(x*decm_place+0.5)/decm_place;
            return y;

        }

    }
}
