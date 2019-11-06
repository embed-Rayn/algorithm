#include<stdio.h>
int main(void){
	int i, j, k, temp;
	int array[10] = {1, 10, 5, 9, 8, 7, 6, 4, 3, 2};
	for(i = 1; i < 10; i++){
		j = i;
		while(array[j] > array[j + 1]){
			temp = array[j];
			array[j] = array[j + 1];
			array[j + 1] = temp;
			j--;
		}
	}
	for(i = 0; i < 10; i++){
		printf("%d ", array[i]);
	}
	
	//기준보다 왼쪽은 항상 정렬이 되어있다는 가정하에 기준점 정렬
	//데이터가 가의 정렬된 상태에서 가장 효율정 
	return 0;
}
