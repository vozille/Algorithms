#include <iostream>
#include <cstdlib>
using namespace std;

struct stack
{
	int data;
	struct stack *next;
}stack,*top = NULL;

void push(int n)
{
	struct stack *s = (struct stack *)malloc(sizeof(struct stack));
	s->data = n;
	s->next = top;
	top = s;
}

void pop()
{
	if(top == NULL)
		cout << "underflow" <<'\n';
	else
	{
		cout << top->data << endl;
		struct stack *tmp;
		tmp = top;
		top = top->next;
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
