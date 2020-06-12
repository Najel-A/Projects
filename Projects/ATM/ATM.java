import java.util.*;

public class ATM
{
    public static void main(String [] args)
    {
        int balance = 5000;
        int withdraw;
        int deposit;
        Scanner input = new Scanner(System.in);
        while (true)
            {
                System.out.println("Najel's Automated Teller Machine");
                System.out.println("Press 1 to Withdraw");
                System.out.println("Press 2 to Deposit");
                System.out.println("Press 3 to Check Account");
                System.out.println("Press 4 to exit");
                System.out.print("What would you like to do today? ");
                int choice = input.nextInt();
                switch(choice)
                    {
                        case 1:
                            System.out.println("");
                            System.out.println("Your account balance: $" + balance);
                            System.out.print("Enter amount to withdraw: $");
                            withdraw = input.nextInt();
                            if (balance >= withdraw)
                                {
                                    balance -= withdraw;
                                    System.out.println("Your money has been dispensed");
                                    System.out.println("Your account balance: $" + balance);
                                }
                            else
                            {
                                System.out.println("Insufficient Funds");
                            }
                            System.out.println("");
                            break;

                        case 2:
                            System.out.println("");
                            System.out.println("Your account balance: $" + balance);
                            System.out.print("Enter amount to deposit: $");
                            deposit = input.nextInt();
                            balance += deposit;
                            System.out.println("Your money has been deposited");
                            System.out.println("Your account balance: $" + balance);
                            System.out.println("");
                            break;

                        case 3:
                            System.out.println("");
                            System.out.println("Your account balance: $" + balance);
                            System.out.println("Your savings balance: $" + 25000);
                            System.out.println("Your interest rate: " + 0.09 + "%");
                            System.out.println("");
                            break;

                        case 4:
                            System.out.println("");
                            System.out.println("Thank you for using Najel's ATM");
                            System.out.println("      Have a great day!"); //Spacing for text presentation
                            System.exit(0);
                    }


            }
    }
}
