#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdio.h>
#include <string.h>
#include "struct.h"

void initializeBooks(Book *books, int count) {
    const char *titles[MAX_BOOKS] = {
        "Dom Casmurro", "O Cortico", "A Hora da Estrela", "Capitaes da Areia", "Iracema",
        "Vidas Secas", "O Quinze", "A Moreninha", "Bras Cubas", "O Guarani"
    };

    const char *authors[MAX_BOOKS] = {
        "Machado de Assis", "Aloisio Azevedo", "Clarice Lispector", "Jorge Amado", "Jose de Alencar",
        "Graciliano Ramos", "Rachel de Queiroz", "Joaquim M. de Macedo", "Machado de Assis", "Jose de Alencar"
    };

    for (int i = 0; i < count; i++) {
        strcpy(books[i].title, titles[i]);
        strcpy(books[i].author, authors[i]);
        books[i].total_borrows = 0;
        books[i].status = AVAILABLE;
        books[i].borrowed_by = -1;
    }
}

void initializeUsers(User *users, int *userCount) {
    *userCount = 0;
}

int createdUser(User *users, int count, const char *name) {
    for (int i = 0; i < count; i++) {
        if (strcmp(users[i].name, name) == 0) {
            return i;
        }
    }
    return -1;
}

int addUser(User *users, int *count, const char *name) {
    if (*count >= MAX_USERS) {
        printf("User limit reached.\n");
        return -1;
    }
    strcpy(users[*count].name, name);
    users[*count].id = *count;
    (*count)++;
    return *count - 1;
}

void borrowBook(Book *book, int userId) {
    if (book->status == BORROWED) {
        printf("This book is already borrowed.\n");
    } else if (book->total_borrows >= MAX_BORROWS) {
        printf("Borrow limit reached for this book.\n");
    } else {
        book->status = BORROWED;
        book->total_borrows++;
        book->borrowed_by = userId;
        printf("Book borrowed successfully.\n");
    }
}

void returnBook(Book *book, int userId) {
    if (book->status == AVAILABLE) {
        printf("This book is already available.\n");
    } else if (book->borrowed_by != userId) {
        printf("You cannot return a book you haven't borrowed.\n");
    } else {
        book->status = AVAILABLE;
        book->borrowed_by = -1;
        printf("Book returned successfully.\n");
    }
}

void printBook(const Book *book) {
    printf("Title: %s\n", book->title);
    printf("Author: %s\n", book->author);
    printf("Total Borrows: %d\n", book->total_borrows);
    printf("Status: %s\n\n", book->status == AVAILABLE ? "Available" : "Borrowed");
}

void listBooks(const Book *books, int count) {
    for (int i = 0; i < count; i++) {
        printf("=== BOOK [%d] ===\n", i + 1);
        printBook(&books[i]);
    }
}

void showLibraryReport(const Book *books, int count) {
    int available = 0, borrowed = 0;
    for (int i = 0; i < count; i++) {
        if (books[i].status == AVAILABLE) available++;
        else borrowed++;
    }
    printf("\n=== LIBRARY REPORT ===\n");
    printf("Total books: %d\nAvailable: %d\nBorrowed: %d\n", count, available, borrowed);
}

void showUserBooks(const Book *books, int count, const User *user) {
    printf("\nBooks borrowed by %s:\n", user->name);
    int found = 0;
    for (int i = 0; i < count; i++) {
        if (books[i].borrowed_by == user->id) {
            printf(" - %s by %s\n", books[i].title, books[i].author);
            found = 1;
        }
    }
    if (!found) {
        printf("No books currently borrowed.\n");
    }
}
#endif
