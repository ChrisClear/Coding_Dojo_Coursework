using System;
using System.Collections.Generic;

namespace basic13
{
    class Program
    {
        static void Main(string[] args)
        {
        oneto255();

        oddsto255();

        intsandsumto255();

        iteratearray();

        findMax();

        getAverage();

        arrayOfOdds();
        
        int[] numberArray1 = {1,3,5,7,9,13};
        int y = 8;
        greaterThanY(numberArray1,y);

        squareValues();

        removeNegatives();

        int[] numberArray2 = {1, 5, 10, -2};
        minMaxAverage(numberArray2);

        int[] numberArray3 = {1, 5, 10, 7, -2};
        shiftArray(numberArray3);

        int[] numberArray4 = {-1, -3, 2};
        numToString(numberArray4);


        }


    //Print 1-255
    //Write a program (sets of instructions) that would print all the numbers from 1 to 255.
    static void oneto255(){
        Console.WriteLine("===================oneto255===============================");
            for(int i = 1; i <= 255; i++){
                Console.WriteLine(i);
            }
        }
        //Print odd numbers between 1-255
        //Write a program (sets of instructions) that would print all the odd numbers from 1 to 255.
    static void oddsto255(){
        Console.WriteLine("======================oddsto255============================");
        for(int i = 1; i <= 255; i++){
            if(i % 2 != 0){
                Console.WriteLine(i);
            }
        }
    }

    // Print Sum
    // Write a program that would print the numbers from 0 to 255 but this time, it would also print the sum of the numbers that have been printed so far. For example, your output should be something like this:
    // New number: 0 Sum: 0
    // New number: 1 Sum: 1
    // New Number: 2 Sum: 3
    // New number: 3 Sum: 6
    // New Number: 255 Sum: ___.
    // Do NOT use an array to do this exercise.
    static void intsandsumto255(){
        Console.WriteLine("===================intsandsumto255===============================");
        int sum = 0;
        for(int i = 0; i <= 255; i++){
            sum += i;
            Console.WriteLine("New number: " + i + ", Sum: " + sum);
        }
    }

    // Iterating through an Array
    // Given an array X, say [1,3,5,7,9,13], write a program that would iterate through each member of the array and print each value on the screen. Being able to loop through each member of the array is extremely important.
    public static void iteratearray(){
        Console.WriteLine("===================iteratearray===============================");
        int[] numberArray = {1,3,5,7,9,13};
        for(int i = 0; i < numberArray.Length ; i++){
                Console.WriteLine(numberArray[i]);
        }
    }
    
    // Find Max
    // Write a program (sets of instructions) that takes any array and prints the maximum value in the array. Your program should also work with a given array that has all negative numbers (e.g. [-3, -5, -7]), or even a mix of positive numbers, negative numbers and zero.
    public static void findMax(){
        Console.WriteLine("==============findMax====================================");
        int[] numberArray = {1,3,5,777,9,13};
        int max = numberArray[0];
        for(int i = 1; i < numberArray.Length ; i++){
            if(numberArray[i] > max){
                max = numberArray[i];
            }
        }
        Console.WriteLine("Max is: " + max);
    }

    // Get Average
    // Write a program that takes an array, and prints the AVERAGE of the values in the array. For example for an array [2, 10, 3], your program should print an average of 5. Again, make sure you come up with a simple base case and write instructions to solve that base case first, then test your instructions for other complicated cases. You can use a count function with this assignment.
    public static void getAverage(){
        Console.WriteLine("==================getAverage================================");
        int[] numberArray = {1,3,5,7,9,13};
        int average = 0;
        int sum = 0;
        for(int i = 0; i < numberArray.Length; i++){
            sum += numberArray[i];
        }
        average = sum / numberArray.Length;
        Console.WriteLine(average);
    }

    // Array with Odd Numbers
    // Write a program that creates an array 'y' that contains all the odd numbers between 1 to 255. When the program is done, 'y' should have the value of [1, 3, 5, 7, ... 255].
    public static void arrayOfOdds(){
        Console.WriteLine("==================arrayOfOdds================================");
        List<int> templist = new List<int>();
        for(int i = 0; i <= 255; i++){
            if(i % 2 != 0){
                templist.Add(i);
            }
        }
        int[] y = templist.ToArray();
        Console.Write("[");
        foreach(var item in templist){
            Console.Write(item.ToString());
            if(item != 255){
                Console.Write(", ");
            }
        }
        Console.Write("]");
        Console.WriteLine();
    }

