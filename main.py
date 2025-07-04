def main():
    favorites = {"color": "blue", "food": "noodles", "movie": "spider man"}
    print("Your favorite categories are: color, food, movie")
    category = input("Which category would you like to see? ")
    if category in favorites:
        print(f"My favorite {category} is {favorites[category]}!\n")
    else:
        print("Category not available.\n")
    choice = input("Would you like to add a new favorite category? (yes/no) ").lower()
    if choice == "yes":
        category = input("Enter new category: ")
        favorite = input("Enter your favorite for {category}: ")
        favorites[category] = favorite
        print()
    else:
        print()
    print("Here are all your favorites:")
    for category, favorite in favorites.items():
        print(f"{category}: {favorite}")

if __name__ == "__main__":
    main()
