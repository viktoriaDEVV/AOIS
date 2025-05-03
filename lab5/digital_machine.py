from prettytable import PrettyTable
import itertools


def subtraction(binary_number):
    result_number = []
    carry = 1
    for bit in reversed(binary_number):
        if bit == '1' and carry == 1:
            result_number.append('0')
            carry = 0
        elif bit == '0' and carry == 1:
            result_number.append('1')
            carry = 1
        else:
            result_number.append(bit)
    return ''.join(reversed(result_number))


def bits_to_string(q2, q1, q0):
    return f"{q2}{q1}{q0}"


def string_to_bits(binary_string):
    return int(binary_string[0]), int(binary_string[1]), int(binary_string[2])


def next_state(q2, q1, q0):
    current_binary = bits_to_string(q2, q1, q0)
    if current_binary == '000':
        next_binary = '111'
    else:
        next_binary = subtraction(current_binary)
    return string_to_bits(next_binary)


def generate_transition_table():
    table = PrettyTable()

    field_names = ['Q2', 'Q1', 'Q0', ' ', 'Q2_next', 'Q1_next', 'Q0_next', '  ', 'T2', 'T1', 'T0']
    table.field_names = field_names

    combinations = list(itertools.product([0, 1], repeat=3))
    combinations.sort(reverse=True)

    for combo in combinations:
        q2, q1, q0 = combo
        q2n, q1n, q0n = next_state(q2, q1, q0)

        t0 = 1 if q0 != q0n else 0
        t1 = 1 if q1 != q1n else 0
        t2 = 1 if q2 != q2n else 0

        table.add_row([q2, q1, q0, '  ', q2n, q1n, q0n, ' ', t2, t1, t0])

    return table, field_names


def create_sdnf_from_transitions(table, field_names, key):
    sdnf_parts = []
    signal_index = {'T2': -3, 'T1': -2, 'T0': -1}[key]

    for row in table.rows:
        value = int(row[signal_index])
        if value == 1:
            part = []
            for i in range(3):
                if int(row[i]) == 0:
                    part.append(f"!{field_names[i]}")
                else:
                    part.append(f"{field_names[i]}")
            sdnf_parts.append(' '.join(part))
    return sdnf_parts


def merge_parts(parts):
    merged = []
    used = set()
    for i in range(len(parts)):
        part1 = parts[i].split()
        for j in range(i + 1, len(parts)):
            part2 = parts[j].split()
            if len(part1) != len(part2):
                continue
            different_var = [(x, y) for x, y in zip(part1, part2) if x != y]
            if len(different_var) == 1 and (
                    (different_var[0][0].startswith('!') and different_var[0][1] == different_var[0][0][1:]) or
                    (different_var[0][1].startswith('!') and different_var[0][0] == different_var[0][1][1:])
            ):
                differences = [x != y for x, y in zip(part1, part2)]
                merged_part = [x if not diff else '' for x, diff in zip(part1, differences)]
                merged.append(' '.join(filter(bool, merged_part)))
                used.add(i)
                used.add(j)
    for k in range(len(parts)):
        if k not in used:
            merged.append(parts[k])

    unique_elements = set()
    final_result = []

    for elem in merged:
        if elem not in unique_elements:
            unique_elements.add(elem)
            final_result.append(elem)

    return final_result


def merging(sdnf_parts):
    current_parts = sdnf_parts
    while True:
        new_parts = merge_parts(current_parts)
        if new_parts == current_parts:
            break
        current_parts = new_parts
    if all(part == '' for part in current_parts):
        return '1'

    return current_parts


def format_str(parts):
    return " ∨ ".join(f'({t})' for t in parts) if parts else None