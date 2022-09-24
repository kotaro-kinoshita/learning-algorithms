class LinkedListNode:
    def __init__(self, val, nextnode):
        self.val = val
        self.next = nextnode

def create_linked_list(vals, pos):
    next_node = None
    nodes = []
    for val in reversed(vals):
        node = LinkedListNode(val, next_node)
        next_node = node
        nodes.insert(0, node)

    if 0 <= pos < len(vals):
        nodes[-1].next = nodes[pos]

    return next_node

def has_cycle(head):
    slow = head
    fast = head

    while(slow is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next

        if slow is None or fast is None:
            return None

        if slow == fast:
            return fast

    return None

def detect_cycle_begin(head):
    intersection = has_cycle(head)
    if intersection is None:
        return None

    slow = head
    fast = intersection
    while(slow != fast):
        slow = slow.next
        fast = fast.next
    
    return slow

def calc_cycle_length(head):
    cycle_begin_node = detect_cycle_begin(head)

    if cycle_begin_node is None:
        return -1

    fast = cycle_begin_node
    slow = cycle_begin_node

    cycle_length = 0
    while(True):
        slow = slow.next
        fast = fast.next.next
        cycle_length += 1
        
        if slow == fast:
            break

    return cycle_length

if __name__ == "__main__":
    case = [3,2,0,-4]
    pos = 1
    head = create_linked_list(case, pos)
    print("cycle_length", calc_cycle_length(head))

    case = [1,2]
    pos = 0
    head = create_linked_list(case, pos)
    print("cycle_length", calc_cycle_length(head))

    case = [1]
    pos = -1
    head = create_linked_list(case, pos)
    print("cycle_length", calc_cycle_length(head))