#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp, *newnode;
	newnode = (listint_t *) malloc(sizeof(listint_t));
	
	tmp = *head;
	if (newnode == NULL)
	{
		return (NULL);
	}

	newnode->n = number;
	
	if (*head == NULL || tmp->n >= number)
	{
		newnode->next = tmp;
		*head = newnode;
		return (newnode);
	}

	while (tmp->next && tmp->next->n < number)
	{
		tmp = tmp->next;
	}
	
	newnode->next = tmp->next;
	tmp->next = newnode;
	return (newnode);
}
