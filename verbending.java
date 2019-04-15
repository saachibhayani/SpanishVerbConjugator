package com.example.arrays;

import java.util.Scanner;
import java.lang.StringBuilder;

public class verbending
{
    public static void main(String[] args)
    {
        Scanner kb = new Scanner(System.in);

        System.out.println("Verb: ");
        String verb = kb.nextLine();

        Character end1 = verb.charAt(verb.length()-1);
        //System.out.println(end1);

        Character end2 = verb.charAt(verb.length()-2);
        //System.out.println(end2);

        //String ending = end2 + end1;
        //System.out.println(ending);

        String ending = new StringBuilder().append(end2).append(end1).toString();
        System.out.println(ending);

        if (ending = "ar")
        {
            System.out.println("Ending is AR");
        }

    }
}
