// SPDX-License-Identifier: GPL-3.0
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

struct service {
	char description[20];
	int price;
	struct service *next;
};

struct service_queue {
	struct service *begin;
	struct service *end;
	int size;
};

void enqueue(struct service_queue **q, struct service *s)
{

	if ((*q)->begin == NULL && (*q)->end == NULL) {
		(*q)->begin = s;
		(*q)->end = s;
	} else {
		struct service *tmp = (*q)->end;

		tmp->next = s;
		(*q)->end = s;
	}
	(*q)->size++;
}

void dequeue(struct service_queue **q)
{
	if ((*q)->begin != NULL && (*q)->end != NULL) {
		struct service *tmp = (*q)->begin;

		if ((*q)->begin == (*q)->end) {
			(*q)->begin = NULL;
			(*q)->end = NULL;
		} else {
			(*q)->begin = tmp->next;
		}
		free(tmp);
		(*q)->size--;
	}

}

void create_nfe(int size, char services[size][20])
{
	struct service_queue *service_q;

	service_q = (struct service_queue *) malloc(sizeof(struct service_queue));
	service_q->begin = NULL;
	service_q->end = NULL;
	service_q->size = 0;

	for (int i = 0; i < size; i += 2) {
		struct service *new;

		new = (struct service *) malloc(sizeof(struct service));
		new->next = NULL;
		strcpy(new->description, services[i]);
		new->price = atoi(services[i + 1]);
		enqueue(&service_q, new);
	}
	FILE * nfe = fopen("nfe.txt", "w");

	fprintf(nfe, "%s\n", "===== NOTA FISCAL ELETRÔNICA =====");
	fprintf(nfe, "%10s\t\t%5s\n", "PRODUTO", "PREÇO");
	int queue_size = service_q->size;
	int total = 0;

	for (int i = 0; i < queue_size; i++) {
		fprintf(nfe, "%10s\t\t%3d\n", service_q->begin->description, service_q->begin->price);
		total += service_q->begin->price;
		dequeue(&service_q);
	}
	fprintf(nfe, "\tTOTAL:\t\tR$ %d\n", total);
	fclose(nfe);
}

void create_nfe_2(void)
{
	struct service_queue *service_q;

	service_q = (struct service_queue *) malloc(sizeof(struct service_queue));
	service_q->begin = NULL;
	service_q->end = NULL;
	service_q->size = 0;

	int size = 0;
	char buffer[20];
	FILE *temp = fopen("temp.txt", "r");

	fgets(buffer, 20, temp);
	buffer[strcspn(buffer, "\n")] = 0;
	size = atoi(buffer);
	printf("%d\n", size);
	char services[size][20];

	for (int i = 0; i < size; i++) {
		fgets(buffer, 20, temp);
		buffer[strcspn(buffer, "\n")] = 0;
		strcpy(services[i], buffer);
	}
	fclose(temp);

	for (int i = 0; i < size; i += 2) {
		struct service *new;

		new = (struct service *) malloc(sizeof(struct service));
		new->next = NULL;
		strcpy(new->description, services[i]);
		new->price = atoi(services[i + 1]);
		enqueue(&service_q, new);
	}
	FILE *nfe = fopen("nfe.txt", "w");

	fprintf(nfe, "%s\n", "===== NOTA FISCAL ELETRÔNICA =====");
	fprintf(nfe, "%10s\t\t%5s\n", "PRODUTO", "PREÇO");
	int queue_size = service_q->size;
	int total = 0;

	for (int i = 0; i < queue_size; i++) {
		fprintf(nfe, "%10s\t\t%3d\n", service_q->begin->description, service_q->begin->price);
		total += service_q->begin->price;
		dequeue(&service_q);
	}
	fprintf(nfe, "\tTOTAL:\t\tR$ %d\n", total);
	fclose(nfe);
}


// int main(void)
// {
// char services_buffer[20];
// char services_arr[4][20];

// printf("Digite os servicos:\n");
// for (int i = 0; i < 4; i++) {
// fgets(services_buffer, 20, stdin);
// services_buffer[strcspn(services_buffer, "\n")] = 0;
// strcpy(services_arr[i], services_buffer);
// }

// for (int i = 0; i < 4; i++)
// printf("%s%s", services_arr[i], (i == 3) ? "\n" : ", ");
// create_nfe(4, services_arr);
// printf("Nota fiscal gerada com sucesso\n");

// }
