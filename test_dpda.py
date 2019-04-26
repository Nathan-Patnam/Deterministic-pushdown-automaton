import pytest
from dpda import DPDA


@pytest.fixture(scope="module")
def create_dpda():
    d_pushdown_automota = DPDA("dpda.txt")
    return d_pushdown_automota


class TestDPDA(object):
    @pytest.fixture(autouse=True)
    def test_remove_whitespace_and_newline(self, create_dpda):
        whitespaced__newline_word = "q4\n "
        formatted_word = "q4"
        whitespaced__newline_word = create_dpda.remove_whitespace_and_newline(
            whitespaced__newline_word)
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
        expected_stack_alphabet = set(["0", "$"])
        states = create_dpda.get_stack_alphabet()
        assert expected_stack_alphabet == states

    def test_parsing_file_for_start_state(self, create_dpda):
        expected_start_state = "q1"
        start_state = create_dpda.get_start_state()
        assert expected_start_state == start_state

    def test_parsing_file_for_accept_staes(self, create_dpda):
        expected_accept_states = set(["q1", "q4"])
        accept_states = create_dpda.get_accept_states()
        assert expected_accept_states == accept_states

    def test_parse_line_for_record(self, create_dpda):
        record = {
            ("q1", "@", "@"): ("$", "q2"),
            ("q2", "0", "@"): ("0", "q2"),
            ("q2", "1", "0"): ("@", "q3"),
            ("q3", "1", "0"): ("@", "q3"),
            ("q3", "@", "$"): ("@", "q4"),
        }
        assert record == create_dpda.get_transition_rules()

    def test_parse_line_for_info(self, create_dpda):
        record = ("q1", "@", "@")
        end_state = ("$", "q2")
        line = "q1,@,@,q2,$"
        foo, bar = create_dpda.parse_line_for_pushed_symbol_and_end_state(line)

        assert [record, end_state] == [foo, bar]

    @pytest.fixture
    def get_machine_result_for_each(self):
        return [("", "accept"),
                ("0", "reject"),
                ("1", "reject"),
                ("00", "reject"),
                ("01", "accept"),
                ("10", "reject"),
                ("11", "reject"),
                ("000111", "accept"),
                ("0011", "accept"),
                ("01", "accept"),
                ("00001111", "accept"),
                ("01111", "reject"),
                ("0010000", "reject"),
                ("1010", "reject"),
                ("0000", "reject")
                ]

    def test_inputs_on_dpda(self, create_dpda, get_machine_result_for_each):
        for input_output in get_machine_result_for_each:
                input_string = input_output[0]
                output = create_dpda.get_decision(input_string)
                expected_output_string = input_output[1]
                assert output == expected_output_string
