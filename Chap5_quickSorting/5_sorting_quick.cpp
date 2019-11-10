#include<stdio.h>

int num = 10;
int array2[10] = {1, 10, 5, 9, 8, 7, 6, 4, 3, 2};
int array[10] = {10, 9, 8, 7 ,6 ,5, 4, 3, 2, 1};
void quickSort(int * data, int start, int end){
	if (start >= end){	//원소가 1개 이하인 경우 
		return;
	}
	int key = start;
	int i = start + 1;
	int j = end;
	int temp;
	 
	while(i <= j){ //큰 값과 작은 값이 엇갈릴때까지 
		while(data[i] <= data[key]){ //키 값보다 큰 것을 찾아 오른쪽으로 
			i++;
		}
		while(data[j] >= data[key] && j > start){ //키 값보다 작은 것을 찾아 왼쪽으로 
			j--;
		}
		if (i > j){
			temp = data[j];
			data[j] = data[key];
			data[key] = temp;
		}
		else{
			temp = data[j];
			data[j] = data[i];
			data[i] = temp;
		}
		quickSort(data, start, j - 1);
		quickSort(data, j + 1, end);
	}
}
int main (void){
	quickSort(array, 0, num - 1);
	
	for(int i = 0; i < num; i++){
		printf("%d ", array[i]);
	}
	return 0;
}
