using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameOfCraps
{
    class Program
    {
        private static Random randomNumbers = new Random();
        private enum status { CONTiNUE, WON, LOST};
        private enum DiceNames
        {
            Snake_Eyes=2,
            Trey=3,
            seven=7,
            Yo_Leven=11,
            Box_Cars=12
        }
        public static void Main(string[] args)
        {
            status gamestatus = status.CONTiNUE;
            int mypoint = 0;
            int sumOfDice = RollDice();

            switch ((DiceNames) sumOfDice)
            {
                case DiceNames.seven:
                case DiceNames.Yo_Leven:
                    gamestatus = status.WON;
                    break;
                case DiceNames.Snake_Eyes:
                case DiceNames.Trey:
                case DiceNames.Box_Cars:
                    gamestatus = status.LOST;
                    break;
                default:
                    gamestatus = status.CONTiNUE;
                    mypoint = sumOfDice;
                    Console.WriteLine("point is {0}", mypoint);
                    break;

            }

            while (gamestatus == status.CONTiNUE)
            {
             sumOfDice = RollDice();
                if (sumOfDice == mypoint)
                    gamestatus = status.WON;
                else
                    if (sumOfDice == (int)DiceNames.seven)
                    gamestatus = status.LOST;
            }
            if (gamestatus == status.WON)
                Console.WriteLine("player win");
            else
                Console.WriteLine("player loses");

            public static int RollDice()
            {
                int die1 = randomNumbers.Next(1, 7);
                int die2 = randomNumbers.Next(1, 7);

                int sum= die1+die2;
                Console.WriteLine("player rolled {0}+{1}={2}", die1, die2, sum);
                return sum;
            }
        }
    }
}