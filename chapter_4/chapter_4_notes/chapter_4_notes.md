**Ch.4 Working With Lists**

**4.1 Looping Through an Entire List**
- *4.1.1 A Closer Look at Looping*:
    - 4.1.1.1 The for loop: a for loop is the first control structure being introduced. The purpose of a for loop is to iterate over an iteratable object (in this case a list, but more generally a sequence). The primary objective of a for loop is to automate repetitive tasks (such as accessing elements in a list, printing statements repeatedly, etc.).
    - 4.1.1.2 Explaining the for loop syntax by breaking it into components:
        - The first example for the for loop shows its syntax. It can be found in [e1_magicians.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_4/chapter_4_examples/e1_magicians.py)
        - 4.1.1.2.1 Start with an example\
        for variable in sequence:\
            (code block that will be executed)
        - 4.1.1.2.2 Keyword for: The keyword "for" initiates the for loop
        - 4.1.1.2.3 variable: "variable" is a placeholder that represents the current item in the sequence during each iteration.
            - 4.1.1.2.3.1 More on "variable": It's called a placeholder variable because it doesn't have a fixed value throughout the loop. Its value changes with each iteration. So, the variable "variable" is essentially a container that's filled with a new item from the list in each pass of the loop.
        - 4.1.1.2.4 Keyword in: The keyword in is used to specify that the variable will iterate over the given sequence.
        - 4.1.1.2.5 sequence: "sequence" is what's being iterated over and it can be any iteratable object. 
        - 4.1.1.2.6 colon (:): The colon marks the end of the for statement
        - 4.1.1.2.7 code block to be executed: The code block indented under the for statement will be executed for each item in the sequence.
- *4.1.2 Doing More Work Within a for Loop*:
    - This subchapter emphasizes that you can write multiple lines in the body of the for loop in order to do a variety of operations on the sequence.
    - See [e1_magicians.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_4/chapter_4_examples/e1_magicians.py) for examples.
    - 4.1.2.1 A for loop with a formatted String: In the example file there is an example of a for loop with a formatted string in its body. 
    - 4.1.2.2 A for loop with two formatted Strings: In the example file there is an example of a for loop with two formatted strings in its body. 
- *4.1.3 Doing Something After a for Loop*:
    - Indentation is critical with for loops, since it specifies what is in and out of the loop. If you want to do something after a for loop finishes executing, then you must ensure that the statement is outside of the loop (and you do this with proper indentation).
    - See [e1_magicians.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_4/chapter_4_examples/e1_magicians.py) for examples.
    - 4.1.3.1 Working outside of the loop: In the example file, there is an example where a statement is printed outside of the loop to illustrate that only statements inside of the loop body are repeated. 

**4.2 Avoiding Indentation Errors**
- Indentation in Python is essential for defining the structure of code blocks, as it indicates which statements belong together, such as in functions, loops, or conditionals. This requirement makes the code more clear while also indicating the scope of variables and the flow of execution. Unlike programming languages that use braces, Python enforces consistent indentation as a syntax requirement, where improper indentation leads to errors.
- See [e1_magicians.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_4/chapter_4_examples/e1_magicians.py) for examples of the various indentation errors.
- *4.2.1 Forgetting to Indent*:
    - 4.2.1.1 Forgotten Indent in General: If you forget to indent, it'll often cause a code error.
- *4.2.2 Forgetting to Indent Additional Lines*:
    - 4.2.2.1 Forgotten Indent of ADDITIONAL Lines: if you forget to indent additional lines, it may not generate an error message but it will cause unexpected code behavior. This is a logical error. 
- *4.2.3 Indenting Unnecessarily*:
- *4.2.4 Indenting Unnecessarilt After the Loop*:
- *4.2.5 Forgetting the Colon*:

**4.3 Making Numerical Lists**

**4.4 Working with Part of a List**

**4.5 Tuples**

**4.6 Styling Your Code**