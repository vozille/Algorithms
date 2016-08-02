#include <iostream>
#include <cstdlib>
using namespace std;

struct doubly_linked_list
{
	int data;
	struct doubly_linked_list *next,*prev;
}doubly_linked_list,*start = NULL,*end = NULL;

//TODO : use the *end pointer

void insert_at_front(int n)
{
	struct doubly_linked_list *s = (struct doubly_linked_list *)malloc(sizeof(struct doubly_linked_list));
	s->data = n;
	s->next = start;
	s->prev = NULL;
	if(start != NULL)
		start->prev = s;
	start = s;
}

void insert_at_back(int n)
{
	struct doubly_linked_list *i,*s = (struct doubly_linked_list *)malloc(sizeof(struct doubly_linked_list));
	s->data = n;
	s->next = NULL;
	if(start == NULL)
	{
		s->prev = NULL;
		start = s;
	}
	else
	{
		i = start;
		while(i->next != NULL)
			i=i->next;
		i->next = s;
		s->prev = i;
	}
}

void traverse_forward()
{
	struct doubly_linked_list *i;
	i = start;
	while(i != NULL)
	{
		cout << i->data << ' ';
		i = i->next;
	}
	cout << endl;
}

void traverse_backward()
{
	struct doubly_linked_list *i;
	i = start;
	while(i->next != NULL)
	{
		i = i->next;
	}
	while(i != NULL)
	{
		cout << i->data << ' ';
		i = i->prev;
	}
	cout << '\n';
}

void insert_after(int n,int pos)
{
	struct doubly_linked_list *i,*j,*s = (struct doubly_linked_list *)malloc(sizeof(struct doubly_linked_list));
	s->data = n;
	i = start;
	j = start;
	while(pos > 1)
	{
		i = i->next;
		pos--;
	}
	j = i;
	j = j->next;

	s->next = j;
	j->prev = s;
	s->prev = i;
	i->next = s;
}

int main(void)
{
	/*
		Do Testing here
	*/

	insert_at_front(1);
	insert_at_back(2);
	insert_at_front(55);
	insert_at_back(3);
	insert_at_front(11);
	insert_at_front(75);
	traverse_forward();
	insert_after(20,3);
	traverse_forward();
	return 0;
}
