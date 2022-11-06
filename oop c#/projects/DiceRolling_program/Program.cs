﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DiceRolling_program
{
    class Program
    {
        public static void Main(string[] args)
        {
				int die1 = 0;
				int die2 = 0;
				int[,] dieValues;
				int[] sums;
				int sum = 0;
				dieValues = new int[7, 7]; 
				sums = new int[13];
				Random rand = new Random();
				for (int i = 0; i < 36000; i++)
				{
					die1 = rand.Next(1, 7);
					die2 = rand.Next(1, 7);
					sum = die1 + die2;

					dieValues[die1, die2] += 1;
					sums[sum] += 1;
				}

				Console.WriteLine("         1       2        3      4        5      6");
				Console.WriteLine("-----------------------------------------------------");
				for (int r = 1; r <= 6; r++)
				{
					Console.Write(" {0:N0} |", r);
					for (int c = 1; c <= 6; c++)
					{
						Console.Write("    {0:D4} ", dieValues[r, c]);
						if (c == 6)
							Console.WriteLine();
					}
				}

				Console.WriteLine("      2      3       4       5       6       7       8       9       10       11       12");
				Console.WriteLine("-------------------------------------------------------------------------------------------");
				for (int i = 2; i <= 12; i++)
				{
					Console.Write("    {0:D4}", sums[i]);
				}

				Console.ReadLine();
			
		}

	}
    
}
