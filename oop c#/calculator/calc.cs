using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace calculator
{
    class calc
    {
        public double number1 ;
        public double number2 ;
        public char c;

        public calc(double number1, double number2,char c)
        {
            this.number1 = number1;
            this.number2 = number2;
        }

        public double add()
        {
            return number1 + number2;
        }

        public void printadd()
        {
            Console.WriteLine("sum of number =" + add());
        }

        public double sub()
        {
            return number1 - number2;
        }

        public void printsub()
        {
            Console.WriteLine("subtract of numbers =" + sub());
        }

        public double multiplication()
        {
            return number1 * number2;
        }

        public void printmulti()
        {
            Console.WriteLine("multyplication of numbers =" + multiplication());
        }

        //calculate sum of items in array
        public int sumIntArray(int[] numbers)
        {
            int sum = 0;
            foreach (int n in numbers)
            {
                sum += n;
            }
            return sum;
        }

        public void printSumIntArr(int[] numbers)
        {
            Console.WriteLine("sum of array =" + sumIntArray(numbers));
        }





        public int[] getClcTowArrays(int[] arr1, int[] arr2, char opea)
        {
            if (arr1.Count() != arr2.Count())
            {
                Console.WriteLine("Erorr: Array1 count not equal Array2 count");
                return new int[] { 0 };    //لازم نرترن مصفوفة       
            }
            else
            {
                int[] arr3 = new int[arr1.Count()];
                for (int i = 0; i < arr3.Count(); i++)
                {
                    if (opea == '+')
                    {
                        arr3[i] = arr1[i] + arr2[i];
                    }
                    else if (opea == '-')
                    {
                        arr3[i] = arr1[i] - arr2[i];
                    }
                    else if (opea == '*')
                    {
                        arr3[i] = arr1[i] * arr2[i];
                    }
                    else if (opea == '/')
                    {
                        if (arr2[i] == 0) arr2[i] = 1;
                        arr3[i] = arr1[i] / arr2[i];
                    }
                    else
                    {
                        if (arr2[i] == 0) arr2[i] = 1;
                        arr3[i] = arr1[i] % arr2[i];
                    }
                }
                return arr3;
            }

        }
        
        public void printResultArr(int[] arr1,int[] arr2, char opea)
        {
            foreach (int i in getClcTowArrays(arr1, arr2, opea))
            {
                Console.WriteLine(i);
            }
        }

    }
}
