using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheretance
{
    class person
    {
        public person(string type = "person", bool isrun = true)
        {
            if (isrun)
            {
                Console.WriteLine("*****new " + type + "*****");         //construyctor inherted
            }
        }
        //public person() { Console.WriteLine("new" + this.GetType().Name); }    نفس الى فوق بس من غير boolean


        private string _name;
        private string _adress;
        private string _phone;

        public string name
        {
            get { return _name;}
            set { _name = value; }       //  returnال
        }

        public string adress
        {
            get { return _adress; }
            set { _adress = value; }
        }

        public string phone
        {
            get { return _phone; }
            set { _phone = value; }
        }


        private string _persondata()
        {
            return name + "\n" + adress + "\n" + phone;
        }

        public string persondata()
        {
            return _persondata();
        }
        public string persondata(string addition)                           //overloading
        {
            return _persondata()+"..."+addition;                            //overloading
        }
                                                                             //cverloading
        public string persondata(string addition,string seperator)             //overloading
        {
            return _persondata().Replace("\n",seperator) + "..." + addition;   //overloading
        }


        public void printdata()
        {
            Console.WriteLine(persondata());
        }






         public void printover()
        {
            Console.WriteLine("person");           //overread 
        }

    }
}
