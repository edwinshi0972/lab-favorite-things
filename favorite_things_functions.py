# display
def disp(favorites) -> None:
    print("Your favorite categories are: ", end="")
    for category in favorites:
        print(category, end=", ")
    print()

# lookup
def lookup(favorites) -> None:
    category = input("Enter a category to lookup: ")
    if category in favorites:
        print(f"My favorite {category} is {favorites[category]}!\n")
    else:
        print("Category not available.\n")

# add
def add(favorites) -> None:
    category = input("Enter new category: ")
    if category in favorites:
        print("Category already exists.\n")
    else:
        favorite = input("Enter your favorite for {category}: ")
        favorites[category] = favorite
    print()

# update
def update(favorites) -> None:
    category = input("Enter a category to update: ")
    if category in favorites:
        favorite = input("Enter your favorite for {category}: ")
        favorites[category] = favorite
        print()
    else:
        print("Category not available.\n")

# delete
def delete(favorites) -> None:
    category = input("Enter a category to delete: ")
    if category in favorites:
        del favorites[category]
        print()
    else:
        print("Category not available.\n")