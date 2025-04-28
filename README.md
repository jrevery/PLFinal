# Final Project for Oklahoma Christian 2025 Programming Languages - Create an Interpreted Language

Credit: [Making a Programming Language & Interpreter in under 10 minutes!](https://www.youtube.com/watch?v=A3gTw1ZkeK0) by bvdl.io.  

Video is used for a large portion of logic and initial code. Minor functionality built atop it to accomplish example programs.

# Language Usage and Information
run ```python PLInterpreter.py <fileName>``` to run the interpreter on a text file.

The programming language itself is stack-based.

```PUSH``` and ```POP``` can be used to add or remove an element from the stack, they are also used within certain functions.

```JUMPGT0``` is a conditional jump for if the top value of the stack is greater than 0

```JUMPLT0``` is for if the value is less than 0

```JUMPEQ0``` is for if the value equals zero

```JUMP``` will always jump, regardless of value

```SECTION <name>``` provides the labels for jumping


```ADD``` and ```SUB``` take 2 values from the stack and push one back after arithmetic


```READ``` can be used for user input. For reading, use ```READ NUM``` or ```READ TEXT``` to explicitly define what kind of data you expect.

```PRINT``` will print a value to the console. ```PRINT /TOP``` prints the top value from the stack without popping. ```PRINTINLINE``` prints without line carriage


Store is a size-4 array used for holding values outside of the stack, reminiscent of registers in assembly. 

```STORE <1-4>``` Stores the top value from the stack into a specified location

```UNSTORE <1-4>``` Loads the value from the store back onto the stack, default 0 if empty

```DUPLICATE``` pushes the top value from the stack onto it again

```STRLEN``` takes a string and pushes its length onto the stack

```CHARCONVERT``` pushes each character of a string onto the stack (probably only useful for character counting and string reversing)

```STOP``` indicates the end of a program

Example programs are attached along with PLInterpreter.py 
