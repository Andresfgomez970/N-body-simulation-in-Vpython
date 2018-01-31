# N-body-simulation-in-Vpython

The N-bodies problem is well known in the literature. One of its future is the lack of an analytical solution for every instant of time. Nevertheless, is possible to coumpute the following instants of time knowing an inicial configuration (the mass, inicial position and inicial velocity of ecah body).

## Getting Started 

The program takes a file with the following form: 

m px   py  pz  vx  vy  vz
----------------------------------------
m1 x11 x12 x13 v11 v12 v13
+
+
mi xi1 xi2 xi3 vi1 vi2 vi3
+
+
mN xN1 xN2 xN3 vN1 vN2 vN3
-----------------------------------------

where pi is position in the i-axis, vi is the velocity on the i-axis, and m the mass (mi the one of the ith-body). So, xi2 is for example the intial position on y of the body i.   

Several sonfigurations can be found in the files with termination ".ap"


## Prerequisites

To run this program you need to have installed the folowing libaries of python: scipy.constants, visual (6 version), and numpy.

## Runing the program 

It is only necessary to change the input in the generate funtion in the file  

generate('SSthrid.ap')


## Built With

* [Python](https://www.python.org/) 
* [Vpython](https://www.python.org/) 

## Authors

* **Andrés Felipe Gómez** - *Initial work without classes implentation* -
* **Luis Abelardo Papiernik** - *Actual code* -

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## References

* [Python](https://www.python.org/) 

## Acknowledgments

* Thanks Luis for helping me and explainme how to manage classes to write this code as is actually right know. 
