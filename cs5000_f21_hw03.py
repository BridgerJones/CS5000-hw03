
###############################################
# cs5000_f21_hw03.py
# Bridger Jones
# A02314787
###############################################


def nfa_to_dfa(nfa):
    # initialize the different parts of 5 tuple into variables
    states = nfa[0]
    sigma = nfa[1]
    delta = nfa[2]
    start_state = nfa[3]
    final_states = nfa[4]

    # create the variables for the new DFA
    new_states = []
    new_delta = {}
    new_final_states = []

    # initialize queue
    queue = []
    queue.append(set([start_state]))

    while len(queue) != 0:
        # grab the current state from queue
        current_state = queue.pop(0)
        # loop through the different types of input
        for alphabet in sigma:
            # create a new state set
            new_state = set()
            # for every state in the current_state
            # apply the transition method and save
            # the union of them in the new_state
            for state in current_state:
                try:
                    new_state |= delta[state, alphabet]
                # if there is no transition for the state and input PASS
                except KeyError:
                    pass
            # create a sorted tuple for ease in displaying
            new_state = tuple(sorted(new_state))
            # stopping check for while loop
            if new_state not in states and new_state not in new_states:
                queue.append(new_state)
                new_states.append(new_state)
            # create an entry in the new delta
            new_delta[(tuple(current_state), alphabet)] = new_state
    # find the new final states
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
        print(f"{count}) d{key} = {value}")
        count += 1
    print(f"FINAL STATES: {dfa[4]}")
