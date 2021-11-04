from helpers.interpreter import Interpreter


interpreter = Interpreter()


def main():
    while True:
        interpreter.start_handling()


if __name__ == '__main__':
    main()
