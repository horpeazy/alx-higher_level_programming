#include <stdlib.h>
#include "lists.h"
#include <stdio.h>

/**
 * add_nodepointer - adds a new node at the beginning of a listint_t list
 * @head: pointer to a pointer of the start of the list
 * @p: integer to be included in node
 * Return: address of the new element or NULL if it fails
 */
listpointer_t *add_nodepointer(listpointer_t **head, listint_t *p)
{
	listpointer_t *new;

	new = malloc(sizeof(listpointer_t));
	if (new == NULL)
		return (NULL);

	new->p = p;
	new->next = *head;
	*head = new;

	return (new);
}

/**
 * check_cycle - checks for loop in a list
 * @list: - head node of the linked list
 * Return: 1 - if there is a cylce, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *list_cpy;
	listpointer_t *prev_list, *temp_node;

	list_cpy = list;
	prev_list = NULL;
	while (list_cpy != NULL)
	{
		temp_node = prev_list;
		while (temp_node != NULL)
		{
			if (list_cpy == temp_node->p)
				return (1);
			temp_node = temp_node->next;
		}
		add_nodepointer(&prev_list, list_cpy);
		list_cpy = list_cpy->next;
	}
	return (0);
}
