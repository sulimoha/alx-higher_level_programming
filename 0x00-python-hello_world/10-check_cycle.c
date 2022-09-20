#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it.
* @list:  the head node of the list need to be checked
*
*Return: 0 (no cycle), 1 (cycle)
*/
int check_cycle(listint_t *list)
{
	listint_t  *current;
	listint_t  *post;

	if (!list)
	{
		return (0);
	}
	current = list;
	post = list->next;
	while (post && post->next)
	{
		if (current == post)
		{
			return (1);
		}
		current = current->next;
		post = post->next->next;
	}
	return (0);
}
