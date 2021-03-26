# programming_assignments_auto-grader

Written in python. this code can be optimized to auto-grade programming assignments with test cases.

Tasks that are performed by this grader:
1) Find paths to all the submission folders (of all students).
2) Copy the orginal test cases to every folder.
3) Run the tests for every student by changing the current working directory. This is done by looping over all the paths to the submission folders. While running tests the following cases are dealt with. <br>
   i) Programs that fail to compile e.g due to syntax error <br>
   ii) Programs that fail to execute e.g due to segmentation faults or exceptions <br>
   iii) Programs that are caught in infinite loops
4) The tests results in the form of stdout are captured in a file and with string manipulation the relevant scores are stored.
5) For every submission, a row is appended to the csv file.
