from copy import deepcopy

INITIAL_STATE = {
    'raft_side': 'left',
    'left_animals': {'wolf': 3, 'chick': 3},
    'right_animals': {'wolf': 0, 'chick': 0},
}

POSSIBLE_MOVES = [
    {'wolf': 1},
    {'wolf': 2},
    {'chick': 1},
    {'chick': 2},
    {'wolf': 1, 'chick': 1},
]

def main():
    stack = [INITIAL_STATE]
    move_list = []
    search(stack, move_list)

    print(stack[0])
    for move, state in zip(move_list, stack[1:]):
        print(move, state['raft_side'])
        print(state)


def search(stack, move_list):
    for move in POSSIBLE_MOVES:
        new_state = deepcopy(stack[-1])
        if cross_river(new_state, move):
            if new_state not in stack:
                stack.append(new_state)
                move_list.append(move)
                if new_state['left_animals'] == {'wolf': 0, 'chick': 0}:
                    return True
                if search(stack, move_list):
                    return True
    stack.pop()
    move_list.pop()
    return False



def num_animals(animals):
    return sum(animals.values())


def are_chicks_safe(side):
    chicks = side.get('chick', 0)
    wolves = side.get('wolf', 0)
    return (
        chicks == 0 or
        chicks >= wolves
    )


def cross_river(state, crossing_animals):
    if state['raft_side'] == 'left':
        start_side = state['left_animals']
        end_side = state['right_animals']
        state['raft_side'] = 'right'
    elif state['raft_side'] == 'right':
        start_side = state['right_animals']
        end_side = state['left_animals']
        state['raft_side'] = 'left'
    else:
        raise ValueError('Invalid raft side')

    assert num_animals(crossing_animals) in [1, 2]

    for animal_type, number in crossing_animals.items():
        start_side[animal_type] -= number
        end_side[animal_type] += number

        if not start_side[animal_type] >= 0:
            return False

    if not (
        are_chicks_safe(state['left_animals']) and
        are_chicks_safe(state['right_animals'])
    ):
        return False

    return True


if __name__ == '__main__':
    main()
