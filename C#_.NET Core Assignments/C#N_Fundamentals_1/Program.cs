using System;

namespace first_csharp
{
    class Program
    {
        static void Main(string[] args)
        {
              // fizz,buzz without Modulus
        
            // loop through 1 to 100
            
            for(int val = 1; val <= 100; val++){

                //convert each number to a string

                string strval = val.ToString();

                //Add the string parts. and get the last number from the sum. 
                int currsum = 0;
                string currsumstr;
                int currsumstrlastdigit = 0;

                for(int x = 0; x < strval.Length; x++){

                    // If the last number is one of the known modulo values, print. 
                    if(currsumstrlastdigit == 3 || currsumstrlastdigit == 6 || currsumstrlastdigit == 9)
                        Console.WriteLine("Fizz");      
                }
            }
        }
    }
};

        // without modulus
        // for(int val = 1; val <= 100; val++){
        //     string valstr = val.ToString();
        //     int y = 0;
        //         for(int x = 0; x<= valstr.Length; x++){
        //             y += valstr[x];
        //         }
        //     if(y/3 == 0){
        //         Console.WriteLine(valstr);
        //     }
          
        // }
        
        // fizz,buzz
        // for(int val = 1; val <= 100; val++){
        //     if(val % 15 == 0){
        //          Console.WriteLine("FizzBuzz");
        //     }
        //     else if(val % 3 == 0){
        //         Console.WriteLine("Fizz");
        //     }
        //     else if(val % 5 == 0){
        //         Console.WriteLine("Buzz");
        //     }

        
        // }
        //     // One to 100 devisible by 3 or 5 byt not both.        
        // for(int val = 1; val <= 100; val++){
        //     if(val % 15 == 0){
        //         //do nothing;
        //     }
        //     else if(val % 3 == 0){
        //         Console.WriteLine(val);
        //     }
        //     else if(val % 5 == 0){
        //         Console.WriteLine(val);
        //     }
        
        //     One to 255
        //  for(int val = 1; val <= 255; val++)
        //     {
        //         Console.WriteLine(val);
        //     }   


        
