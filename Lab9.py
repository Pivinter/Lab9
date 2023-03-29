class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def print_tree(root, level=0):
    if root is not None:
        print_tree(root.left, level + 1)
        print(" " * 4 * level + "->", root.value)
        print_tree(root.right, level + 1)


def build_binary_search_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root


def count_leaf_nodes(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


def main():
    while True:
        print("\nМеню:")
        print("1. Створити бінарне дерево пошуку")
        print("2. Вивести бінарне дерево пошуку на екран")
        print("3. Визначити кількість елементів, які не мають дочірніх")
        print("0. Вийти")

        choice = int(input("Введіть номер операції: "))

        if choice == 1:
            n = int(input("Введіть кількість елементів: "))
            elements = [int(input(f"Введіть елемент {i + 1}: ")) for i in range(n)]
            root = build_binary_search_tree(elements)
        elif choice == 2:
            print("Бінарне дерево пошуку:")
            print_tree(root)
        elif choice == 3:
            count = count_leaf_nodes(root)
            print(f"Кількість елементів, які не мають дочірніх: {count}")
        elif choice == 0:
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
