**Ch.2 Variables and Simple Data Types**

**2.1 What Really Happens When You Run hello_world.py**\
![Python Interpretation and Compilation](https://raw.githubusercontent.com/chloenumber1/intro-python/refs/heads/main/chapter_2/chapter_2_notes/ch_2_notes_imgs/python-interpretation-compilation.jpg)

**2.2 Variables**
- *2.2.1 Naming and Using Variables*:
    - 2.2.1.1 Variable names can only have letters, numbers, and underscores.
        - 2.2.1.1.1 Variables CAN start with a letter or underscore.
        - 2.2.1.1.2 Variables CANNOT start with a number.
    - 2.2.1.2 Spaces are NOT allowed in variable names (e.g. variable name) so use underscores as separators (e.g. variable_name)
    - 2.2.1.3 Do not use Python keywords and function names as variable names.
    - 2.2.1.4 Keep variable names short and descriptive.
    - 2.2.1.5 Try to careful when using 1, 0, O, and l since they can easily be confused.
- *2.2.2 Avoiding Name Errors When Using Variables*:
    - 2.2.2.1 "A traceback is a record of where the interpreter ran into trouble when trying to execute your code" (p.18).
    - 2.2.2.2 Ensure your variables are spelled correctly throughout your code to prevent errors.
- *2.2.3 Variables are Labels*:
    - 2.2.3.1 Variables are named spaces, meaning that they reference a stored value. Name your variables in a meaningful, descriptive way so your code is cleaner and so you can parse through errors more easily.
    - 2.2.3.2 Try-It-Yourself [2-1](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/ch_2_try_it_yourself/tiy_2_1_simple_message.py) and [2-2](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/ch_2_try_it_yourself/tiy_2_2_simple_messages.py) are in this section. Refer to the ch2_try_it_yourself folder to see the files.Those 2 exercises are about how to assign a string variable and what string reassignment looks like. 

**2.3 Strings**
- A String is a series of characters enclosed in either double or single quotes.
- *2.3.1 Changing Case in a String with Methods*:
    - [e1_cases.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e1_cases.py) contains the code examples for this section
    - Methods used in this section were .title(), .upper(), and .lower().
    - 2.3.1.1 Further information about variables: another way to manipulate data held in a variable without reassigning it is to use a method.
    - 2.3.1.2 What is a method: in the context of the example name.py, where methods like .title() were used, built-in methods are predefined functions that can perform specific operations on objects (strings are objects).
    - 2.3.1.3 Explaining the syntax &lt;variable&gt;.<method()> by breaking it into components:
        - 2.3.1.3.1 &lt;variable&gt;: This variable can hold any data type that has methods defined for it such as a string, list, etc.
        - 2.3.1.3.2 Dot operator (.): The dot operator is used to access the methods and attributes of the object. The dot signifies that the method belongs to the object referenced by <variable>.
        - 2.3.1.3.3 <method()>:This is the name of the method you want to call. It can take parameters in the parentheses if it needs to.
- *2.3.2 Using Variables in Strings*:
    - 2.3.2.1 Formatted Strings AKA F-Strings: The purpose of F-Strings is to be able to make dynamic strings that include variable content such as variables, function calls, method calls, etc. 
    - All of the examples below are also in the [e2_f_strings.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e2_f_strings.py) file. I copied the examples in the full_name.py file from the book, but the ones below are my own.
    - 2.3.2.2 F-String Syntax: 
      f"{variable1}{variable2}"
    - 2.3.2.3 F-String Syntax Print Statement With Variable: 
      friend = "Susie"
      print(f"Hello, {friend}")
    - 2.3.2.4 F-String Syntax Print Statement With Variable and Method:
      friend = "susie"
      print(f"Hello, {friend.title()}")
- *2.3.3 Adding Whitespace to Strings with Tabs or Newlines*:
    - See [e3_escape_sequences_whitespace.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e3_escape_sequences_whitespace.py) for the tab and newline examples.
    - Escape sequences are denoted by a backslash, AKA the escape character, and another character (e.g. \n, \t, \", etc.). They allow you to put special characters into strings.
    - 2.3.3.1 Tab escape sequence: adding \t will add a tab
      ex. 
      print("\tPython")
    - 2.3.3.2 Newline escape sequence: adding \n will add a newline
      ex. print("Languages:\nPython\nC\nJavaScript")
- *2.3.4 Stripping Whitespace*:
  - See [e3_escape_sequences_whitespace.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e3_escape_sequences_whitespace.py) for whitespace stripping examples
  - Previously, we added whitespace. What if we want to remove it?
   - 2.3.4.1 The .strip() method can be used to strip whitespace FROM BOTH SIDES.
    ex.
    favorite_language1 = "    Python    "
    print(favorite_language1.strip())
   - 2.3.4.2 The .rstrip() method can be used to strip whitespace FROM THE RIGHT.
    ex. 
    favorite_language2 = "Python     "
    print(favorite_language.rstrip())
   - 2.3.4.3 The .lstrip() method can be used to strip whitespace FROM THE LEFT.
    ex. 
    favorite_language3 = "     Python"
    print(favorite_language2.lstrip())
- *2.3.5 Avoiding Syntax Errors with Strings*:
  - 2.3.5.1 Single Quotes vs. Double Quotes: See [e4_single_vs_double.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e4_single_vs_double.py) for code examples.
  - 2.3.5.2 Using ALL Single or Double Quotes: A common syntax error that can occur is if you write a string such as 'This string 'in single quotes' here.' What will happen is that Python can't identify where the string starts and ends. 
  - 2.3.5.3 A Mix of Double and Single Quotes: A mix of double quotes and single quotes won't create the error above. Something like "This string 'in single quotes' here" won't generate an error because there's no ambiguity as to where the quote starts and stops. Also, 'This string in "double quotes" doesn't generate an error either'.

**2.4 Numbers**
- *2.4.1 Integers*: 
    - An integer is 0, positive whole numbers, and negative whole numbers. Refer to [e5_integers.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e5_integers.py) to see integer code examples.
    - 2.3.1.1 What you can do with integers in Python: you can add (+), subtract(-), multiply(*), and divide(/).
    - 2.3.1.2 How you can denote exponentiation in Python: Two asterisks 
    (e.g. 3**3 = 27)
    - 2.3.1.3 Order of Operations: Python supports order of operations (e.g. 5 + 5*2 = 15)
    - 2.3.1.4 Spacing: Spacing has no effect on the evaluation of integers.
- *2.4.2 Floats*:
    - A float is any number with a decimal point. Refer to [e6_floats.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e6_floats.py) to see float code examples.
    - You can do the same operations with floats as you can do with integers.
- *2.4.3 Integers and Floats*:
    - Refer to [e7_ints_vs_floats.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e7_ints_vs_floats.py) for code examples.
    - 2.4.3.1 Division: When you divide two numbers, whether they're ints or floats, the result is a float. !!!CAVEAT: If you divide two ints with the "//" operator, it'll evaluate to an int.
    - 2.4.3.2 Mixing Integers and Floats: If you mix an integer and a float, you will always get a float, even if the result is a whole number. 
- *2.4.4 Underscores in Numbers*:
    - Refer to [e8_num_underscores.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e8_num_underscores.py) for the underscores in numbers example
    - 2.4.4.1 What Underscores in Numbers are For: You use underscores in numbers for code readibility (ex. 1_000_000). 
    - 2.4.4.2 What Underscores in Numbers Output: Python will only print the output.
- *2.4.5 Multiple Assignment*:
    - See [e9_mult_assignment.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e9_mult_assignment.py) for examples
    - 2.4.5.1 You can assign multiple variables at once: x,y,z=0,1,2
- *2.4.6 Constants*:
    - Refer to [e10_constant.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/e10_constant.py) to see a constant example where I calculate the area of a circle.
    - 2.4.6.1 A constant is a variable whose value can't be changed. Its syntax is all capital letters (e.g. A_CONSTANT_VAR = 5).

**2.5 Comments**
- See [tiy_2_10_11_comments_zen.py]() for comments
- *2.5.1 Comments Syntax*: # comment
- *2.5.2 What Comments You Should Write*:
    - 2.5.2.1 Comments should explain your code
    - 2.5.2.2 Comments should clarify complex code segments
    - 2.5.2.3 Comments should be functional, meaning that they explain a code base in a way that is clear to both new collaborators and the original code writer.

**2.6 The Zen of Python**
- See [tiy_2_10_11_comments_zen.py]() for the 19 principles