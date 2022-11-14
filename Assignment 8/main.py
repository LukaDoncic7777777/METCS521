x = """to kill a mockingbird
by Harper lee
and power of
mind and Python"""
x_list = list(x)
cursor = 3


def print_file(y, cur):
    print(y[:cur] + "$" + y[cur:] + "\n")



def cmd_h(y, cur):
    if cur > 0:
        cur -= 1
    return y, cur

print_file(x, cursor)
y, cur = cmd_h(x, cursor)
print_file(y, cur)

def cmd_l(y, cur):
    if cur < len(y) - 1:
        cur += 1
    return y, cur

print_file(x, cursor)
y, cur = cmd_l(x, cursor)
print_file(y, cur)

def cmd_end_current_line(y, cur):
    pos = y[cur:].find("\n")
    if pos >= 0:
        cur = cur + pos
    else:
        cur = len(y)
    return cur



def cmd_start_current_line(y, cur):
    pos = y[:cur].rfind("\n")
    if pos >= 0:
        cur = pos + 1
    else:
        cur = 0
    return cur


def cmd_j(y, cur):
    start_line = cmd_start_current_line(y, cur)
    delta = cur - start_line
    if start_line == 0:
        last_line = start_line - 1
        end_last_line = cmd_start_current_line(y, last_line)
        len_last_line = last_line - end_last_line
        if delta < len_last_line:
            cur = end_last_line + delta
        else:
            cur = end_last_line
    else:
        cur = cur - start_line
    return y, cur

cursor = 24
print_file(x, cursor)
y, cur = cmd_j(x, cursor)
print_file(y, cur)

def cmd_k(y, cur):
    start_line = cmd_start_current_line(y, cur)  # get position of starting line
    delta = cur - start_line  # get the index of current sign on the current line
    end_line = cmd_end_current_line(y, cur)
    if end_line < len(y) - 1:
        start_next_line = end_line + 1  # get to the beginning of the next line
        end_next_line = cmd_end_current_line(y, start_next_line)
        len_next_line = end_next_line - end_line
        if delta <= len_next_line:
            cur = end_line + delta + 1
        else:
            cur = end_next_line
    else:
        cur = len(y) - 1
    return y, cur

cursor = 24
print_file(x, cursor)
y, cur = cmd_k(x, cursor)
print_file(y, cur)


def cmd_X(y, cur):
    y = y.replace(y[cur - 1], '')
    cur = cur - 1
    return y, cur

cursor = 24
print_file(x, cursor)
y, cur = cmd_X(x, cursor)
print_file(y, cur)


def cmd_D(y, cur):
    end_line = cmd_end_current_line(y, cur)
    y = y.replace(y[cur:end_line], '')
    return y, cur

cursor = 24
print_file(x, cursor)
y, cur = cmd_D(x, cursor)
print_file(y, cur)


def cmd_dd(y, cur):
    start_line = cmd_start_current_line(y, cur)  #find the current beginning of the line
    end_line = cmd_end_current_line(y, cur) #find the end of the line
    after_line = y.find("\n", end_line + 1)
    if start_line == -1:
        y = y[end_line + 1:]
    if after_line == -1:
        prev_line = cmd_start_current_line(y, start_line)
        cur = prev_line + 1
    else:
        y = y[:start_line] + y[end_line:]
        cur = start_line + 1
    return y, cur


cursor = 24
print_file(x, cursor)
y, cur = cmd_dd(x, cursor)
print_file(y, cur)



def cmd_ddp(y, cur):
    before = y.rfind("\n", 0, cur)
    present = y.find("\n", cur)
    after = y.find("\n", present + 1)

    if after != -1:
        if before != -1:
            y = y[:before + 1] + y[present + 1:after] + y[before:present] + y[after:]
        else:
            y = y[present + 1:after] + '\n' + y[:present] + y[after:]
    else:
        before_before = y.rfind("\n", 0, before)
        y = y[:before_before + 1] + y[before + 1:present] + y[before_before:before] + y[present:]
    return y, cur

print_file(x, cursor)
y, cur = cmd_ddp(x, cursor)
print_file(y, cur)


def cmd_n(y, cur, target):
    pos = y.find(target, cur, len(y))
    if pos >= 0:
        cur = pos
    return y, cur

print_file(x, cursor)
y, cur = cmd_n(x, cursor, "power")
print(cur)


def cmd_wq(y,cur):
    f = open("hw6.txt", "a")
    f.truncate(0)
    f.write(y[:cur] + '^' + y[cur:])
    f.close()

cmd_wq(x, cursor)

#insert text at beginning of the line
def cmd_I(y, cur, text):
    x = y.rfind("\n", 0, cur)
    if x != 0:
        y = y[:x+1] + text + y[x + 1:]
    else:
        y = text + y[text+1:]

    return y, cur

print_file(x, cursor)
y, cur = cmd_I(x, cursor, "of")
print_file(y, cur)

#insert text before cursor
def cmd_i(y, cur, text):
    y = y[:cur] + text + y[cur:]
    cur += len(text)
    return y, cur

print_file(x, cursor)
y, cur = cmd_i(x, cursor, "of")
print_file(y, cur)

#append text after cursor
def cmd_a(y, cur, text):
    y = y[:cur] + text + y[cur:]
    return y, cur

print_file(x, cursor)
y, cur = cmd_a(x, cursor, "faic")
print_file(y, cur)

#append text at the end of the line
def cmd_A(y, cur, text):
    pos = y.find("\n", cur)
    if pos < len(y) - 1:
        y = y[:pos] + text + y[pos:]
    else:
        y = y[:pos] + text

    return y, cur

print_file(x, cursor)
y, cur = cmd_A(x, cursor, "faic")
print_file(y, cur)

#import file into current file
def cmd_r_file(y, cur):
    with open("hw6.txt", encoding='utf-8') as f:
        y = f
    return y, cur

y, cur = cmd_r_file(x, cursor)


def cmd_w_file(y, cur): #write the file to named file
    f = open("hw6.txt", "a")
    f.write("\nmy first file\n")
    current = f
    y = current
    return y, cur


cmd_w_file(x, cursor)

#move cursor to end of line
def cmd_C(y, cur):
    cur = y.find("\n", cur)
    return y, cur

print_file(x, cursor)
y, cur = cmd_C(x, cursor)
print_file(y, cur)

#replace certain character at cursor
def cmd_r(y, cur, newstring):
    if cur < len(y) - 1:
        y = y[:cur] + newstring + y[cur:]
    return y, cur

print_file(x, cursor)
y, cur = cmd_r(x, cursor, "faic")
print_file(y, cur)

#Move to first line on screen
def cmd_H(y, cur):
    cur = 0
    return y, cur

print_file(x, cursor)
y, cur = cmd_H(x, cursor)
print_file(y, cur)

#move cursor to end of line
def cmd_DollarSign(y, cur):
    cur = y.find("\n", cur, len(y))
    return y, cur

print_file(x, cursor)
y, cur = cmd_DollarSign(x, cursor)
print_file(y, cur)
