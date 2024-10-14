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
    - [name.py](https://github.com/chloenumber1/intro-python/blob/main/chapter_2/chapter_2_examples/name.py) contains the code examples for this section
    - Methods used in this section were .title(), .upper(), and .lower().
    - 2.3.1.1 Further information about variables: another way to manipulate data held in a variable without reassigning it is to use a method.
    - 2.3.1.2 What is a method: in the context of the example name.py, where methods like .title() were used, built-in methods are predefined functions that can perform specific operations on objects (strings are objects).
    - 2.3.1.3 Explaining the syntax &lt;variable&gt;.<method()> by breaking it into components:
        - 2.3.1.3.1 &lt;variable&gt;: This variable can hold any data type that has methods defined for it such as a string, list, etc.
        - 2.3.1.3.2 Dot operator (.): The dot operator is used to access the methods and attributes of the object. The dot signifies that the method belongs to the object referenced by <variable>.
        - 2.3.1.3.3 <method()>:This is the name of the method you want to call. It can take parameters in the parentheses if it needs to.
- *2.3.2 
**2.4 Numbers**

**2.5 Comments**

**2.6 The Zen of Python**