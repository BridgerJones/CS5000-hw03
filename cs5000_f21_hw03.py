
###############################################
# cs5000_f21_hw03.py
# Bridger Jones
# A02314787
###############################################


def nfa_to_dfa(nfa):
    states = nfa[0]
    sigma = nfa[1]
    delta = nfa[2]
    start_state = nfa[3]
    final_states = nfa[4]

    new_states = []
    new_delta = {}
    new_final_states = []
    new_sigma = sigma

    # initialize queue
    queue = []
    queue.append(set([start_state]))

    while len(queue) != 0:
        current_state = queue.pop(0)

        for alphabet in sigma:
            new_state = set()
            for state in current_state:
                try:
                    new_state |= delta[state, alphabet]
                except KeyError:
                    pass
            new_state = set(sorted(tuple(new_state)))
            if new_state not in states and new_state not in new_states:
                queue.append(new_state)
                new_states.append(new_state)
            new_delta[(str(current_state), alphabet)] = new_state
    for state in new_states:
        for sub_state in state:
            if sub_state in final_states:
                new_final_states.append(state)

    return (new_states, sigma, new_delta, start_state, new_final_states)



def display_dfa(dfa):
    print(f"STATES: {dfa[0]}")
    print(f"SIGMA: {dfa[1]}")
    print(f"START STATE: {dfa[3]}")
    count = 0
    for key, value in dfa[2].items():
        print(f"{count}) {key} = {value}")
        count += 1
    print(f"FINAL STATES: {dfa[4]}")
