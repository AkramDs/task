def decorator(func):
    def wrapper():
        try:
            result = func()
        except TypeError as e:
            e = str(e).split('\'')

            if e[1] == 'new_password':
                print('Вы не вели новый пароль!')

            elif e[1] == 'input_username':
                print('Вы не вели имя пользывателя!')

            else:
                print('Это не должно появится (если вы это видете то кто-то петух)')
                
    return wrapper

class User:
    username = 'akram'
    password = 'qwerty'
    balance = 9.64


    def get_account_balance(self, input_username):
        self.input_username = input_username

        if input_username == self.username:
            return balance

    def change_password(self, new_password):
        self.new_password = new_password

        self.password = new_password

@decorator
def main():
    u = User()

    u.change_password()
    u.get_account_balance()

if __name__ == '__main__':
    main()
