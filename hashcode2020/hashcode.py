#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import sys
import copy

if (sys.argv.__len__() != 2):
    print("Invalid number of arguments\n")
    exit(1)

#############################
#        Variables
#############################
file_in = "./input/" + sys.argv[1] + ".txt"
file_out = "./output/" + sys.argv[1] + ".out"


n_different_books = 0
n_libraries = 0
n_days = 0
books = []
libraries = []


# ongoing proccesing books
processing_books = []

# libraries not singed up yet
available_libraries = []
available_libraries_status = []
current_day = 0

solution = [] # [(lib_index_to_sign_up, books), ...]

#############################
#        Functions
#############################
def read():
    global file_in, n_different_books, n_libraries, n_days, books
    global libraries, available_libraries, processing_books
    input_file = open(file_in, "r")
    first_line = [int(x) for x in input_file.readline().split(" ")]
    n_different_books = first_line[0]
    n_libraries = first_line[1]
    n_days = first_line[2]

    books = [int(x) for x in input_file.readline().split(" ")]
    for i in range(len(books)):
        books[i] = (i, books[i])
    processing_books = [False for _ in books]

    for i in range(n_libraries):
        first_line = [int(x) for x in input_file.readline().split(" ")]
        book_ids = [int(x) for x in input_file.readline().split(" ")]
        book_ids = sorted(book_ids, key=lambda x: books[x][1], reverse=True) # order by book score

        library_data = (i, first_line[0], first_line[1], first_line[2])
        libraries.append((library_data, book_ids))

    input_file.close()


def library_index(library):
    return library[0][0]

def n_books(library):
    return library[0][1]

def sign_up_time(library):
    return library[0][2]

def n_ships_day(library):
    return library[0][3]

def book_index(book):
    return book[0]

def book_score_from_index(book_index):
    return books[book_index][1]

def get_books_idxs(library):
    return library[1]



def write():
    global file_out
    output_file = open(file_out, "w")
    output_file.write(str(len(solution)))
    output_file.write("\n")
    for lib in solution:
        output_file.write(str(lib[0]))
        output_file.write(" ")
        output_file.write(str(len(lib[1])))
        output_file.write("\n")
        for book in lib[1]:
            output_file.write(str(book))
            output_file.write(" ")
        output_file.write("\n")
    output_file.write("\n")
    output_file.close()

# Books can be scanned in time
def get_books_to_send(library):
    days_available = n_days - current_day - sign_up_time(library)
    n_books_send = min(n_books(library), days_available * n_ships_day(library))
    return [book_idx for book_idx in get_books_idxs(library)[:n_books_send] if not processing_books[book_idx]]

# Returns the score of a library
def get_library_score(library):
    score = 0
    for book_idx in get_books_to_send(library):
        score += book_score_from_index(book_idx)
    return score / sign_up_time(library)

# Returns the library with best score
def best_library():
    scores = [(library, get_library_score(library)) for library in available_libraries]
    scores.sort(key = lambda x : x[1], reverse = True)
    return scores[0]

# Updates the books to send in the future
def update_used_books(books):
    for book_idx in books:
        processing_books[book_idx] = True

#############################
#        Program
#############################


read()
available_libraries = copy.deepcopy(libraries)
available_libraries_status = [True for _ in range(len(available_libraries))]

while (current_day < n_days and len(available_libraries) > 0):
    selected_library, score = best_library()
    if score == 0: break
    sent = get_books_to_send(selected_library)
    solution.append((library_index(selected_library),sent))
    update_used_books(sent)
    current_day += sign_up_time(selected_library)
    available_libraries.remove(selected_library)

write()
