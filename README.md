# cky_algorithm
The Cocke–Younger–Kasami algorithm: a parsing algorithm for context-free grammars

https://medium.com/swlh/cyk-cky-f63e347cf9b4

Stats:
This algorithm is a dynamic, bottom-up approach to parsing. In this context, “dynamic” means we are going to create a table that solves a lot of subproblems, and then in the end we will be able to understand the whole problem by looking through our amalgamation of subproblems in the table.
Minna Sundberg’s illustration of language families is flipped upside down so that the root is at the top
Minna Sundberg’s illustration of language families displays few roots and many branches
Bottom-up means that when we read the table we created, we’ll look from the bottom of the branches, or the input, and track which parts of speech can be chained together in a tree on the way up, rather than starting with the first part of speech, or the root, and tracing our way down which part of speech can branch off from the first one until we get to the input.

In terms of speed, this is not the most efficient algorithm for parsing in all cases, but it is one of the best for worst-case scenarios. The algorithm has a cubic run time for the length of the input, with a multiplier for the size of the grammar.

High Level:
In this algorithm, we will use the upper right hand portion of a matrix. We will start by storing the words in the string in cells that span a diagonal line from the top left of the matrix to the bottom right. Using the information previously stored in the matrix, we will incrementally build up the rest of the upper right hand portion of the matrix, storing subtrees that match what we have as we go. As we get farther away from the words, a split point or pivot point becomes key to this process. As we look through the table’s rows and columns (i-j) we will also be checking for a pivot point (k) where we might have a grammar rule for both [i,k] and [k,j]. So to have A -> B C in [i][j], we will need to have B in [i][k] and C in [k][j] while k is greater than i but less than j. This is possible because we have split up our grammar rules into Chomsky normal form, so we will only have at most two rules in a production, and can check for all of these possible outcomes easily, as opposed to splitting them up into a billion extra substrings and searching through each one. The pseudocode looks like this:

![jurafskypseudo](https://user-images.githubusercontent.com/28895742/110976788-5b190500-832f-11eb-939d-d7a1c31462be.PNG)
