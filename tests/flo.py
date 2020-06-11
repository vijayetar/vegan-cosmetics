import builtins
from main import welcome_information, user_input,search_product, find_search_product,save_user_product, grab_saved_product

class Flo:
    PROMPTS = (
        "Would you like to see anything from our store catalog (y/n) Or would you like to quit (q)?",
        "What would you like to view? Quit with (q)",
        "Would you like to save the products to your personal catalog (y/n)? You can also quit(q)",
        "Would you like to view your personal catalog (y/n)? You can also quit (q)",
        "Would you like to view more products(y/n) or quit(q)?",
        "Enter (q) to quit or (y) to view more products"
    )
    def __init__(self, path):
        self.path = path
        self.old_print = print
        self.old_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.prints = ""
        self.responses = []
        with open(self.path) as file:
            file_list = file.readlines()
        for i,line in enumerate(file_list):
                # gather prompt responses
            for prompt in self.PROMPTS:
                if line.startswith(prompt):
                    response = file_list[i+1].strip()
                    self.responses.append(response)
                    self.old_print("this is response", self.responses)
    @staticmethod
    def test(path):
        flo = Flo(path)
        try:
          user_input()
        except SystemExit:
          flo.old_print('no problemo')
        finally:
          flo._exit()
    def _mock_print(self, *args, **kwargs):
        self.prints += str(*args) + "\n"
    def _mock_input(self, *args, **kwargs):
        self.prints += str(*args)
        response = self.responses.pop(0)
        self.prints += response + "\n"
        return response
    def _exit(self):
        with open(self.path) as file:
            print_lines = self.prints.strip().split("\n")
            file_lines = file.read().strip().split("\n")
            pairs = zip(print_lines, file_lines)
            for i, pair in enumerate(pairs):
                actual, expected = pair
                assert (
                    actual == expected
                ), f"line {i} - actual:{actual} - expected:{expected}"
        builtins.print = self.old_print
        builtins.input = self.old_input
if __name__ == "__main__":
    Flo.test("tests/flow/flo_quit.txt")