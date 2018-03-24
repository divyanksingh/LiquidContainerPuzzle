Problem statement:

There are three vessels of some capacity specified by a tuple as (c1, c2, c3)
Initial filled state of each vessel is given as tuple (i1, i2, i3)
Target state of each vessel is given as tuple (f1, f2, f3)
Check if it is possible to go from initial to final state without using any other vessel, and if possible list down the least number of steps to achieve this.


Script can be run with python3.

Sample run of the script is as below:

Divyanks-MacBook-Pro:Task divyank$ ./solution.py 
Enter capacity:(10,5,2)    
Enter initial_conf:(6,3,0)
Enter final conf:(5,4,0)
Result:  [(6, 3, 0), (4, 5, 0), (2, 5, 2), (7, 0, 2), (7, 2, 0), (5, 2, 2), (5, 4, 0)]


Divyanks-MacBook-Pro:Task divyank$ ./solution.py 
Enter capacity:(10,8,6)
Enter initial_conf:(5,3,2)
Enter final conf:(4,2,4)
Result:  Not possible


tests.py has some test cases for data validation and different set of inputs.

Run the tests as below:

Divyanks-MacBook-Pro:Task divyank$ ./tests.py 
.......
----------------------------------------------------------------------
Ran 7 tests in 0.004s

OK
