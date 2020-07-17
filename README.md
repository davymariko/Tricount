# Tricount
Here is a project I worked on my school project in the course of algorithm.

A Python program to help friends with their expenses to set accounts to zero.

It is therefore a question here of producing a list of transactions allowing each person to be reimbursed from a list of expenses.
The description of an expense includes several elements:
- The name of the person who paid the expense (here denoted by a number);
- The amount paid;
- The names of the persons concerned (denoted by a number too);

Example:
2	50	1	3	4
3	15	3	4
1	25	2	3

--> 2 paid 50 euros for 1, 3 and 4 hence they owe 2 16.3 euros(50/3) each
    3 paid 15 euros for 3 and 4 hence 4 owes 7.5 to 3
    1 paid 25 euros for 2 and 3 hence they owe 1 12.5 euros each

As part of this project, instances(examples/database) of the problem will be described in TSV (tab-separated values) files.

The goal is to produce a list of transactions (the minimum possible) in order to set the expenses to zero.

Exmple of output:
4 pays 24.17 eur to 2
3 pays 13.33 eur to 2
3 pays 8.33 eur to 1
