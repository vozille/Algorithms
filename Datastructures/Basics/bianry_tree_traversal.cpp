#include <iostream>
#include <cstdlib>
using namespace std;
#define line() cout << '\n';
struct btree
{
	int data;
	struct btree *left,*right;
}btree;

struct btree *new_node(int n)
{
	struct btree *s = (struct btree *)malloc(sizeof(struct btree));
	s->data = n;
	s->left = NULL;
	s->right = NULL;
	return s;
}

void inorder_traverse(struct btree *new_tree)
{
	struct btree *s = new_tree;
	if(s == NULL)
		return;
	inorder_traverse(s->left);
	cout << s->data << " ";
	inorder_traverse(s->right);
}

void postorder_traverse(struct btree *new_tree)
{
	struct btree *s = new_tree;
	if(s == NULL)
		return;
	postorder_traverse(s->left);
	postorder_traverse(s->right);
	cout << s->data << ' ';
}

void preorder_traverse(struct btree *new_tree)
{
	struct btree *s = new_tree;
	if(s == NULL)
		return;
	cout << s->data << ' ';
	preorder_traverse(s->left);
	preorder_traverse(s->right);
}

int main(void)
{
	struct btree *new_tree = new_node(12);
	new_tree->left = new_node(25);
	new_tree->right = new_node(11);
	new_tree->left->left = new_node(1);
	new_tree->left->right = new_node(2);
	inorder_traverse(new_tree);
	line();
	postorder_traverse(new_tree);
	line();
	preorder_traverse(new_tree);
	line();
	return 0;
}
