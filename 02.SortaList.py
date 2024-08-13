def sortlistofnumbers(listofnumbers,sorttype):
    if sorttype == "asc":
        return sorted(listofnumbers)
    elif sorttype == "desc":
        return sorted(listofnumbers,reverse= True)
    elif sorttype == "none":
        return listofnumbers
    else:
        raise ValueError("Invalid value for 'order'. Expected 'asc', 'desc', or 'none'.")


listofnumbers = [5, 3, 8, 1, 2]
print(sortlistofnumbers(listofnumbers, "asc"))  # Output: [1, 2, 3, 5, 8]
print(sortlistofnumbers(listofnumbers, "desc")) # Output: [8, 5, 3, 2, 1]
print(sortlistofnumbers(listofnumbers, "none")) # Output: [5, 3, 8, 1, 2]