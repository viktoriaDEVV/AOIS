import itertools
from prettytable import PrettyTable


def is_logical_formula(formula):
    allowed_chars = set("abcde &|!()∧∨->~")
    for char in formula:
        if char not in allowed_chars:
            return False
    return True


def extracting_variables(input_string):
    pattern = ['a', 'b', 'c', 'd', 'e']
    variables = sorted(set(symbol for symbol in input_string if symbol in pattern))
    return variables


def truth_table(expression):
    variables = extracting_variables(expression)
    all_subformulas = extracting_sub_formulas(expression)
    unique_subformulas = [formula for formula in all_subformulas if formula not in variables]
    table = PrettyTable()
    table.field_names = variables + unique_subformulas
    combinations = list(itertools.product([0, 1], repeat=len(variables)))

    truth_values = {}
    for combo in combinations:
        row = list(combo)
        env = dict(zip(variables, combo))
        for subformula in unique_subformulas:
            row.append(evaluate(subformula, env))
        gray_key = ''.join(map(str, combo))
        truth_values[gray_key] = row[-1]
        table.add_row(row)
    return table, table.field_names, truth_values


def evaluate(expr, env):
    expr = expr.replace(" ", "")
    expr = remove_outer_parentheses(expr)

    if expr in env:
        return env[expr]

    if expr.startswith('!'):
        inner_expr = expr[1:]
        return 1 if not evaluate(inner_expr, env) else 0
    elif expr.startswith('not'):
        inner_expr = expr[3:]
        return 1 if not evaluate(inner_expr, env) else 0

    if 'and' or '&' in expr:
        last_and = find_last_operator(expr, ['and', '&'])
        if last_and != -1:
            left = expr[:last_and]
            right = expr[last_and + 3:] if expr[last_and:last_and + 3] == 'and' else expr[last_and + 1:]
            return 1 if evaluate(left, env) and evaluate(right, env) else 0

    if 'or' or '|' in expr:
        last_or = find_last_operator(expr, ['or', '|'])
        if last_or != -1:
            left = expr[:last_or]
            right = expr[last_or + 2:] if expr[last_or:last_or + 2] == 'or' else expr[last_or + 1:]
            return 1 if evaluate(left, env) or evaluate(right, env) else 0

    if '->' in expr:
        last_implication = find_last_operator(expr, ['->'])
        if last_implication != -1:
            left = expr[:last_implication]
            right = expr[last_implication + 2:]
            return 1 if not evaluate(left, env) or evaluate(right, env) else 0

    if '~' in expr:
        last_equivalence = expr.rfind('~')
        if last_equivalence != -1:
            left = expr[:last_equivalence]
            right = expr[last_equivalence + 1:]
            return 1 if evaluate(left, env) == evaluate(right, env) else 0

    if expr == "True":
        return 1
    elif expr == "False":
        return 0
    return 0


def find_last_operator(expr, operators):
    count = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')':
            count += 1
        elif expr[i] == '(':
            count -= 1
        elif count == 0 and any(expr.startswith(op, i) for op in operators):
            return i
    return -1


def remove_outer_parentheses(expr):
    while expr.startswith('(') and expr.endswith(')'):
        count = 0
        for i, char in enumerate(expr):
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count == 0 and i != len(expr) - 1:
                return expr
        expr = expr[1:-1]
    return expr


def extracting_sub_formulas(expression):
    sub_formulas = set()
    expression = expression.replace(' ', '')
    expression = remove_outer_parentheses(expression)
    sub_formulas.add(expression)
    if expression.startswith('!'):
        inner_expr = expression[2:-1] if expression[1] == '(' and expression.endswith(')') else expression[1:]
        sub_formulas.add(expression)
        sub_formulas.update(extracting_sub_formulas(inner_expr))
    operations = ['~', '->', '|', '&']
    level = 0
    main_operation_position = -1
    operation_length = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            level += 1
        elif expression[i] == ')':
            level -= 1
        elif level == 0:
            for op in operations:
                if expression[i:i + len(op)] == op:
                    main_operation_position = i
                    operation_length = len(op)
                    break
            if main_operation_position != -1:
                break
    if main_operation_position != -1:
        left_expr = remove_outer_parentheses(expression[:main_operation_position])
        right_expr = remove_outer_parentheses(expression[main_operation_position + operation_length:])
        sub_formulas.update(extracting_sub_formulas(left_expr))
        sub_formulas.update(extracting_sub_formulas(right_expr))
    unique_sub_formulas = sorted(set(sub_formulas), key=lambda x: (len(x), x))
    return unique_sub_formulas


def create_sdnf(table, field_names):
    variable_names = [name for name in field_names
                      if not any(char in name for char in ['(', ')', '∨', '∧', '!', '->', '&', '|'])]
    sdnf_parts = []
    for index, row in enumerate(table.rows, start=1):
        last_element = int(row[-1])
        if last_element == 1:
            part = []
            for i in range(len(variable_names)):
                if int(row[i]) == 0:
                    part.append(f"!{variable_names[i]}")
                else:
                    part.append(f'{variable_names[i]}')
            sdnf_parts.append(' '.join(part))
    return sdnf_parts


