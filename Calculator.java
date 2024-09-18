import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        // Create a Scanner object to read input from user
        Scanner input = new Scanner(System.in);

        // Enter two double numbers
        System.out.print("Enter the first number: ");
        String strNum1 = input.nextLine();
        System.out.print("Enter the second number: ");
        String strNum2 = input.nextLine();

        // Convert the strings to double
        double num1 = Double.parseDouble(strNum1);
        double num2 = Double.parseDouble(strNum2);

        // Calculate sum, difference, product
        double sum = num1 + num2;
        double difference = num1 - num2;
        double product = num1 * num2;

        // Check if the second number is not zero for division
        if (num2 != 0) {
            double quotient = num1 / num2;
            System.out.println("Quotient: " + quotient);
        } else {
            System.out.println("Cannot divide by zero!");
        }

        // Print results
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
    }
}
