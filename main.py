class Example:
    def get_data_user(self):
        marker = True
        while marker:
            try:
                a = int(input("Введите первое число = "))
                b = int(input("Введите второе число = "))
                ch = input("Введите операцию = ")
                marker = False
            except:
                print("Вы ввели неправильно данные")
            finally:
                if a is None:
                    print("Вы ввели неправильно первое число")
                elif b is None:
                    print("Вы ввели неправильно второе число")
                elif ch is None:
                    print("Вы не ввели операцию")
                elif ch is ['+','-','/','*']:
                    print("Вы неправильно ввели операцию")

        self.a,self.b,self.ch =  [a,b,ch]

    def refresh(self):
        match self.ch:
            case '+':
                self.res = self.a + self.b
            case '-':
                self.res = self.a - self.b
            case '/':
                self.res = self.a / self.b
            case '*':
                self.res = self.a * self.b

    def full(self):
        self.get_data_user()
        self.refresh()
        print(self.res)

Example().full()