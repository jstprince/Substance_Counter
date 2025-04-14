class Node:  # Node for linkedlist in program
    def __init__(self, brand, name, stock):
        self.brand = brand
        self.name = name
        self.stock = stock
        self.next = None


class CannabisList:
    def __init__(self):
        self.start_node = None

    # ---------------- Add to item list ----------------#
    def add(self, brand, name, stock):
        new_node = Node(brand, name, stock)
        if not self.start_node:
            self.start_node = new_node
        else:
            n = self.start_node
            while n.next:
                n = n.next
            n.next = new_node

    # -- add stock to existing item --#
    def addToItem(self, brand, name, stock):
        if not self.start_node:
            print("There are no items in the list.")
            return
        n = self.start_node
        while n is not None:
            if n.brand == brand and n.name == name:
                n.stock += stock
                print(f"Added {stock} to {brand} ({name}). New stock: {n.stock}")
                return
            n = n.next
        print(f"Item {brand} ({name}) not found in the list.")

    # -- Deletes stock of existing item from list --#
    def delItem(self, brand_choice, name_choice):
        current = self.start_node
        prev = None

        while current is not None:
            if current.brand == brand_choice and current.name == name_choice:
                if prev is None:
                    # Deleting the first node
                    self.start_node = current.next
                else:
                    # Deleting a middle or last node
                    prev.next = current.next
                print(f"Deleted item {brand_choice} ({name_choice}) from the list.")
                return
            prev = current
            current = current.next

        print(f"Item {brand_choice} ({name_choice}) not found in the list.")

    # -- Print out only one brand of Items --#
    def ItemBrand(self, brand, choice):
        n = self.start_node
        if self.start_node is None:
            print("There are no Items")
            return
        else:
            found = False  # To check if at least one item matches
            while n is not None:
                if choice == n.brand:  # Match the choice with current node's brand
                    print(n.brand, n.name, n.stock)
                    found = True
                n = n.next  # Move to the next node
            if not found:
                print("No items found for the selected brand.")
            print("")  # Blank line for formatting

    # -- print out existing list of items --#
    def printItems(self):
        print("Items list: ")
        if self.start_node is None:
            print("There are no Items")
            return
        else:
            i = self.start_node
            while i is not None:
                print("Brand: ", i.brand, "|", "Name: ", i.name, "|", "Stock", i.stock, "|")
                i = i.next
            print(" ")