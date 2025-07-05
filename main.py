import favorite_things_functions as ft

def main():
    favorites = {"color": "blue", "food": "noodles", "movie": "spider man"}
    ft.disp(favorites)
    
    while True:
        command = input("What would you like to do? (lookup/add/update/delete/quit): ").lower()
        if command == "lookup":
            ft.lookup(favorites)
        elif command == "add":
            ft.add(favorites)
        elif command == "update":
            ft.update(favorites)
        elif command == "delete":
            ft.delete(favorites)
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.\n")

if __name__ == "__main__":
    main()
