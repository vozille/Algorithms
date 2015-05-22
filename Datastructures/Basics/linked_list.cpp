#include <iostream>
#include <cstdlib>
using namespace std;

struct list
{
	int data;
	struct list *next;
}list,*start = NULL;

void init(int n)
{
	struct list *s,*curr;
	s = (struct list *)malloc(sizeof(struct list));
	s->data = n;
	s->next = NULL;
	if(start == NULL)
	{
		start = s;
		curr = s;
	}
	else
	{
		curr->next = s;
		curr = s;
	}
}

void traverse()
{
	struct list *i = start;
	while(i != NULL)
	{
		cout << i->data << " ";
		i = i->next;
	}
	cout << '\n';
}

void insert_element_at_start(int x)
{
	struct list *new_list;
	new_list = (struct list *)malloc(sizeof(struct list));
	new_list->data = x;
	new_list->next = start;
	start = new_list;
}

void insert_element_at_end(int x)
{
	struct list *new_list, *i;
	i = start;
	new_list = (struct list *)malloc(sizeof(struct list));
	new_list->data = x;
	new_list->next = NULL;

	while(i->next != NULL)
	{
		i = i->next;
	}
	i->next = new_list;
}

void insert_element_at_pos(int x, int pos)
{
	struct list *list_pos,*i,*j;
	i = start;
	j = start;
	list_pos = (struct list *)malloc(sizeof(struct list));
	list_pos->data = x;
	if(pos == 0)
	{
		insert_element_at_start(x);
	}
	else
	{
		while(pos > 1)
		{
			i = i->next;
			j = j->next;
			pos--;
		}
		j = j->next;
		i->next = list_pos;
		list_pos->next = j;
	}
}

void delete_element_at_pos(int pos)
{
	struct list *i,*j,*tmp;
	i = start;
	j = start;
	while(pos > 1)
	{
		i = i->next;
		j = j->next;
		pos--;
	}
	j = j->next;
	tmp = j;
	j = j->next;
	i->next = j;
	free(tmp);
}

void reverse()
{
	struct list *i,*j,*k;
	i = NULL;
	j = start;
	while(j != NULL)
	{
		k = j->next;
		j->next = i;
		i = j;
		j = k;
	}
	start = i;
}

int main(void)
{
	for(int i = 1; i <=5; i++)
		init(i);
	/*
		Do testing here
	*/
	return 0;
}
