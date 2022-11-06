using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace two_dimintional_array_test
{
    class Program
    {
        static void Main(string[] args)
        {
            int[,,] array = new int[2, 8, 7];                                                    // one dimentional array
            System.Console.WriteLine(array);

            //int[,] array2D = new int[,] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };              two dimntional array
            //System.Console.WriteLine(array2D[2,1]);

            //int[,] array2Da = new int[4, 2] { { 1, 2 }, { 3, 4 }, { 5, 6 }, { 7, 8 } };          two dimentional array محدده
            //System.Console.WriteLine(array2Da[1, 0]);

            //int[,,] array3D = new int[,,] { { { 1, 2, 3 }, { 4, 5, 6 } },                      //  three dimentional array
            //                     { { 7, 8, 9 }, { 10, 11, 12 } } };
            //System.Console.WriteLine(array3D[1, 1, 2]);

            for (int i=1;i<=array.Length; i++)
            {
                Console.WriteLine(i);
            }


            Console.ReadKey();
        }
    }
}
