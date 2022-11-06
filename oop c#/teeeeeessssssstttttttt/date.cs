using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace teeeeeessssssstttttttt
{
    class clc
    {
        public int number1;
        public int number2;

        public clc(int number1,int number2)
        {
            this.number1 = number1;
            this.number2 = number2;

        }
        public int add()
        {
             return number1 + number2;
        }

        public void printadd()
        {
            Console.WriteLine("sum of two numbers =" + add());
        }
        public int subtract()
        {
            return number1 - number2;
        }

        public void printsubtract()
        {
            Console.WriteLine("sum of two numbers =" + subtract());
        }
        public int multiply()
        {
            return number1 * number2;
        }

        public void printmultiply()
        {
            Console.WriteLine("sum of two numbers =" + multiply());
        }
        public int divide()
        {
            if (number2 == 0) return number2 = 1;
            else
                return number1 % number2;
        }



        public void printdivide()
        {
            Console.WriteLine("sum of two numbers =" + divide());
        }
        //////////////////////////////////////////////////////////////////////////
        public int sumintarr(int[] arr)
        {
            int sum = 0;
            foreach (int i in arr) 
            {
                sum += i;
            }
            return sum;
        }
        public void printsumintarr(int[] arr)
        {
            Console.WriteLine("sum of array =" + sumintarr( arr));
        }




    }
}
