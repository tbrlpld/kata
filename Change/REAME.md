Change
====== 

Change is a small program to return a given cent value (between 1 and 99) with the least number of coins. 
E.g. to return 51 cents of change in US coins it would return 2 Quarter and 1 Penny.

The possible coins only use the widely used Penny, Nickel, Dime and Quarter. 
The less commonly used Half-Dollar or Dollar coins are not considered


Testing
-------

I am using `pytest` for testing. To run all the tests, just do 
```bash
$ pytest
```