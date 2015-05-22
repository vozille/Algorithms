#include <iostream>
#include <cstdlib>
using namespace std;

struct queue
{
	int data;
	struct queue *next;
}queue,*front = NULL,*rear = NULL;

void en_queue(int n)
{
	struct queue *s = (struct queue *)malloc(sizeof(struct queue));
	s->data = n;
	s->next = NULL;
	if(rear == NULL)
	{
		rear = s;
		front = s;
	}
	else
	{
		rear->next = s;
		rear = s;
	}
}

void de_queue()
{
	if(front == NULL)
	{
		cout << "underflow" << '\n';
		rear = NULL;
	}
	else
	{
		struct queue *tmp;
		tmp = front;
		cout << tmp->data << endl;
		front = front->next;
		free(tmp);
	}
}

int main(void)
{
	/*
		Do Testing here
	*/
	
	return 0;
}
