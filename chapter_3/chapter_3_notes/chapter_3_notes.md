**Ch.3 Introducing Lists**

**3.1 What is a List**
- Refer to [e1_bicycles.py]() for code examples for 3.1.1 through 3.1.4
- *3.1.1 Defining a List*: 
    - 3.1.1.1 A list is a Python data structure that is a mutable ordered sequence of elements.
    - 3.1.1.2 A set of square brackets ([]) indicate a list
    - 3.1.1.3 List elements are separated by commas
    - 3.1.1.3 Example syntax: my_list = [1,2,3,4,5]
- *3.1.2 Accessing Elements in a List*:
    - 3.1.2.1 Using an Index: An index is the position of an element in a list. If you want to access an element in the list, use the syntax list_name[1]. 
    - 3.1.2.2 Using an Index and Method: You can add a method on an element you're accessing. Ex. print(list_name[1].title()) 
- *3.1.3 Index Positions Start at 0, Not 1*:
    - 3.1.3.1 Lists are Zero-Indexed: A list's index positions always start at 0 and go to n-1.
    - 3.1.3.2 Index -1: You can access the last item of a list using the index -1. 
- *3.1.4 Using Individual Values From a List*:
    - 3.1.4.1 List Item Application: You can use list elements like variables. See the bicycles.py file for the corresponding example.

**3.2 Changing, Adding, and Removing Elements**
- *3.2.1 Modifying Elements in a List*:
- See e2_motorcycles.py for example code. Methods used in this section are" .append(), .insert(), .del(), 
    - 3.2.1.1 Changing an Element in a List: You can change an element in a similar way that you access it. 
        3.1.1.1 Step 1: Know what position of the list you want to change.
        3.1.1.2 Step 2: Reassign the element at that position in the list (ex. list_ex[0] = 5)
- *3.2.2 Adding Elements to a List*:
    - 3.2.2.1 Appending Elements to the End of a List
        - 3.2.2.1.1 You use the .append() method when you want to add an element to the END of a list. Ex. list_ex.append("hi").
        - 3.2.2.1.2 You can also use the .append() method MULTIPLE times to populate a list.
    - 3.2.2.2 Inserting Elements Into a List: You use the .insert() method to insert an element in a SPECIFIC position in a list. The syntax is list_ex.insert(<position>,"what you want")
- *3.2.3 Removing Elements from a List*:
    - 3.2.3.1 Removing an Item Using the del Statement: You use the del statement to remove an element in a SPECIFIC position in a list. 
        - 3.2.1.1.1 The del statement isn't a method, it's a statement, so no dot notation.
        - 3.2.3.1.2 The syntax is del list_ex[<position>]
    - 3.2.3.2 Removing an Item Using the pop() Method: the pop() method removes and returns the last item in a list by default.
        - 3.2.3.2.1 pop() method syntax: list_ex.pop(). See e2_motorcycles.py for an example.
    - 3.2.3.3 Popping Items from any Position in a List
    - 3.2.3.4 Removing an Item by Value
- *3.2.4 Organizing a List:*
- *3.2.5 Modifying Elements in a List*:
**3.3 Avoiding Index Errors When Working with Lists**