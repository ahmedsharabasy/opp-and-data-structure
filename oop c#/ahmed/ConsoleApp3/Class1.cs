using System;
using System.Collections.Generic;
using System.Text;



    class Grade_Book_Teast

    {
        public static void Main  (string[] args)
        {
            Grade_Book mygradebook = new Grade_Book();
            Console.WriteLine("please enter the course name");
            string nameOfcourse = Console.ReadLine();
            Console.WriteLine();

            mygradebook.DisplayMessage(nameOfcourse);




        }


    }

