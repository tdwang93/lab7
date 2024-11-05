#!/usr/bin/env python3
# Student ID: twangmo12

def function1():
    global schoolName  # Make `schoolName` global so that changes here affect the global scope
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # `schoolName` already global; changes will affect the global scope
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'
print('print() in main on schoolName:', schoolName)
function1()
print('print() in main on schoolName:', schoolName)
function2()
print('print() in main on schoolName:', schoolName)
