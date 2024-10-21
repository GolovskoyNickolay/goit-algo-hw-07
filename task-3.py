# Вузол дерева
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Функція для вставки у двійкове дерево пошуку
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Функція для знаходження суми всіх значень
def find_sum(root):
    if root is None:
        return 0  # Базовий випадок: якщо дерево порожнє
    # Сума значення поточного вузла + рекурсивна сума лівого і правого піддерева
    return root.key + find_sum(root.left) + find_sum(root.right)

# Приклад використання
if __name__ == "__main__":
    root = None
    # Вставляємо значення в дерево
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        root = insert(root, value)

    print("Сума всіх значень у дереві:", find_sum(root))
