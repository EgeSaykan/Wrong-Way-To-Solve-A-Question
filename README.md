# Wrong-Way-To-Solve-A-Question
Probably most unefficent and wrong way to solve a hard maths question.

## Question: 
In a school, every student has a student number starting from 00000 up to 99999. And student numbers of two random students have at least two different digits. How many students are there in this school?

## What I did:
What I understand is every student number will have 2 different digits from any other. For example, 00000 and 00011 is suitable. Because ones-digit and tens-digit are different. but 00000 and 00001 can't be. Because they have only ones-digit different. 

The markscheme says there are 10,000 students in school. 
I didn't understand how or why. So I made a program to check every number from 00000 to 99999.

It creates a text file called Q1Answers.txt (which is 47kb). First number in that file is how many students there are (6735 students) and the rest are students' numbers. Basicly I didn't find the answer markscheme has. 

#### P.S.
If you find a way to solve this question the way it is supposed to and prove me wrong, please let me know.


# The Solution:
I have finally solved the problem. (22/06/2022)
I have used mathematical way instead of computer science way:

### If we just consider last 2 digits:
00000, 
00011, 
00022, 
  .
  .
  .
00099
### This produces 10 combinations.


### And of course numbers in the case are just symbols, so 0 at 3rd digit doesnt have much significance.
### So the patterns:
00000,
00011,
00022,
  .
  .
  .
00099,

00100,
00111,
00122,
  .
  .
  .
00199
### can exist simultaneously.
### Hence 3rd digit can be changed with any number. So 10 * 10 different combinations.

## Same principle applies to 2nd digit, and 1st digit. Hence 10 * 10 * 10 * 10 = 10,000 different combinations.
