# Regex Sudoku Challenge

## Table of Regular Expressions:
![image](https://github.com/yardenrev/scripts/assets/145215505/3a708970-c233-4b9b-805d-b4360e687636)

## Instructions:

1. The challenge consists of a table with two columns and two rows. Each row and column contains a regular expression that you will use to create a new regular expression.

2. To solve the challenge, combine the regular expressions in the corresponding row and column to create a new regular expression that satisfies both conditions.

3. Example: If the row regular expression is `[a-p]` (one lowercase letter between a and p) and the column regular expression is `[rotem]` (one of the following letters: "r", "o", "t", "e", "m"), the combined regular expression would be `[oem]` because "r" and "t" are not in the "a-p" range, and all letters that are in "a-p" but not in "rotem" do not satisfy the column condition.

![image](https://github.com/yardenrev/scripts/assets/145215505/acf328df-960c-48f1-857e-2223a3142ff4)

4. Repeat this process for each empty slot in the table, using the regular expressions in the corresponding row and column to create a new regular expression that satisfies both conditions.

5. Once you have filled in all four empty slots with the correct regular expressions, you will have completed the Regex Sudoku challenge.

6. Your task is to extract the flag from the attached text file "CFT_regex_text.txt" using the regex you have found.

Feel free to use regex tools or your preferred programming language to test and validate your combined regular expressions. Good luck!
