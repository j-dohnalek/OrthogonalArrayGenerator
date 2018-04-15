# OrthogonalArrayGenerator
Simple python 2.7 tool to generate orthogonal arrays for Orthogonal Array Testing
 
### How to apply Orthogonal Array Testing?
https://www.guru99.com/orthogonal-array-testing.html

### Required libraries

```
pip install OApackage
```

## Example usage

A Web page has three distinct sections (Top, Middle, Bottom) that can be individually shown or hidden from user

* No of Factors = 3 (Top, Middle, Bottom)
* No of Levels (Visibility) = 2 (Hidden or Shown)
* Array Type = L4(23)

<pre>
Test Cases 	TOP        Middle     Bottom
Test #1     Hidden     Hidden     Hidden
Test #2     Hidden     Visible    Visible
Test #3     Visible    Hidden     Visible
Test #4     Visible    Visible    Hidden
</pre>
Generate the test array (0-Hidden; 1-Visible)
```
>> python orthogonalArray.py 2 4 3
0   0   0
0   1   1
1   0   0
1   1   1
```

## Credits
http://www.pietereendebak.nl/oapackage/

Credits go to:

* [Complete Enumeration of Pure-Level and Mixed-Level Orthogonal Arrays](http://dx.doi.org/10.1002/jcd.20236), E.D. Schoen, P.T. Eendebak, M.V.M. Nguyen, Volume 18, Issue 2, pages 123-140, 2010.
* [Two-Level Designs to Estimate All Main Effects and Two-Factor Interactions](https://doi.org/10.1080/00401706.2016.1142903), Pieter T. Eendebak, Eric D. Schoen, Technometrics Vol. 59 , Iss. 1, 2017

The code was written by:

* Pieter Eendebak <pieter.eendebak@gmail.com>
* Vincent Brouerius van Nidek
* Alan Vazquez-Alcocer

Ideas contributed by:

* Eric Schoen <eric.schoen@tno.nl>
* Alan Vazquez-Alcocer <alanrvazquez@gmail.com>
