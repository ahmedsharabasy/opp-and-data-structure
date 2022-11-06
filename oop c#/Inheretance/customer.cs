using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Inheretance
{
    class customer:person                //    عملية الوراثة
    {
        public customer() :base("customer",false) { }             //constructor inherted
        
        



        private string _shipmentAdress;

        public string shipmentadress
        {
            get { return _shipmentAdress; }
            set { _shipmentAdress = value; }
        }

       public string Shepment()
        {
            return persondata() + "\n" + shipmentadress;
        }

        public void printShipmentData()
        {
            Console.WriteLine(Shepment());
        }
    }
}
