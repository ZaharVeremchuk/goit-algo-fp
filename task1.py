class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def insert_at_end(self, data):
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
    else:
      cur = self.head
      while cur.next:
        cur = cur.next
      cur.next = new_node

  def insert_after(self, prev_node: Node, data):
    if prev_node is None:
      print("Попереднього вузла не існує.")
      return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node

  def delete_node(self, key: int):
    cur = self.head
    if cur and cur.data == key:
      self.head = cur.next
      cur = None
      return
    prev = None
    while cur and cur.data != key:
      prev = cur
      cur = cur.next
    if cur is None:
      return
    prev.next = cur.next
    cur = None

  def search_element(self, data: int) -> Node | None:
    cur = self.head
    while cur:
      if cur.data == data:
        return cur
      cur = cur.next
    return None

  def print_list(self):
    current = self.head
    while current:
      print(current.data)
      current = current.next

  def reverse(self):
    self.head = reverse_list(self.head)

  def insertion_sort(self):
        if self.head is None or self.head.next is None: 
            return

        sorted_head = None 
        current = self.head

        while current:
            next_node = current.next 
            sorted_head = sorted_insert(sorted_head, current) 
            current = next_node  

        self.head = sorted_head 

  
def reverse_list(head):
    prev = None
    curr = head
    while curr:
      next_node = curr.next
      curr.next = prev
      prev = curr
      curr = next_node
    return prev

def sorted_insert(head, node_to_insert):
    if head is None or node_to_insert.data <= head.data:  
        node_to_insert.next = head
        return node_to_insert

    current = head
    while current.next and node_to_insert.data > current.next.data: 
        current = current.next

    node_to_insert.next = current.next  
    current.next = node_to_insert
    return head

def merge_sorted_lists(head1, head2):
    """
    head1: Перший вузол першого списку.
    head2: Перший вузол другого списку.
    """
    dummy = Node()
    tail = dummy

    while head1 and head2:
        if head1.data <= head2.data:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    # Додаємо залишки одного зі списків
    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

llist.reverse()

print("\nReversed Linked List")
llist.print_list()

print("\n Insertion Sort")
llist.insertion_sort()
llist.print_list()

print("\n Merge two Linked list")
list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_head = merge_sorted_lists(list1.head, list2.head)

merged_list = LinkedList()
merged_list.head = merged_head

merged_list.print_list()