#include "lists.h"

/**
 * insert_node - insert a node into a linked list
 * @head: head node
 * @number: value of node
 * Return: address of node of success, NULL if fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *prev_node, *temp_node, *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	prev_node = NULL;
	temp_node = *head;
	if (!temp_node)
	{
		new_node->n = number;
		new_node->next = NULL;
		return (new_node);
	}
	while (temp_node)
	{
		if (temp_node->n >= number)
		{
			if (prev_node != NULL)
				prev_node->next = new_node;
			new_node->n = number;
			new_node->next = temp_node;
			return (new_node);
		}
		prev_node = temp_node;
		temp_node = temp_node->next;
	}
	prev_node->next = new_node;
	new_node->n = number;
	new_node->next = NULL;
	return (new_node);
}
