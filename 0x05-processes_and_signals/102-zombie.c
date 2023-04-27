#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zoombie processes
 *
 * Return: (Always 0)
 */
int main()
{
	int i;
	pid_t child_pid;

	for (i = 0; i < 5; i++)
	{
		child_pid = fork();
		if (child_pid == 0)
		{
			exit(0);
		}
		else
		{
			printf("Zoombie process created, PID: %u\n", child_pid);
		}
	}
	infinite_while();
	return (0);
}
