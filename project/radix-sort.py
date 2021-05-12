import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    #make inner function counting_sort to use for radix
    def counting_sort(idx, lst):
        counts = [0] * 127
        new = [0] * len(lst)
        counter = 0
        #loop through list to fill up first list with decoded number vals
        while counter<len(lst):
            if idx <= len(lst[counter]) - 1:
                i = ord(lst[counter].decode('ascii')[idx])
            else:
                i = 0
            counter += 1
            counts[i] += 1
        #reset counter for next loop
        counter = 0
        while counter<len(counts)-1:
            counts[counter+1] += counts[counter]
            counter += 1
        #loop to fill new list with updated order
        counter = len(lst) - 1
        while counter>=0:
            if idx <= len(lst[counter]) - 1:
                i = ord(lst[counter].decode('ascii')[idx])
            else:
                i = 0
            new[counts[i]-1] = lst[counter]
            counts[i] -= 1
            counter -= 1
        return new
    
    words = book_to_words()
    input_max = max([len(i) for i in words]) + 1
    #use max word length & counting sort to sort list of words in book
    sorted_lst = counting_sort(input_max, words)
    input_max -= 1
    #loop and update sorted list
    for i in range(input_max, -1, -1):
        sorted_lst = counting_sort(i, sorted_lst)
    return sorted_lst
    
