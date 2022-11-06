using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace dateTest
{
    class date
    {
        public int month { get; set; }
        public int day { get; set; }
        public int year { get; set; }

        public date(int month,int day,int year)
        {
            this.month = month;
            this.day = day;
            this.year = year;
        }

        public void DisplayData()
        {
            Console.WriteLine(month + "/" + day + "/" + year);
        }
            
    }
}
