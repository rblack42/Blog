//Problem Statement:
//If X is the number we want the cube root of, and A is our guess, then X should equal A*A*A.

#include <iostream>
#include <math.h>
using namespace std;

int main(int argc, char * argv[])
{




//Get initial input number 


const double ACCURACY = 0.001;
double Cube = 0.0;
cout << "Type in your guess number for cube root of : \n";
cin >> Cube;

//Make the formula to calculate

 double error;
 double x = Cube;
 double A = x/2;
 
 
 error=A*A*A-Cube;
 if (error<0)
 	error = -error;
 
cout << "Current guess for the cube root is:" <<  A << " This is off by:" << error <<"."<<endl;
 
 while(error>=ACCURACY)
{
	 A = 1.0/3.0 * (x/(A*A) + 2 * A);
	error=A*A*A-Cube;
 	if (error<0)
 	error = -error;
 	
 	cout << "Current guess for the cube root is:" <<  A << " This is off by:" << error << endl <<"."<<endl;
 
	
		
}





}













 
 