    // Greater than Y
    // Write a program that takes an array and returns the number of values in that array whose value is greater than a given value y. For example, if array = [1, 3, 5, 7] and y = 3. After your program is run it will print 2 (since there are two values in the array that are greater than 3).
    public static void greaterThanY(int[] numberArray, int y){
        Console.WriteLine("================greaterThanY==================================");
        int count = 0;
        for(int i = 0; i < numberArray.Length ; i++){
            if(numberArray[i] > y){
                count++;
            }          
        }
        Console.WriteLine(count);
    }

    // Square the Values
    // Given any array x, say [1, 5, 10, -2], create an algorithm (sets of instructions) that multiplies each value in the array by itself. When the program is done, the array x should have values that have been squared, say [1, 25, 100, 4].
    public static void squareValues(){
        Console.WriteLine("=================squareValues=================================");
        int[] givenArray = {1,5,10,-2};
        List<int> templist =new List<int>();
        for(int i = 0; i < givenArray.Length ; i++){
            int temp = givenArray[i]*givenArray[i];
            templist.Add(temp);
        }
        int[] x = templist.ToArray();
        foreach(var item in templist){
            Console.WriteLine(item);
        }
    }

    // Eliminate Negative Numbers
    // Given any array x, say [1, 5, 10, -2], create an algorithm that replaces any negative number with the value of 0. When the program is done, x should have no negative values, say [1, 5, 10, 0].
    public static void removeNegatives(){
        Console.WriteLine("=================removeNegatives=================================");
        int[] givenArray = {1,5,10,-2};
        List<int> templist = new List<int>();
        for(int i = 0; i < givenArray.Length ; i++){
            if(givenArray[i] >=0 ){
                templist.Add(givenArray[i]);
            }
        }
        int[] x = templist.ToArray();
        foreach(var temp in templist){
            Console.WriteLine(temp);
        }
    }

    // Min, Max, and Average
    // Given any array x, say [1, 5, 10, -2], create an algorithm that prints the maximum number in the array, the minimum value in the array, and the average of the values in the array.
    public static void minMaxAverage(int[] numberArray){
        Console.WriteLine("===============minMaxAverage===================================");
        int min = numberArray[0];
        int max = numberArray[0];
        int sum = numberArray[0];
        int avg = 0;

        for(int i = 1; i < numberArray.Length ; i++){
            if(numberArray[i] < min){
                min = numberArray[i];
            }
            if(numberArray[i] > max ){
                max = numberArray[i];
            }
            sum += numberArray[i];
        }
        avg = sum/numberArray.Length;
        Console.WriteLine("Min: "+min+", Max: "+max+", and Avg: "+avg);
    }

    // Shifting the values in an array
    // Given any array x, say [1, 5, 10, 7, -2], create an algorithm that shifts each number by one to the front and adds '0' to the end. For example, when the program is done,  if the array [1, 5, 10, 7, -2] is passed to the function, it should become [5, 10, 7, -2, 0].
    public static void shiftArray(int[] numberArray){
        Console.WriteLine("===============shiftArray==================================");
    
        List<int> templist = new List<int>();
    
        for(int i = 0; i < numberArray.Length-1; i++){
            templist.Add(numberArray[i+1]);
        }
        templist.Add(0);
        foreach(var item in templist){
            Console.WriteLine(item);
        }
    }

    // Number to String
    // Write a program that takes an array of numbers and replaces any negative number with the string 'Dojo'. For example, if array x is initially [-1, -3, 2] your 
    //function should return an array with values ['Dojo', 'Dojo', 2].
    public static List<string> numToString(int[] numberArray){
        Console.WriteLine("================numToString==================================");
        
        List<string> templist = new List<string>();

        for(int i = 0; i < numberArray.Length; i++){
            if(numberArray[i] < 0){
                templist.Add("Dojo");
            } else {
                templist.Add(numberArray[i].ToString());
            }
        }
        // templist.ToArray();
        foreach(var item in templist){
            Console.WriteLine(item);
        }
        return templist;
    }

    }
}
