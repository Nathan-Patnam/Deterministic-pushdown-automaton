#from ..nfa import build_nfa
import pytest
from dpda import DPDA


class TestDPDA(object):
    """
    @pytest.fixture(scope="function")
    def create_nfa(self):
        test_nfa = build_nfa("mocks/nfa_1.txt")
        test_nfa.run_machine("./mocks/nfa_input_1.txt",
                             "./mocks/outputs/nfa_output_1.txt")
        return test_nfa

    def test_get_states(self, create_nfa):
        states = set(["s2", "s1", "s3", "s4", "s5"])
        nfa_states = create_nfa.states
        assert states == nfa_states
    """

    @pytest.fixture(scope="function")
    def create_dpda(self):
        d_pushdown_automota = DPDA("dpda.txt")
        return d_pushdown_automota

    def test_remove_whitespace_and_newline(self, create_dpda):
        whitespaced__newline_word = "q4\n "
        formatted_word = "q4"
        whitespaced__newline_word = create_dpda.remove_whitespace_and_newline(whitespaced__newline_word)
        assert whitespaced__newline_word == formatted_word


    def test_parsing_file_for_states(self, create_dpda):
        expected_states = set(["q1", "q2", "q3", "q4"])
        states = create_dpda.get_states()
        assert expected_states == states
    
    def test_parsing_file_for_dpda_alphabet(self, create_dpda):
        expected_dpda_alphabet = set(["0", "1"])
        dpda_alphabet = create_dpda.get_dpda_alphabet()
        assert expected_dpda_alphabet == dpda_alphabet
    
    def test_parsing_file_for_stack_alphabet(self, create_dpda):
        expected_states = set(["0", "$"])
        states = create_dpda.get_stack_alphabet()
        assert expected_states == states
