#include <iostream> 
#include <vector>	//vector container
#include <cstring> //just in case you want to use characters

using namespace std;

/*
	using vectors allows you to perform merge sort by passing a single variable
	to a function. Also better memory management

	Frankly using arrays is a bit childish
*/

/*
	Merge sort is one of the most time efficient soting algorithms out 
	there. My code uses vectors to sort a list of numbers in O(nlog(n))
	average time.

	Merge sort works on the principle of divide and conquer.
*/

void msort(vector<int>&arr) //pass by reference
{
	vector<int>left; // split the list
	vector<int>right;
	vector<int>::iterator i,j,k;
	if((arr.size())>1)
	{
		for(i=arr.begin();i<(arr.begin()+arr.size()/2);++i)
			left.push_back(*i);
		for(i=(arr.begin()+arr.size()/2);i!=arr.end();++i)
			right.push_back(*i);

		msort(left);
		msort(right); //recursively sort the individual factions

		i=left.begin();
		j=right.begin();
		k=arr.begin();

		while((i!=left.end())&&(j!=right.end()))
		{
			if(*i<*j)	//sorts in ascending order. Reverse 
						//inequality to sort in descending.
			{
				*k=*i;
				++i;
				++k;
			}
			else
			{
				*k=*j;
				++j;
				++k;
			}
		}
		while(i!=left.end())
		{
			*k=*i;
			++i;
			++k;
		}
		while(j!=right.end())
		{
			*k=*j;
			++j;
			++k;
		}
	}
}

//driver program

int main(void)
{
	vector<int>v;
	vector<int>::iterator i;
	for(int j=5;j>=0;j--)	//sample testcase
		v.push_back(j);
	msort(v);
	for(i=v.begin();i!=v.end();++i)
		cout<<*i<<" ";
	return 0;
}
