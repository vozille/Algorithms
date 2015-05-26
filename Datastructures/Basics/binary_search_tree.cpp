#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <vector>
using namespace std;

struct btree
{
	int data;
	struct btree *left,*right;
}btree;

struct btree *add_node(int n)
{
	struct btree *s = (struct btree *)malloc(sizeof(struct btree));
	s->data = n;
	s->left = NULL;
	s->right = NULL;
	return s;
}

int count(struct btree *tree)
{
	struct btree *s = tree;
	if(s == NULL)
		return 0;
	else
		return count(s->left)+count(s->right)+1;
}

void traverse_inorder(struct btree *tree)
{
	struct btree *s = tree;
	if(s == NULL)
		return;
	traverse_inorder(s->left);
	cout << s->data << ' ';
	traverse_inorder(s->right);
}

void get_nodes(struct btree *tree, vector <int> &arr)
{
	struct btree *s = tree;
	if(s == NULL)
		return;
	get_nodes(s->left,arr);
	arr.push_back(s->data);
	get_nodes(s->right,arr);
}

void convert_to_BST(struct btree *tree,vector <int> &arr)
{
	struct btree *bst = tree;
	vector<int>::iterator k;
	k = arr.begin();
	if(bst == NULL)
		return;
	convert_to_BST(bst->left,arr);
	bst->data = *k;
	arr.erase(k);
	convert_to_BST(bst->right,arr);
}


void search_node_bst(struct btree *tree,int n,string foo)
{
	struct btree *s = tree;
	string ans = foo;
	if(s == NULL or s->data == n)
	{
		cout << ans << endl;
		return;
	}
	else if(s->data < n)
	{
		ans += "->right";
		search_node_bst(s->right,n,ans);
	}
	else
	{
		ans += "->left";
		search_node_bst(s->left,n,ans);
	}
}

int main(void)
{
	struct btree *s;
	s = add_node(11);
	s->left = add_node(2);
	s->left->left = add_node(8);
	s->left->right = add_node(1);
	s->right = add_node(7);
	int i,n = count(s);
	vector <int> arr;
	get_nodes(s,arr);
	sort(arr.begin(),arr.end());

	struct btree *fff = s;
	convert_to_BST(fff,arr);
	//traverse_inorder(fff);
	search_node_bst(fff,1,"root");

	return 0;
}
