
INTEGER, PLUS, SPACE, EOF = 'INTEGER', 'PLUS', 'SPACE', 'EOF'

class Token(object):

    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)}"

    def __repr__(self):
        return self.__str__()


class Interpreter(object):

    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception("Error parsing input")

    def get_next_token(self):
        text = self.text

        if self.pos > len(text)-1:
            return (EOF, None)

        current_char = text[self.pos]

        if current_char.is_digit():
            token = Token(INTEGER, current_char)
            self.pos += 1
            return token

        if current_char == "+":
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        if current_char == " ":
            token = Token(SPACE, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token == self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()


