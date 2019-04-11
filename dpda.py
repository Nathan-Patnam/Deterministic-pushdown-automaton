class DPDA():
    def __init__(self, file_name):
        self.file_name = ""
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
                self.parse_line_for_start_states(line)
            elif line_number == 1:
                self.parse_line_for_dpda_alphabet(line)
            elif line_number == 2:
                self.parse_line_for_stack_alphabet(line)
            elif line_number == 3:
                self.parse_line_for_start_state(line)
            elif line_number == 4:
                self.parse_line_for_accept_states(line)
            else:
                self.parse_line_for_transition(line)

            line_number += 1

        f.close()

    def parse_line_for_start_states(self, line):
        line = self.remove_whitespace_and_newline(line)
        states = line.split(",")
        for state in states:
            self.start_states.add(state)
    
    def parse_line_for_dpda_alphabet(self, line):
        line = self.remove_whitespace_and_newline(line)
        alphabet = line.split(",")
        for element in alphabet:
            self.dpda_alphabet.add(element)
    
    def parse_line_for_stack_alphabet(self, line):
        line = self.remove_whitespace_and_newline(line)
        alphabet = line.split(",")
        for element in alphabet:
            self.stack_alphabet.add(element)
    
    def parse_line_for_start_state(self, line):
        line = self.remove_whitespace_and_newline(line)
        self.start_state = line
    
    def parse_line_for_accept_states(self, line):
        line = self.remove_whitespace_and_newline(line)
        accept_states = line.split(",")
        for accept_state in accept_states:
            self.accept_states.add(accept_state)

    def parse_line_for_transition(self, line):
        line = self.remove_whitespace_and_newline(line)
        start_state,transition_record,end_state = self.parse_line_for_info(line)
    

        print(line)
    
    def parse_line_for_info(self, line):
        line = line.split(",")
        start_state = line[0]
        reading_symbol = line[1]
        top_of_stack = line[2]
        end_state = line[3]
        push_to_stack = line[4]

        record = (reading_symbol, top_of_stack, push_to_stack)
        return start_state, end_state, record

    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")


    def add_transition(self, line):
        return ""
    
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
