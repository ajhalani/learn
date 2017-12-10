#include <stdio.h>
#include <stdlib.h>     /* srand, rand */
#include <time.h>       /* time */
#include <iostream>
#include <vector>

using namespace std;

const int arraySize=10;
int printArray(int nums[]) 
{
	for(int i=0; i<arraySize; ++i) {
		if(i!=0)
			cout << ", ";
		cout << nums[i];
	}
	cout << endl;
}

void merge(int nums[], int start, int middle, int end, int temp[]) 
{
	int leftIndex=start;
	int rightIndex=middle;
	for(int i=start; i<end; ++i) {
		if(rightIndex>=end || 
        (leftIndex<middle && (nums[leftIndex] <= nums[rightIndex]))
      ){
			temp[i]=nums[leftIndex];
			leftIndex++;
		}
		else {
			temp[i] = nums[rightIndex];
			rightIndex++;
		}
	}
	for(int i=start; i<end; ++i) 
		nums[i]=temp[i];
}

void mergeSort(int nums[], int start, int size, int temp[])
{
	if(size<2) {
		return;
	}
	int middle = start + size/2;
	mergeSort(nums, start, middle-start, temp);				//sort left
	mergeSort(nums, middle, start+size-middle, temp);	//sort right
  //merge two sorted sub-arrays
  merge(nums, start, middle, start+size, temp);
}

int main()
{
	srand(time(NULL));
	int nums[arraySize];
	int temp[arraySize];
	for(int i=0; i<arraySize; ++i){
		nums[i]= rand()%100;
	}
	printArray(nums);
	mergeSort(nums, 0, arraySize, temp);
	printArray(nums);
	return 0;
}
