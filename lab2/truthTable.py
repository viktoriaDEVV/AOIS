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

    for combo in combinations:
        row = list(combo)
        env = dict(zip(variables, combo))
        for subformula in unique_subformulas:
            row.append(evaluate(subformula, env))
        table.add_row(row)
    return table, table.field_names


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
            sknf_parts.append(" ∨ ".join(part))
    sknf_expression = " ∧ ".join(f'({t})' for t in sknf_parts)
    return sknf_expression if sknf_parts else None


def create_sdnf(table, field_names):
    variable_names = [name for name in field_names
                      if not any(char in name for char in ['(', ')', '∨', '∧', '!', '->', '&', '|'])]
    sdnf_parts = []
    for row in table.rows:
        last_element = int(row[-1])
        if last_element == 1:
            part = []
            for index in range(len(variable_names)):
                if int(row[index]) == 0:
                    part.append(f"!{variable_names[index]}")
                else:
                    part.append(f'{variable_names[index]}')
            sdnf_parts.append(" ∧ ".join(part))
    sknf_expression = " ∨ ".join(f'({t})' for t in sdnf_parts)
    return sknf_expression if sdnf_parts else None


def digital_form_sknf(table):
    digital_sknf = []
    part = []
    for row_index, row in enumerate(table.rows):
        last_element = int(row[-1])
        if last_element == 0:
            part.append(row_index)
    if part:
        sknf_string = f"({', '.join(map(str, part))}) ∧"
        digital_sknf.append(sknf_string)
    else:
        digital_sknf.append("")
    return ''.join(digital_sknf)


def digital_form_sdnf(table):
    digital_sdnf = []
    part = []
    for row_index, row in enumerate(table.rows):
        last_element = int(row[-1])
        if last_element == 1:
            part.append(row_index)
    if part:
        sdnf_string = f"({', '.join(map(str, part))}) ∨"
        digital_sdnf.append(sdnf_string)
    else:
        digital_sdnf.append("")
    return ''.join(digital_sdnf)


def index_form(table):
    result_values = []
    digital_result = 0
    for row in table.rows:
        last_element = int(row[-1])
        result_values.append(last_element)
    for index, value in enumerate(reversed(result_values)):
        digital_result += int(value) * (2 ** index)
    result_values = ''.join(map(str, result_values))
    return digital_result, result_values
