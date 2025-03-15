#include <cs50.h>
#include <stdio.h>

/*int main(void)
{
    int n;
    do
    {
        n = get_int("what is height even? ");
    }
    while (n < 1);

    //the outside loop will iterate an amount of times = to the return value gathered from the user at the prompt.
    //This number is represented by i < 1 since the first iteration happens when i = 0
    for (int i = 0; i < n; i++)
    {
        {
            //it is common to use j inside i
            //if j is less than (n - i) - 1, incrementally increase j.
            //e.g. if n is 10, the first iteration would be 10 - i(which is zero) -1. this = 9.
            //so no matter what the input, this equation ensures that the inside loop always runs 1 less than the difference
            for (int j = 0; j < n - i - 1; j++)
            {
                printf(" ");
            }
            //this inner loop
            for (int j = 0; j <= i; j++)
            {
                printf("#");
            }

            printf("  ");

            for (int j = 0; j <= i; j++)
            {
                printf("#");
            }

            for (int j = 0; j < n - i - 1; j++)
            {
                printf(" ");
            }
            printf("\n");
        }
    }
}*/

int printRow(int userInput, int row);

int main(void)
{
    int n;
    do
    {
        n = get_int("height?: ");
    }
    while(n < 1);
    for(int i = 0; i < n; i++)
    {
        printRow(n, i);
    }
}

int printRow(int userInput, int row)
{
        for(int j = 0; j < userInput - row - 1; j++)
        {
            printf(" ");
        }
        for(int j = 0; j < row; j++)
        {
            printf("#");
        }

        printf("  ");

        for(int j = 0; j < row; j++)
        {
            printf("#");
        }
        for(int j = 0; j < userInput - row - 1; j++)
        {
            printf(" ");
        }

        printf("\n");
        return 0;
}
