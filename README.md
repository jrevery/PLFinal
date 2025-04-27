# Final Project for Oklahoma Christian 2025 Programming Languages - Create an Interpreted Language

CREDIT - https://www.youtube.com/watch?v=A3gTw1ZkeK0&pp=ygUHI2RveHRzbA%3D%3D "Making a Programming Language & Interpreter in under 10 minutes!" by bvdl.io. 

Video is used for a large portion of logic and initial code. Minor functionality built atop it to accomplish example programs.

# Language Usage and Information
run python PLInterpreter.py <fileName> to run the interpreter on a text file.

The programming language itself is stack-based. Push and pop are used within certain functions. Conditional and unconditional jumps can be used, with section headers named SECTION <name>

ADD and SUB take 2 values from the stack and push one back

PRINT and READ can be used for I/O. With READ you have to specify if it is a NUM or TEXT you're expecting Really useful PRINT /TOP will print the top value from the stack without popping. (you can also use PRINTINLINE for printing on the same line)

STORE is a size-4 array used for holding values outside of the stack, reminiscent of registers in assembly. you can store the top value from the stack with STORE <position 1-4> and load it back onto the stack by using UNSTORE <position 1-4>

DUPLICATE pushes the top value from the stack onto it again

lastly, STRLEN takes a string and pushes its length onto the stack, and CHARCONVERT pushes each character of a string onto the stack (probably only useful for character counting and string reversing)

Lastly, finish each program with STOP

Example programs are attached along with PLInterpreter.py 
