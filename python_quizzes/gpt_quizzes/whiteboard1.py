"""Problem: Find the Longest Substring Without Repeating Characters

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Step 1: 
Understand the Problem
Inputs:

A single string s (e.g., "abcabcbb").
Outputs:
An integer representing the length of the longest substring with unique characters (e.g., for "abcabcbb", the result is 3 because "abc" is the longest substring without duplicates).
Constraints:

The string can contain lowercase/uppercase letters, numbers, or special characters.
The string can be empty (""), in which case the result should be 0.
Edge Cases:

Empty string ("").
All characters are unique ("abcdef").
All characters are the same ("aaaaa").
String with mixed repeating and unique characters ("pwwkew").
Step 2: Break the Problem into Sub-Problems
Track Unique Characters:

Use a data structure to keep track of characters in the current substring.
Sliding Window Approach:

Expand the window (substring) when characters are unique.
Shrink the window when a character repeats.

Track the Maximum Length:
Keep a variable to store the maximum length of a unique substring seen so far.

Step 3: Design the Solution (Mental Whiteboard)
High-Level Algorithm:
Use two pointers (left and right) to represent a sliding window over the string.
Expand the window by moving the right pointer and adding characters to a set.
If a character repeats, shrink the window by moving the left pointer until the character is no longer in the set.
Update the maximum length whenever the window expands.
Data Structures:
Set: To track unique characters in the current window.
Variables: max_length to store the maximum substring length.

Step 4: Pseudocode
plaintext
Copy code
1. Initialize:
    - A set to store unique characters.
    - Two pointers: left = 0, right = 0.
    - A variable max_length = 0.

2. While right < length of the string:
    - If s[right] is not in the set:
        a. Add s[right] to the set.
        b. Update max_length = max(max_length, right - left + 1).
        c. Move right pointer forward.
    - Else:
        a. Remove s[left] from the set.
        b. Move left pointer forward.

3. Return max_length.
Step 5: Analyze Complexity
Time Complexity:

Each character is added and removed from the set at most once → O(n).
Space Complexity:

The set requires space proportional to the number of unique characters in the string → O(min(n, a)), where a is the size of the character set (e.g., 26 for lowercase English letters)."""