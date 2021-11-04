class Interpreter:
    __available_commands = ['H', 'Q', '9', '+', 'exit', 'help']

    def __init__(self):
        self.__counter = 0
        self.__show_available_commands()
        pass

    def __show_available_commands(self):
        for index, cmd in enumerate(self.__available_commands):
            print(f'{index}.{cmd}')

    def exec_command(self, command: str):

        match command:
            case 'H':
                print('Hello, World!')
            case 'Q':
                print(input())
            case '+':
                self.__counter += 1
                print(f'Total: {self.__counter}')
            case 'exit':
                print('See ya!')
                exit(0)
            case 'help':
                self.__show_available_commands()
            case '9':
                for bottle in range(99, 0, -1):
                    with_right_postfix = 'bottles' if bottle != 1 else 'bottle'
                    print('{0} {1} of beer on the wall, {0} {1} of beer.'.format(
                        bottle, with_right_postfix))
                    with_right_postfix = 'bottles' if bottle - 1 != 1 else 'bottle'
                    print('Take one down and pass it around, {} {} of beer on the wall.'.format(
                        bottle - 1 if bottle - 1 != 0 else 'no more', with_right_postfix))
                    print()
                    print(
                        'No more bottles of beer on the wall, no more bottles of beer.')
                    print(
                        'Go to the store and buy some more, 99 bottles of beer on the wall.')

    def start_handling(self):
        command = input(str('Command: '))
        self.exec_command(command)
