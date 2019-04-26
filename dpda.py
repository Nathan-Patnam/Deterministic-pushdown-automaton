class DPDA():
    def __init__(self, file_name):
        self.start_states = set()
        self.dpda_alphabet = set()
        self.stack_alphabet = set()
        self.accept_states = set()
        self.start_state = ""
        self.transition_rules = {}
        self.build_dpda_from_file(file_name)

    def build_dpda_from_file(self, file_name):
        f = open(file_name, "r")
        lines = f.readlines()
        line_number = 0
        for line in lines:
            if line_number == 0:
                self.set_start_states(line)
            elif line_number == 1:
                self.set_dpda_alphabet(line)
            elif line_number == 2:
                self.set_stack_alphabet(line)
            elif line_number == 3:
                self.set_start_state(line)
            elif line_number == 4:
                self.parse_line_for_accept_states(line)
            else:
                self.set_dpda_transition(line)
            line_number += 1
        f.close()

    def set_start_states(self, line):
        line = self.remove_whitespace_and_newline(line)
        states = line.split(",")
        for state in states:
            self.start_states.add(state)

    def set_dpda_alphabet(self, line):
        line = self.remove_whitespace_and_newline(line)
        alphabet = line.split(",")
        for element in alphabet:
            self.dpda_alphabet.add(element)

    def set_stack_alphabet(self, line):
        line = self.remove_whitespace_and_newline(line)
        alphabet = line.split(",")
        for element in alphabet:
            self.stack_alphabet.add(element)

    def set_start_state(self, line):
        line = self.remove_whitespace_and_newline(line)
        self.start_state = line

    def parse_line_for_accept_states(self, line):
        line = self.remove_whitespace_and_newline(line)
        accept_states = line.split(",")
        for accept_state in accept_states:
            self.accept_states.add(accept_state)

    def set_dpda_transition(self, line):
        line = self.remove_whitespace_and_newline(line)
        key, value = self.parse_line_for_pushed_symbol_and_end_state(line)
        self.transition_rules[key] = value

    def parse_line_for_pushed_symbol_and_end_state(self, line):

        line = line.split(",")

        start_state = line[0]
        reading_symbol = line[1]
        top_of_stack = line[2]

        end_state = line[3]
        push_to_stack = line[4]

        inputt = (start_state, reading_symbol, top_of_stack)
        output = (push_to_stack, end_state)
        return inputt, output

    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")

    def get_decision(self, string):
        stack = []
        current_state = self.start_state
        char = ""

        current_character_in_input_string_index = 0

        while True:
            if len(string) != 0 and current_character_in_input_string_index < len(string):
                char = string[current_character_in_input_string_index]
            else:
                char = "@"

            if stack:
                top_of_stack = stack[-1]
            else:
                top_of_stack = "@"
                
            can_transition_be_made = self.is_transition_possible(
                current_state, char, top_of_stack)
            
            if (current_character_in_input_string_index >= (len(string))) and current_state in self.accept_states:
                return "accept"
        
            if can_transition_be_made:
                curr_state_char_top_of_stack, pushed_value_end_state = self.get_possible_transition_rule(
                    current_state, char, top_of_stack)

                value_to_push_to_stack = pushed_value_end_state[0]
                end_state = pushed_value_end_state[1]

                if curr_state_char_top_of_stack[1] == "@":
                    current_character_in_input_string_index -= 1
                if curr_state_char_top_of_stack[2] != "@":
                    stack.pop()
                if value_to_push_to_stack != "@":
                    stack.append(value_to_push_to_stack) 
                current_state = end_state
                current_character_in_input_string_index += 1
            else:
                return "reject"
        

    def is_transition_possible(self, current_state, char, top_of_stack):
            curr_state_char_top_of_stack, pushed_value_end_state = self.get_possible_transition_rule(
                current_state, char, top_of_stack)
            return curr_state_char_top_of_stack != ""

    def get_possible_transition_rule(self, current_state, char, top_of_stack):
        possible_transitions = [
            (current_state, char, top_of_stack),
            (current_state, char, "@"),
            (current_state, "@", "@"),
            (current_state, "@", top_of_stack)
        ]
        for transition in possible_transitions:
            if transition in self.transition_rules:
                return transition, self.transition_rules[transition]
        return "", ""

  

    def get_states(self):
        return self.start_states

    def get_dpda_alphabet(self):
        return self.dpda_alphabet

    def get_stack_alphabet(self):
        return self.stack_alphabet

    def get_accept_states(self):
        return self.accept_states

    def get_start_state(self):
        return self.start_state

    def get_transition_rules(self):
        return self.transition_rules


def main():
    d_pushdown_automota = DPDA("dpda.txt")
    fh = open("input.txt", "r")
    output_fh = open("output.txt","w")
    lines = fh.readlines()
    for line in lines:
        line = line.strip("\n")
        result = d_pushdown_automota.get_decision(line)
        output_fh.write(result + "\n")
  

if __name__ == "__main__":
    main()
