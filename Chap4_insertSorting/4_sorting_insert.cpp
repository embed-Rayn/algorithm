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
	
	//���غ��� ������ �׻� ������ �Ǿ��ִٴ� �����Ͽ� ������ ����
	//�����Ͱ� ���� ���ĵ� ���¿��� ���� ȿ���� 
	return 0;
}
