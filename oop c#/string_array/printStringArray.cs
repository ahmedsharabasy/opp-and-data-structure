using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace string_array
{
    class printStringArray
    {
        string[] content;

        public printStringArray(string[] content)
        {
            this.content = content;
        }

        public string getStrintArray(string seperator)
        {
            string strintarr = "";
            foreach (string s in content)
            {
                strintarr += s + seperator;
            }
            return strintarr;
        }
        public void printStrArr(string sererator)
        {
            Console.WriteLine(getStrintArray(sererator));
        }
             

    }
}
