class Expression:
    def __init__(self,expression):
        self.expression=expression
    def evaluation(self):
        if self.expression is int:
            result=eval(self.expression)
            return result
        else:
            print('Syntax error.')
    def show_result(self):
        print(f"🧮 Expression: {self.expression}")
        result = self.evaluation()
        print(f"✅ Result: {result}")
# Example usage
if __name__ == "__main__":
    expr = input("Enter a mathematical expression (e.g., 3 + 5 * (2 - 1)): ")
    solver = Expression(expr)
    solver.show_result()        