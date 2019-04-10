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
        

    def remove_whitespace_and_newline(self, line):
        return line.strip().replace("\n", "")


    
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