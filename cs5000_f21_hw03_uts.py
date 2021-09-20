####################################################
# CS5000: F21: Assignment 3: Unit Tests
# Description: Two unit tests for the subset construction
#              algorithm.
# bugs to vladimir kulyukin in canvas
#####################################################

from cs5000_f21_hw03 import nfa_to_dfa, display_dfa
import unittest

class CS5000F21Assign03UnitTests(unittest.TestCase):

    def test_assgn_03_ut_01(self):
        print('\n***** Assign 03: Subset Construction UT 01 *****')
        ### This NFA is from Lecture 4 (Slide 7 in
        ### CS5000_F21_Lecture_04_SubsetConstructionWithQueueOptimization.pdf).
        NFA_DELTA_01 = {}
        NFA_DELTA_01[('q0', '0')] = set(['q0'])
        NFA_DELTA_01[('q0', '1')] = set(['q0', 'q1'])
        NFA_DELTA_01[('q1', '0')] = set(['q2'])
        NFA_DELTA_01[('q1', '1')] = set(['q2'])
        NFA_01 = (set(['q0','q1', 'q2']),
                  set(['0', '1']),
                  NFA_DELTA_01,
                  'q0',
                  set(['q2']))

        dfa_01 = nfa_to_dfa(NFA_01)
        display_dfa(dfa_01)

    def test_assgn_03_ut_02(self):
        print('\n***** Assign 03: Subset Construction UT 02 *****')
        ### This NFA is from CS5000: F21: Assignment 02: Problem 02.
        NFA_DELTA_02 = {}
        NFA_DELTA_02[('q0', '0')] = set(['q0', 'q1'])
        NFA_DELTA_02[('q0', '1')] = set(['q1'])
        NFA_DELTA_02[('q1', '0')] = set(['q2'])
        NFA_DELTA_02[('q1', '1')] = set(['q2'])
        NFA_DELTA_02[('q2', '0')] = set(['q2'])
        NFA_DELTA_02[('q2', '1')] = set(['q2'])        
        NFA_02 = (set(['q0', 'q1', 'q2']),
                  set(['0', '1']),
                  NFA_DELTA_02,
                  'q0',
                  set(['q1']))
        dfa_02 = nfa_to_dfa(NFA_02)
        display_dfa(dfa_02)
    
### ================ Unit Tests ====================

if __name__ == '__main__':
    unittest.main()


 
    
        
        

    
        