def format_str(parts, key):
    if key == 1:
        expression = " ∨ ".join(f'({t})' for t in parts)
    else:
        expression = " ∧ ".join(f'({t})' for t in parts)
    return expression if parts else None


def create_sknf(table, field_names):
    variable_names = [name for name in field_names
                      if not any(char in name for char in ['(', ')', '∨', '∧', '!', '->', '&', '|'])]
    sknf_parts = []
    for row in table.rows:
        last_element = int(row[-1])
        if last_element == 0:
            part = []
            for index in range(len(variable_names)):
                if int(row[index]) == 1:
                    part.append(f"!{variable_names[index]}")
                else:
                    part.append(f'{variable_names[index]}')
            sknf_parts.append("  ".join(part))
    return sknf_parts


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
    return current_parts


def build_table(constituents, minimized):
    table = PrettyTable()
    table.field_names = [""] + constituents
    for mini in minimized:
        row = [mini]
        for term in constituents:
            if all(var in term.split() for var in mini.split()):
                row.append('X')
            else:
                row.append('')
        table.add_row(row)
    print(table)
    return table


def minimized_from_table(table):
    results = set()

    for col in range(1, len(table.field_names)):
        x_count = 0
        corresponding_value = None

        for row in table.rows:
            if row[col] == 'X':
                x_count += 1
                corresponding_value = row[0]

        if x_count == 1 and corresponding_value is not None:
            results.add(corresponding_value)

    return list(results)


def generate_gray_code(n):
    if n == 1:
        return ['0', '1']
    prev_gray_code = generate_gray_code(n-1)
    gray_code = ['0' + num for num in prev_gray_code] + ['1' + num for num in reversed(prev_gray_code)]

    return gray_code


def carno_cart(variables, truth_values):
    amount_var = len(variables)
    half = amount_var // 2
    headers = generate_gray_code(amount_var - half)
    side_headers = generate_gray_code(half)
    table = PrettyTable()
    table.field_names = [f'{variables[:half]} \\ {variables[half:]}'] + headers

    for side in side_headers:
        row = [side]
        for col_header in headers:
            gray_index = side + col_header
            row.append(truth_values.get(gray_index, ''))
        table.add_row(row)
    print(table)
    return table


def find_groups(variables, truth_values, form):
    amount_var = len(variables)
    half = amount_var // 2
    headers = generate_gray_code(amount_var - half)
    side_headers = generate_gray_code(half)

    groups = []

    for side in side_headers:
        for col_header in headers:
            gray_index = side + col_header
            if form == 'SKNF' and truth_values.get(gray_index, '') == 0:
                groups.append((side, col_header))
            elif form == 'SDNF' and truth_values.get(gray_index, '') == 1:
                groups.append((side, col_header))
    return groups


def merge_groups(groups):
    merged = []
    used = set()
    for i in range(len(groups)):
        part1 = groups[i]
        for j in range(i + 1, len(groups)):
            part2 = groups[j]
            if len(part1) != len(part2):
                continue
            different_var = [(x, y) for x, y in zip(part1, part2) if x != y]
            if len(different_var) == 1 and (
                    (different_var[0][0] == '0' and different_var[0][1] == '1') or
                    (different_var[0][0] == '1' and different_var[0][1] == '0')
            ):
                differences = [x != y for x, y in zip(part1, part2)]
                merged_part = [x if not diff else '-' for x, diff in zip(part1, differences)]
                merged.append(''.join(merged_part))
                used.add(i)
                used.add(j)
    for k in range(len(groups)):
        if k not in used:
            merged.append(''.join(groups[k]))

    unique_elements = set()
    final_result = []

    for elem in merged:
        if elem not in unique_elements:
            unique_elements.add(elem)
            final_result.append(elem)

    return final_result


def minimize(variables, groups, form):
    amount_var = len(variables)
    half = amount_var // 2

    def binary_to_term(binary_str, variables, form):
        term = []
        for i, bit in enumerate(binary_str):
            if form == 'SKNF':
                if bit == '0':
                    term.append(variables[i])
                elif bit == '1':
                    term.append(f"!{variables[i]}")
            elif form == 'SDNF':
                if bit == '1':
                    term.append(variables[i])
                elif bit == '0':
                    term.append(f"!{variables[i]}")
            if bit == '-':
                continue
        return ' '.join(term)

    groups = [side + col for side, col in groups]
    merged_groups = merge_groups(groups)
    merged_groups = merge_parts(merged_groups)
    terms = []
    for group in merged_groups:
        terms.append(binary_to_term(group, variables, form))

    terms = merging(terms)
    expression = ' ∧ '.join(f'({t})' for t in terms)
    return expression
