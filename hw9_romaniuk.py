
#  Функція декоратор

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            print('Enter user name')
        except ValueError:
            print('Value is not correct')
        except IndexError:
            print('Give me name and phone please')
        except TypeError:
            print('Enter the correct command')
    return wrapper

# __Функції____________________


@ input_error
def hello(*args) -> str:
    return "How can I help you?"


@ input_error
def exit(*args) -> str:
    return "Bye!"


@ input_error
def add(*args):
    if len(args) < 2:
        return "Give me name and phone please!"
    else:
        phone_book[args[0]] = args[1]
        return "Contact add successful!"


@ input_error
def show_all(*args):
    print(phone_book)
    return "End of phone book!"


@ input_error
def change(*args):

    for k, v in phone_book.items():
        if k.lower() == args[0].lower():
            phone_book[args[0]] = args[1]
            return "Phone number changed successful!"
        else:
            return f"Contact with name {args[0]} not found!"


@ input_error
def phone(*args):
    if len(args) == 0:
        return "Give me name please!"
    else:
        return f'{args[0]} number is {phone_book.get(args[0])}'


@ input_error
def wrong(*args):
    return f'Unknown command'


#  Функція command_parser - парсер команд
# ___________________________________________________________________________________
COMMAND_DICT = {'hello': hello, 'add': add, 'change': change, 'phone': phone, 'show all': show_all,
                'exit': exit, 'close': exit, 'good bye': exit, }


@input_error
def command_parser(comm):
    comm.strip()
    if comm.lower() in ['hello', 'show all', 'good bye', 'close', 'exit']:
        command = COMMAND_DICT.get(comm.lower())
        data = []
        return command, data
    str_command, *comm_list = comm.split(' ')

    if str_command.lower() in ['add', 'change', 'phone']:
        command = COMMAND_DICT.get(str_command.lower())
        return command, comm_list
    else:
        command = wrong
        return command, comm_list
 # _____________________________________________________________________________


phone_book = {}


if __name__ == "__main__":
    while True:
        user_input = input("Please type command: ")
        command, data = command_parser(user_input)
        if command == exit:
            print(command())
            break
        result = command(*data)
        print(result)
