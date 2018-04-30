#include<iostream>
#include<cstdlib>
using namespace std;

struct node {
	int data;
	struct node *left;
	struct node *right;
};

struct node *addNode(int data) {
		struct node* node = (struct node*)malloc(sizeof(struct node));
		node->data = data;
		node -> left = NULL;
		node->right = NULL;
		return node;
}
void printInorder(struct node *node) {
	if (node == NULL){
		return;
	}
	printInorder(node->left);
	cout<< node->data<<endl;
	printInorder(node->right);
}

void printPostorder(struct node *node){
	if (node == NULL){
                return;
        }
	printPostorder(node->left);
	printPostorder(node->right);
	cout<<node->data<<endl;
}
void printPreorder(struct node *node) {
	if (node == NULL){
		return;
	}
	cout << node -> data <<endl;
	printPreorder(node->left);
	printPreorder(node->right);
}
int main() {
	struct node *node = addNode(5);
	node->left = addNode(6);
	node->right = addNode(3);
	node->right->right = addNode(8);
	node->left->right = addNode(2);
	node->left->left = addNode(9);
	node->right->left = addNode(1);
	printInorder(node);
	cout<< "................."<<endl;
	printPostorder(node);
	cout<<".................."<<endl;
	printPreorder(node);
}

	
