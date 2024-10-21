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

# Функція для знаходження найменшого значення
def find_min(root):
    if root is None:
        return None  # Якщо дерево порожнє
    current = root
    while current.left is not None:
        current = current.left  # Переходимо ліворуч
    return current.key

# Приклад використання
if __name__ == "__main__":
    root = None
    # Вставляємо значення в дерево
    values = [20, 8, 22, 4, 12, 10, 14]
    for value in values:
        root = insert(root, value)

    print("Найменше значення в дереві:", find_min(root))
