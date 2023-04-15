import java.io.*;
import java.util.*;

public class Main{
    public static int solution(String str){
        int n = str.length();             //Length of the given string is initialized to n
        int[][] dp = new int[n+1][n+1];   //this creates the dp table

        for(int i=n;i>=0;i--){         //The dp table is filled from the bottom right-most cell
            for(int j=n;j>=0;j--){
                if(i==n || j==n){       //The last row and column are zero as "blank" is considered at the ends
                    dp[i][j] = 0;
                }
                else {
                    if(str.charAt(i)==str.charAt(j) && i!=j){     //To make sure that the same place holder character are not considered(i.e i!=j) 
                        dp[i][j] = dp[i+1][j+1]+1;                //Diagonally two opposite values are added
                    }
                    else{
                        dp[i][j] = Math.max(dp[i+1][j],dp[i][j+1]);  //the max of the two diagonally  opposite values is considered  
                    }
                }
            }
        }
        return dp[0][0];    //The 1st cell will always gives the length of the maximum repeating subsequence
    }

    public static void main(String[] args){
    	System.out.println("Enter the string : ");
        try (Scanner scn = new Scanner(System.in)) {     //Scanner class is used for taking the input
            String str = scn.next();
            System.out.println(solution(str));
        }
    }
}
