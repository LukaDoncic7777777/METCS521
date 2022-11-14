# You may need to comment and uncomment some test in order to work.

x = """da vinci code
atomic habits
harry potter"""

x_list = x.split("\n")
line = 1
delta = 3


def print_file(x_list, line, delta):
    left_side = "\n".join(x_list[:line])
    right_side = "\n".join(x_list[line + 1:])
    c_line = x_list[line]
    middle = c_line[: delta] + "$" + c_line[delta:]
    print(left_side + "\n" + middle + "\n" + right_side + "\n")


def cmd_h(x_list, line, delta):  # move left one pos
    if delta > 0:
        delta = delta - 1
    else:
        if line > 0:
            line = line - 1
            delta = len(x_list[line])
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_h(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_k(x_list, line, delta):  # move vertically down
    if line < len(x_list) - 1:
        line = line + 1
        if delta > len(x_list[line]):
            delta = len(x_list[line])
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_k(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_l(x_list, line, delta):
    current = x_list[line]
    if delta < len(current):
        delta = delta + 1
    elif line < len(x_list) - 1:
        line += 1
        delta = 0
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_l(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_j(x_list, line, delta):
    if line > 0:
        previous = x_list[line - 1]
        if delta < len(previous):
            line -= 1

        else:
            line -= 1
            delta = len(previous)

    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_j(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_X(x_list, line, delta):
    if delta > 0:
        current = x_list[line]
        new_line = current[:delta - 1] + current[delta:]
        x_list[line] = new_line
        delta -= 1
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_X(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_D(x_list, line, delta):
    if delta == 0:
        x_list.pop(x_list[line])

    else:
        current = x_list[line]
        new_line = current[:delta]
        x_list[line] = new_line

    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_D(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_dd(x_list, line, delta):
    if line < len(x_list) - 1:
        x_list.pop(line)
        delta = 0
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_dd(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_ddp(x_list, line, delta):
    if line < len(x_list) - 1:
        current = x_list[line]
        next = x_list[line + 1]
        x_list[line] = next
        x_list[line + 1] = current
        line += 1
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_ddp(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_n(x_list, line, delta, target):
    for next_line, next_sentence in enumerate(x_list):
        if next_line >= line:
            pos = next_sentence.find(target)
            if pos >= 0:
                line = next_line
                delta = pos
                break
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_n(x_list, line, delta, "atm")
print_file(the_list, the_line, the_delta)


def cmd_wq(x_list, line, delta):
    f = open('hw9.txt', "a")
    f.truncate(0)
    string = '\n'.join(x_list)
    f.writelines(string)
    f.close()


cmd_wq(x_list, line, delta)


def cmd_I(x_list, line, delta, target):
    sentence = x_list[line]
    new_line = target + sentence
    x_list[line] = new_line
    delta += len(target)
    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_I(x_list, line, delta, "atm")
print_file(the_list, the_line, the_delta)
"""


def cmd_i(x_list, line, delta, target):
    sentence = x_list[line]
    if delta > 0:
        new_sentence = sentence[:delta] + target + sentence[delta + 1:]
        x_list[line] = new_sentence
        delta += len(target)

    else:
        new_sentence = target + sentence[delta:]
        x_list[line] = new_sentence
        delta += len(target)

    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_i(x_list, line, delta, "atm")
print_file(the_list, the_line, the_delta)
"""


def cmd_a(x_list, line, delta, target):
    sentence = x_list[line]
    new_sentence = sentence[:delta] + target + sentence[delta:]
    x_list[line] = new_sentence
    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_a(x_list, line, delta, "atm")
print_file(the_list, the_line, the_delta)
"""


def cmd_A(x_list, line, delta, target):
    sentence = x_list[line]
    new_sen = target + sentence
    x_list[line] = new_sen
    delta += len(target)
    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_A(x_list, line, delta, "abe")
print_file(the_list, the_line, the_delta)
"""


def cmd_r_file(x_list, line, delta):
    with open("hw9.txt", encoding='utf-8') as f:
        x_list.append(f)
    return x_list, line, delta


"""
cmd_r_file(x_list, line, delta)
"""


def cmd_w_file(x_list, line, delta):  # write the file to named file
    f = open("hw9.txt", "a")
    f.write("\nGG Bond\n")
    f.close()
    return x_list, line, delta


"""
cmd_w_file(x_list, line, delta)
"""


def cmd_C(x_list, line, delta):
    current = x_list[line]
    delta = len(current)
    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_C(x_list, line, delta)
print_file(the_list, the_line, the_delta)
"""


def cmd_r(x_list, line, delta, target):
    if delta < len(x_list[line]):
        sentence = x_list[line]
        new_sen = sentence[:delta] + target + sentence[delta + 1:]
        x_list[line] = new_sen
    return x_list, line, delta


"""
print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_r(x_list, line, delta, "youd")
print_file(the_list, the_line, the_delta)
"""


def cmd_H(x_list, line, delta):
    line = 0
    delta = 0
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_H(x_list, line, delta)
print_file(the_list, the_line, the_delta)


def cmd_DollarSign(x_list, line, delta):
    delta = len(x_list[line])
    return x_list, line, delta


print_file(x_list, line, delta)
the_list, the_line, the_delta = cmd_DollarSign(x_list, line, delta)
print_file(the_list, the_line, the_delta)
