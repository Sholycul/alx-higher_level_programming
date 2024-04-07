#include "lists.h"
#include <stdio.h>

/**
 * reverse_list - Reverse a linked list
 * @head: Pointer to the head node of the list
 *
 * Return: Pointer to the head of the reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL, *current = head, *next_node = NULL;

	while (current != NULL)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}

	return (prev);
}

/**
 * compare_lists - Compare two linked lists
 * @head1: Pointer to the head node of the first list
 * @head2: Pointer to the head node of the second list
 *
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 && head2)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (1);
}

/**
 * is_palindrome - Check if a singly linked list is a palindrome
 * @head: Pointer to the pointer to the head node of the list
 *
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head, *second_half = NULL;
	listint_t *prev_slow_ptr = *head, *mid_node = NULL;

	int is_palindrome = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast_ptr != NULL && fast_ptr->next != NULL)
		{
			fast_ptr = fast_ptr->next->next;
			prev_slow_ptr = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		if (fast_ptr != NULL)
		{
			mid_node = slow_ptr;
			slow_ptr = slow_ptr->next;
		}

		second_half = slow_ptr;
		prev_slow_ptr->next = NULL;
		second_half = reverse_list(second_half);

		is_palindrome = compare_lists(*head, second_half);

		second_half = reverse_list(second_half);

		if (mid_node != NULL)
		{
			prev_slow_ptr->next = mid_node;
			mid_node->next = second_half;
		}
		else
		{
			prev_slow_ptr->next = second_half;
		}
	}

	return (is_palindrome);
}

