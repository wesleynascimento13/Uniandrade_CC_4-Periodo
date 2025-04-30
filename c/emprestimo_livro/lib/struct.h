#ifndef STRUCT_H
#define STRUCT_H

#define MAX_BOOKS 10
#define MAX_BORROWS 3
#define MAX_USERS 10

typedef enum {
    AVAILABLE,
    BORROWED
} BookStatus;

typedef struct {
    char title[100];
    char author[100];
    int total_borrows;
    BookStatus status;
    int borrowed_by;
} Book;

typedef struct {
    char name[100];
    int id;
} User;

#endif
