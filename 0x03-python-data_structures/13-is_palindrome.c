#include "lists.h"

/**
 * allocateMem - allocates the memory required for the array
 * @head: a pointer to the head node pf the list
 *
 * Return: allocated array
 */

int *allocateMem(listint_t *head)
{
	int *array;
	size_t size;

	size = 0;
	while (head)
	{
		size++;
		head = head->next;
	}
	array = malloc(sizeof(int) * size);
	if (!array)
	{
		exit(1);
	}
	return (array);
}
/**
 * is_palindrome - a function in C that checks
 * if a singly linked list is a palindrome.
 * @head: a pointer to the head node of the list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int j;
	int *data;

	if (!head || !(*head))
	{
		return (1);
	}
	data = allocateMem(*head);
	temp = *head;
	j = -1;
	while (temp)
	{
		data[++j] = temp->n;
		temp = temp->next;
	}
	temp = *head;
	for (; j >= 0; j--)
	{
		if (data[j] != temp->n)
		{
			free(data);
			return (0);
		}
		temp = temp->next;
	}
	free(data);
	return (1);
}
