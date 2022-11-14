# Please uncomment some tests to test 
data = 0
n_ptr = 1
p_ptr = 2

x = """today
is the next
Wed"""


def get_double_linked_list(x):
    head, tail = None, None
    x_list = x.split("\n")
    for e in x_list:
        next_node = [e, None, None]
        if head is None:
            head = next_node;
            tail = next_node
        else:
            tail[n_ptr] = next_node;
            next_node[p_ptr] = tail
            tail = next_node
    return head, tail


h, t = get_double_linked_list(x)
cur_node = h
cursor = 1


def print_linked_list(head, tail):
    cur_node = head
    while cur_node is not None:
        print(cur_node[data])
        cur_node = cur_node[n_ptr]
    return


def print_file_linked_list(head, tail, cur_node, cursor):
    tmp_node = head
    while tmp_node is not None:
        if tmp_node == cur_node:
            cur_line = tmp_node[data]
            print(cur_line[: cursor] + "$" + cur_line[cursor:])
        else:
            print(tmp_node[data])
        tmp_node = tmp_node[n_ptr]
    print("\n")
    return


def cmd_h(head, tail, cur_node, cursor):  # move left 1 char
    if cursor > 0:
        cursor = cursor - 1
    else:
        if cur_node is not head:
            cur_node = cur_node[p_ptr]
            cursor = len(cur_node[data])
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, c, cursor = cmd_h(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""

def cmd_l(head, tail, cur_node, cursor):
    cur_data = cur_node[data]
    if cursor < len(cur_data):
        cursor += 1

    else:
        if cur_node[n_ptr] is not None:
            cur_node = cur_node[n_ptr]
            cursor = 0
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, c, cursor = cmd_l(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""

def cmd_j(head, tail, cur_node, cursor):
    if cur_node is not head:
        prev_Node = cur_node[p_ptr]
        prev_Data = prev_Node[data]
        if cursor <= len(prev_Data):
            cur_node = cur_node[p_ptr]
        else:
            cursor = len(prev_Data)
            cur_node = cur_node[p_ptr]

    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, c, cursor = cmd_j(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""

def cmd_k(head, tail, cur_node, cursor):
    if cur_node is not tail:
        next_node = cur_node[n_ptr]
        next_line = next_node[data]
        if cursor < len(next_line):
            cur_node = next_node
        else:
            cursor = len(next_line) - 1
            cur_node = next_node
    return head, tail, cur_node, cursor


"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, c, cursor = cmd_k(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""


def cmd_X(head, tail, cur_node, cursor):
    if cursor > 0:
        line = cur_node[data]
        new_line = line[:cursor - 1] + line[cursor:]
        cur_node[data] = new_line
        cursor -= 1

    return head, tail, cur_node, cursor


"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, c, cursor = cmd_X(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""


def cmd_D(head, tail, cur_node, cursor):
    if cursor == 0:
        if cur_node == tail:
            cur_node[p_ptr][n_ptr] = None
        else:
            prev = cur_node[p_ptr]
            next_node = cur_node[n_ptr]
            prev[n_ptr] = cur_node[n_ptr]
            next_node[p_ptr] = cur_node[p_ptr]
            cur_node = prev
    else:
        line = cur_node[data]
        cur_node[data] = line[:cursor]

    return head, tail, cur_node, cursor


"""
print_file_linked_list(h, t, c, cursor)
h, t, c, cursor = cmd_D(h, t, cur_node, cursor)
print_file_linked_list(h, t, c, cursor)
"""


def cmd_dd(head, tail, cur_node, cursor):

    if cur_node is not tail and cur_node[p_ptr] is not None:
        prev = cur_node[p_ptr]
        next_node = cur_node[n_ptr]
        prev[n_ptr] = cur_node[n_ptr]
        next_node[p_ptr] = cur_node[p_ptr]
        cur_node = next_node
        cursor = 0

    else:
        head = cur_node[n_ptr]
        next_node = cur_node[n_ptr]
        next_node[p_ptr] = cur_node[p_ptr]
        cur_node = next_node
        cursor = 0
    return head, tail, cur_node, cursor
"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_dd(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""

def cmd_ddp(head, tail, cur_node, cursor):
    if cur_node is not tail:
        next_node = cur_node[n_ptr]
        cur_node, next_node = next_node, cur_node
        if cursor > len(cur_node[data]):
            cursor = len(cur_node[data])

    return head, tail, cur_node, cursor
"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_ddp(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""

def cmd_n(head, tail, cur_node, cursor, target):
    next_node = cur_node
    while next_node is not None:
        line = next_node[data]
        pos = line.find(target)
        if pos >= 0:
            return head, tail, next_node, pos
        next_node = next_node[n_ptr]
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_n(h, t, cur_node, cursor, "is")
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_wq(head, file_name):
    f = open(file_name, "a")
    f.truncate(0)
    curr_node = head
    while curr_node is not None:
        line = curr_node[data]
        line += '\n'
        curr_node = curr_node[n_ptr]
        f.writelines(line)
    f.close()
"""
cmd_wq(h, "hw10.txt")
"""

def cmd_i(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = line[:cursor] + target + line[cursor:]
    cursor += len(target)
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_i(h, t, cur_node, cursor, "is")
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_I(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = target + line
    cursor += len(target)
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_I(h, t, cur_node, cursor, "abc")
print_file_linked_list(h, t, cur_node, cursor)
"""

def cmd_a(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = line[:cursor] + target + line[cursor:]
    return head, tail, cur_node, cursor
"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_a(h, t, cur_node, cursor, "abc")
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_A(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = line + target
    return head, tail, cur_node, cursor
"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_A(h, t, cur_node, cursor, "abc")
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_C(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = line[:cursor] + target
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_C(h, t, cur_node, cursor, "abc")
print_file_linked_list(h, t, cur_node, cursor)
"""

def cmd_r(head, tail, cur_node, cursor, target):
    line = cur_node[data]
    cur_node[data] = line[:cursor] + target + line[cursor + 1:]
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_r(h, t, cur_node, cursor, "abc")
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_H(head, tail, cur_node, cursor):
    cur_node = head
    cursor = 0
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_H(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_DollarSign(head, tail, cur_node, cursor):
    cursor = len(cur_node[data])
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_DollarSign(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_x(head, tail, cur_node, cursor):
    line = cur_node[data]
    if cursor < len(line):
        cur_node[data] = line[:cursor] + line[cursor + 1:]
    return head, tail, cur_node, cursor

"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_x(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""
def cmd_w_file(head, tail, cur_node, cursor):
    f = open("hw10.txt", "a")
    cur_node = tail
    if cur_node is not None:
        f.writelines("Time to cook")
        cur_node = cur_node[n_ptr]
    f.close()

cmd_w_file(h, t, cur_node, cursor)

def cmd_0(head, tail, cur_node, cursor):
    cursor = 0
    return head, tail, cur_node, cursor
"""
print_file_linked_list(h, t, cur_node, cursor)
h, t, cur_node, cursor = cmd_0(h, t, cur_node, cursor)
print_file_linked_list(h, t, cur_node, cursor)
"""