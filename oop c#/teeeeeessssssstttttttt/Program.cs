using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace teeeeeessssssstttttttt
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter the base number:");
            var basenumber = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine("Enter an exponent:");
            var exponent = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine(power(basenumber,exponent));

        }
        public static int power(int basse,int expo)
        {
            int Result = 1;
            for(int i=0;i<expo;i++)
            {
                Result *= basse;
            }
            return Result;

        }
    }
}
