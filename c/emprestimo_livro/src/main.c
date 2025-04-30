#ifndef MAIN_H
#define MAIN_H

/*
** Douglas Nascimento
** Wesley Vilgino do Nascimento
*/

#include "../lib/functions.h"
#include "../lib/clear.h"

int main() {
    Book library[MAX_BOOKS];
    User users[MAX_USERS];
    int userCount = 0;
    int loggedInUser;
    char inputName[100];

    initializeBooks(library, MAX_BOOKS);
    initializeUsers(users, &userCount);

    printf("Enter your name: ");
    fgets(inputName, sizeof(inputName), stdin);
    inputName[strcspn(inputName, "\n")] = '\0';

    int created = createdUser(users, userCount, inputName);
    if (created == -1) {
        loggedInUser = addUser(users, &userCount, inputName);
        printf("Welcome, %s! Your ID is %d\n", users[loggedInUser].name, users[loggedInUser].id);
    }

    int option, bookId;

    do {
        printf("\n=== BOOK LOAN SYSTEM ===\n");
        printf("1. List all books\n");
        printf("2. Borrow a book\n");
        printf("3. Return a book\n");
        printf("4. Show library report\n");
        printf("5. Show my borrowed books\n");
        printf("0. Exit\n");
        printf("Choose an option: ");
        scanf("%d", &option);

        switch (option) {
            case 1:
                clear2();
                listBooks(library, MAX_BOOKS);
                break;
            case 2:
                clear2();
                printf("Enter book ID to borrow (1 to %d): ", MAX_BOOKS);
                scanf("%d", &bookId);
                bookId--;
                if (bookId >= 0 && bookId < MAX_BOOKS) {
                    borrowBook(&library[bookId], loggedInUser);
                } else {
                    clear2();
                    printf("Invalid book ID.\n");
                }
                break;
            case 3:
                clear2();
                printf("Enter book ID to return (1 to %d): ", MAX_BOOKS);
                scanf("%d", &bookId);
                bookId--;
                if (bookId >= 0 && bookId < MAX_BOOKS) {
                    returnBook(&library[bookId], loggedInUser);
                } else {
                    clear2();
                    printf("Invalid book ID.\n");
                }
                break;
            case 4:
                clear2();
                showLibraryReport(library, MAX_BOOKS);
                break;
            case 5:
                clear2();
                showUserBooks(library, MAX_BOOKS, &users[loggedInUser]);
                break;
            case 0:
                clear2();
                printf("Exiting program...\n");
                break;
            default:
                clear2();
                printf("Invalid option.\n");
        }

    } while (option != 0);

    return 0;
}
#endif
