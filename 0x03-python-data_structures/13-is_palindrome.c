#include "lists.h"

/**
 * check_palindrome - checks if an array is a palindrome
 * @p: pointer to the first element is the array
 *
 * Return: 1 if it is a palindrome 0 otherwise
 */
int check_palindrome(int *p)
{
	int n = 0;
	int *pp = p;
	int i;

	while (*pp != '\0')
	{
		pp++;
		n++;
	}

	for (i = 0; i < (n / 2); i++)
	{
		if (p[i] != p[n-i-1])
			return (0);
	}

	return (1);
}

/**
 * is_palindrome - checked if a linked list is a palindrome
 * @head: pointer to the head
 * Return: 1 for success, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int *array;
	int n = 0;
	int i = 0;
	int j;
	listint_t *temp_head, *temp_node;
	
	temp_head = temp_node = *head;
	while (temp_head != NULL)
	{
		n++;
		temp_head = temp_head->next;
	}
	array = malloc(sizeof(int) * n);

	while (temp_node != NULL)
	{
		array[i++] = temp_node->n;
		temp_node = temp_node->next;
	}
	array[i] = '\0';
	j = check_palindrome(array);
	free(array);
	return (j);
}
