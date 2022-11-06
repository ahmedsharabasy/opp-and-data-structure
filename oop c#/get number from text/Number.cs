using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace get_number_from_text
{
    class Number
    {
        public static int getNumberOnly(string text)
        {
            string newText = "";
            foreach(char c in text.ToCharArray())
            {
                if ((c == '0') || (c == '1') || (c == '2') || (c == '3') || (c == '4') || (c == '5') || (c == '6') || (c == '7') || (c == '8') || (c == '9'))
                {
                    newText += c;
                }
                
            }
            if (newText == "") newText = "0";
            int newint = Convert.ToInt32(newText);
            return newint;
s

        }

        public static void printNumberOnly(string text)
        {
            Console.WriteLine(getNumberOnly(text));
        }
    }
}
