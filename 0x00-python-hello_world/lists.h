#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;


/**
 * struct listpointer_s - singly linked list
 * @p: pointer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * 
 */
typedef struct listpointer_s
{
    listint_t *p;
    struct listpointer_s *next;
} listpointer_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
listpointer_t *add_nodepointer(listpointer_t **head, listint_t *p);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

#endif /* LISTS_H */
