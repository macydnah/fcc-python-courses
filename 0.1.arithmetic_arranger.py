def arithmetic_arranger(problems, show_answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    for current in range(len(problems)):
        current_split = problems[current].split(' ')
        
        for i in range(0, len(current_split) - 1, 2):

            top = current_split[i]
            operator = current_split[i+1]
            bottom = current_split[i+2]

            top_len = len(top)
            bottom_len = len(bottom)

            #if not (True or True):
            if not (operator == '+' or operator == '-'):
                return "Error: Operator must be '+' or '-'."
            #if not (True and True):
            if not (top.isdigit() and bottom.isdigit()):
                return 'Error: Numbers must only contain digits.'
            if (top_len > 4 or bottom_len > 4):
                return 'Error: Numbers cannot be more than four digits.'

            width = max(top_len, bottom_len) + 2
            dashes = '-' * width
            space = ' ' * 4

            top = top.rjust(width)
            bottom = bottom.rjust(width - 1)
            dashes = dashes.rjust(width)
            answers = str(int(top) + int(bottom) if operator == '+' else int(top) - int(bottom)).rjust(width)
            if current:
                top_top += space + top
                bottom_bottom += space + operator + bottom
                dashes_dashes += space + dashes
                answers_answers += space + answers
            else:
                top_top = top
                bottom_bottom = operator + bottom
                dashes_dashes = dashes
                answers_answers = answers

    if show_answers:
        problems[current] = top_top + '\n' + bottom_bottom + '\n' + dashes_dashes + '\n' + answers_answers
    else:
        problems[current] = top_top + '\n' + bottom_bottom + '\n' + dashes_dashes

    return problems[len(problems) - 1]

print(f'{arithmetic_arranger(["3801 - 2", "123 + 49"], show_answers=True)}')
#print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True)}')
