#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: a pointer to the head node
 * @number: a number to be inserted
 * 
 * Return: new node adress after insertion or NULL if faild
 */ 
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *temp;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
    {
        return (NULL);
    }
    new->n = number;
    new->next = NULL;
    if(*head == NULL || (*head)->n > number)
    {
        new->next = *head;
        *head = new;
        return (new);
    }
    temp = *head;
    while(temp != NULL && temp->next != NULL)
    {
        if (temp->next->n > number)
        {
            break;
        }
        temp = temp->next;
    }
    new->next = temp->next;
    temp->next = new;
    return (new);
}