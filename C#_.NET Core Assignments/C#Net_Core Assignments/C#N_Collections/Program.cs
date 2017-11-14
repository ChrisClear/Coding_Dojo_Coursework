using System;
using System.Collections.Generic;

namespace collectionspractice
{
    class Program
    {
        static void Main(string[] args)
        {

//            Three Basic Arrays

            //Create an array to hold integer values 0 through 9
            int[] numArray1 = {1,2,3,4,5,6,7,8,9};

            //Create an array of the names "Tim", "Martin", "Nikki", & "Sara"
            string[] nameArray1 = new string[4] { "Tim", "Martin", "Nikki", "Sara"};

            //Create an array of length 10 that alternates between true and false values, starting with true           
            bool[] array = new bool[10];
                array[0] = true;
                array[2] = true;
                array[4] = true;
                array[6] = true;
                array[8] = true;

//             Multiplication Table

            //With the values 1-10, use code to generate a multiplication table like the one below.
            int[,] cbox = new int[10,10]; //m as in roman numaeral 100 
                for(int x = 0; x <= 9; x++){ //row loop
                    for(int z = 0; z <= 9; z++){ // column loop
                        cbox[x,z]=(x+1)*(z+1);
                        Console.Write(string.Format("{0} ", cbox[x,z]));
                    }
                    Console.Write(Environment.NewLine);
                }
                Console.ReadLine();


//              List of Flavors


            // Create a list of Ice Cream flavors that holds at least 5 different flavors (feel free to add more than 5!)
               
                List<string> flavors = new List<string>();
                flavors.Add("Ninjas N' Cream");
                flavors.Add("Dojo");
                flavors.Add("Mint Dojo Chip");
                flavors.Add("Vanilla");
                flavors.Add("Cookie Doujo");
                flavors.Add("Rocky Cobblestone Path");

            // Output the length of this list after building it

                Console.WriteLine("We currently know of {0} favors.", flavors.Count);



            // Output the third flavor in the list, then remove this value.

                Console.WriteLine(flavors[2]); //Prints "Mint Dojo Chip"
                flavors.Remove("Mint Dojo Chip");
                Console.WriteLine(flavors[2]); //Prints "Vanilla" which I found very cool! It works by string and not just index!!!
                flavors.Remove(flavors[2]);
                Console.WriteLine(flavors[2]); //Prints "Cookie Doujo" 


            // Output the new length of the list (Note it should just be two less~)

                Console.WriteLine("We currently know of {0} favors.", flavors.Count);

//          User Info Dictionary

            // Create a Dictionary that will store  string values
            Dictionary<string,string> userflavors = new Dictionary<string,string>();

            // For each name in the array of names you made previously, add it as a new key in this dictionary with value null
            foreach(string name in nameArray1){
                userflavors.Add(name, null);
                Console.WriteLine("Writing names: " + name);
            };

            // For each name key, select a random flavor from the flavor list above and store it as the value
            // select random number... equal to array length. 


            // check randFlavors

             // For each name key, select a random flavor from the flavor list above and store it as the value
            Random rand = new Random();
            
            List<string> keys = new List<string>(userflavors.Keys);
            for (int i = 0; i < keys.Count; i++){
                userflavors[keys[i]] = flavors[rand.Next(0,4)];
            }
            // Loop through the Dictionary and print out each user's name and their associated ice cream flavor.            
            foreach (var entry in userflavors){
                Console.WriteLine(entry.Key + " - " + entry.Value);
            }
        }       
    }
}
