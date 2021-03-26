# programming_assignments_auto-grader

Written in python. this code can be optimized to auto-grade programming assignments with given test cases.

Tasks that are performed by this grader:
1) Find paths to all the submission folders (of students).
2) Copy the orginal test cases to every folder.
3) Run the tests for every student by changing the current working directory. This is done by looping over all the paths to the submission folders. While running tests the following cases are dealt with.
   i) Programs that fail to compile e.g due to syntax error
   ii) Programs that fail to execute e.g due to segmentation faults or exceptions
   iii) Programs that are caught in infinite loops
