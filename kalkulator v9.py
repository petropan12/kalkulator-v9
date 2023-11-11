n = input("Русский,English,Deutsch,Français")
if n == "Русский":
    m = input("Привет, я твой калькулятор если хотите за кончить то напишите нет")
    while m != "нет":
        print("1)Сумма")
        print("2)Вычетание")
        print("3)Умножение")
        print("4)Деление")
        print("5)Целочисленое деление")
        print("6)Остаток деления")
        print("7)Возведение в степень")
        print("8)Выведение квадратного корня из числа")
        print("10)Анализ числа(Пока не готово!!!)")
        n = input("Ваше действие")
        if n == "1" or n == "Сумма" or n == "+":
           a = int(input("Введите ваше первое число"))
           b = int(input("Введите ваше второе число"))
           c = str(a)
           d = str(b)
           if c == 0 or d == 0:
              print("Что за фигня где число")
           else:
               print(a, "+", b, "=", a + b)
        else:
            if n == "2" or n == "Вычетание" or n == "-":
               a = int(input("Введите ваше первое число"))
               b = int(input("Введите ваше второе число"))
               c = str(a)
               d = str(b)
               if c == 0 or b == 0:
                   print("Что за фигня где число")
               else:
                   print(a, "-", b, "=", a - b)
            else:
                if n == "3" or n == "Умножение" or n == "*":
                    a = int(input("Введите ваше первое число"))
                    b = int(input("Введите ваше второе число"))
                    c = str(a)
                    d = str(b)
                    if c == 0 or d == 0:
                        print("Что за фигня где число")
                    else:
                        print(a, "*", b, "=", a * b)
                else:
                    if n == "4" or n == "Деление" or n == "/":
                       a = int(input("Введите ваше первое число"))
                       b = int(input("Введите ваше второе число"))
                       c = str(a)
                       d = str(b)
                       if c == 0 or d == 0:
                            print("Что за фигня где число")
                       else:
                           if b == 0:
                              print("Делить на 0 нельзя без разрешения учителя математики")
                           else:
                               print(a, "/", b, "=", a / b)
                    else:
                        if n == "5" or n == "Целочисленое деление" or n == "//":
                           a = int(input("Введите ваше первое число"))
                           b = int(input("Введите ваше второе число"))
                           c = str(a)
                           d = str(b)
                           if c == 0 or d == 0:
                              print("Что за фигня где число")
                           else:
                               if b == 0:
                                  print("Делить на 0 нельзя без разрешения учителя математики")
                               else:
                                   print(a, "//", b, "=", a // b)
                        else:
                            if n == "6" or n == "Остаток деления" or n == "%":
                               a = int(input("Введите ваше первое число"))
                               b = int(input("Введите ваше второе число"))
                               c = str(a)
                               d = str(b)
                               if c == 0 or d == 0:
                                  print("Что за фигня где число")
                               else:
                                   if b == 0:
                                      print("Делить на 0 нельзя без разрешения учителя математики")
                                   else:
                                       print(a, "%", b, "=", a % b)
                            else:
                                if n == "7" or n == "возведение в степень" or n == "**":
                                    a = int(input("Введите ваше первое число"))
                                    b = int(input("Введите ваше второе число"))
                                    print(a, "**", b, "=", a ** b)
                                else:
                                    if n == "8" or n == "Выведение квадратного корня из числа" or n == "**/":
                                       a = int(input("Введите число"))
                                       b = 0.5
                                       c = str(a)
                                       if c == 0:
                                          print("Что за фигня где число")
                                       else:
                                           if a < 0:
                                              print("Это как, отрицательное число? Нельзя!")
                                           else:
                                               print(a, "**/", "0.5", "=", a ** b)
                                    else:
                                        if n == "9" or n == "Смена системы счисления" or n == "<>":
                                           a = int(float(input("Введите число для перевода")))
                                        if n == "10" or n == "Анализ числа" or n == "=":
                                           a = int(input("Введите число"))
                                           b = str(a)
                                           if b == 0:
                                              print("Что за фигня где число")
                                           else:
                                               if b > 9:
                                                  print("Слишком много цифр!")
                                               else:
                                                   print(b)
                                                   if b == 9:
                                                      c = b // 100000000
                                                      d = b % 100000000
                                                      e = d // 10000000
                                                      d = b % 10000000
                                                      f = d // 1000000
                                                      d = b % 1000000
                                                      h = d // 100000
                                                      d = b % 100000
                                                      k = d // 10000
                                                      d = b % 10000
                                                      g = d // 1000
                                                      d = b % 1000
                                                      j = d // 100
                                                      d = b % 100
                                                      s = d // 10
                                                      d = b % 10
                                                      print(c, e, f, h, k, g, j, s, d)
                                                   else:
                                                       if b == 8:
                                                          e = b // 10000000
                                                          d = b % 10000000
                                                          f = d // 1000000
                                                          d = b % 1000000
                                                          h = d // 100000
                                                          d = b % 100000
                                                          k = d // 10000
                                                          d = b % 10000
                                                          g = d // 1000
                                                          d = b % 1000
                                                          j = d // 100
                                                          d = b % 100
                                                          s = d // 10
                                                          d = b % 10 
                                                          print(e, f, h, k, g, j, s, d)
                                                       else:
                                                           if b == 7:
                                                              f = b // 1000000
                                                              d = b % 1000000
                                                              h = d // 100000
                                                              d = b % 100000
                                                              k = d // 10000
                                                              d = b % 10000
                                                              g = d // 1000
                                                              d = b % 1000
                                                              j = d // 100
                                                              d = b % 100
                                                              s = d // 10
                                                              d = b % 10
                                                              print(f, h, k, g, j, s, d)
                                                           else:
                                                               if b == 6:
                                                                  h = b // 100000
                                                                  d = b % 100000
                                                                  k = d // 10000
                                                                  d = b % 10000
                                                                  g = d // 1000
                                                                  d = b % 1000
                                                                  j = d // 100
                                                                  d = b % 100
                                                                  s = d // 10
                                                                  d = b % 10
                                                                  print(h, k, g, j, s, d)
                                                               else:
                                                                   if b == 5:
                                                                      k = b // 10000
                                                                      d = b % 10000
                                                                      g = d // 1000
                                                                      d = b % 1000
                                                                      j = d // 100
                                                                      d = b % 100
                                                                      s = d // 10
                                                                      d = b % 10
                                                                      print(k, g, j, s, d)
                                                                   else:
                                                                       if b == 4:
                                                                          g = b // 1000
                                                                          d = b % 1000
                                                                          j = d // 100
                                                                          d = b % 100
                                                                          s = d // 10
                                                                          d = b % 10
                                                                          print(g, j, s, d)
                                                                       else:
                                                                           if b == 3:
                                                                              j = b // 100
                                                                              d = b % 100
                                                                              s = d // 10
                                                                              d = b % 10
                                                                              print(j, s, d)
                                                                           else:
                                                                               if b == 2:
                                                                                  s = b // 10
                                                                                  d = b % 10
                                                                                  print(s, d)
                                                                               else:
                                                                                   if b == 1:
                                                                                      d = b % 10
                                                                                      print(d)               
                                                                                      q = a // 2
                                                                                      if q == 0:
                                                                                         print("чётное")
                                                                                      else:
                                                                                          print("нечётное")
                                                                                          if b == 9:
                                                                                             c = a // 100000000
                                                                                             d = a % 100000000
                                                                                             e = d // 10000000
                                                                                             d = a % 10000000
                                                                                             f = d // 1000000
                                                                                             d = a % 1000000
                                                                                             h = d // 100000
                                                                                             d = a % 100000
                                                                                             k = d // 10000
                                                                                             d = a % 10000
                                                                                             g = d // 1000
                                                                                             d = a % 1000
                                                                                             j = d // 100
                                                                                             d = a % 100
                                                                                             s = d // 10
                                                                                             d = a % 10
                                                                                             print(c + d + e + f + h + k + g + j + s)
                                                                                          else:
                                                                                              if b == 8:
                                                                                                 e = a // 10000000
                                                                                                 d = a % 10000000
                                                                                                 f = d // 1000000
                                                                                                 d = a % 1000000
                                                                                                 h = d // 100000
                                                                                                 d = a % 100000
                                                                                                 k = d // 10000
                                                                                                 d = a % 10000
                                                                                                 g = d // 1000
                                                                                                 d = a % 1000
                                                                                                 j = d // 100
                                                                                                 d = a % 100
                                                                                                 s = d // 10
                                                                                                 d = a % 10 
                                                                                                 print(e + f + h + k + g + j + s + d)
                                                                                              else:
                                                                                                  if b == 7:
                                                                                                     f = a // 1000000
                                                                                                     d = a % 1000000
                                                                                                     h = d // 100000
                                                                                                     d = a % 100000
                                                                                                     k = d // 10000
                                                                                                     d = a % 10000
                                                                                                     g = d // 1000
                                                                                                     d = a % 1000
                                                                                                     j = d // 100
                                                                                                     d = a % 100
                                                                                                     s = d // 10
                                                                                                     d = a % 10
                                                                                                     print(f + h + k + g + j + s + d)
                                                                                                  else:
                                                                                                      if b == 6:
                                                                                                         h = a // 100000
                                                                                                         d = a % 100000
                                                                                                         k = d // 10000
                                                                                                         d = a % 10000
                                                                                                         g = d // 1000
                                                                                                         d = a % 1000
                                                                                                         j = d // 100
                                                                                                         d = a % 100
                                                                                                         s = d // 10
                                                                                                         d = a % 10
                                                                                                         print(h + k + g + j + s + d)
                                                                                                      else:
                                                                                                          if b == 5:
                                                                                                             k = a // 10000
                                                                                                             d = a % 10000
                                                                                                             g = d // 1000
                                                                                                             d = a % 1000
                                                                                                             j = d // 100
                                                                                                             d = a % 100
                                                                                                             s = d // 10
                                                                                                             d = a % 10
                                                                                                             print(k + g + j + s + d)
                                                                                                          else:
                                                                                                              if b == 4:
                                                                                                                 g = a // 1000
                                                                                                                 d = a % 1000
                                                                                                                 j = d // 100
                                                                                                                 d = a % 100
                                                                                                                 s = d // 10
                                                                                                                 d = a % 10
                                                                                                                 print(g + j + s + d)
                                                                                                              else:
                                                                                                                  if b == 3:
                                                                                                                     j = a // 100
                                                                                                                     d = a % 100
                                                                                                                     s = d // 10
                                                                                                                     d = a % 10
                                                                                                                     print(j + s + d)
                                                                                                                  else:
                                                                                                                      if b == 2:
                                                                                                                         s = a // 10
                                                                                                                         d = a % 10
                                                                                                                         print(s + d)
                                                                                                                      else:
                                                                                                                          d = a % 10
                                                                                                                          print(b)
                                                                                                                          z = 1
                                                                                                                          w = 0
                                                                                                                          while z != b:
                                                                                                                                x = b % z
                                                                                                                                if x != 0:
                                                                                                                                   w = w + 1
                                                                                                                                   z = z + 1 
                                                                                                                                else:
                                                                                                                                    z = z + 1
                                                                                                                          if w > 2:
                                                                                                                             print("Данное число не является простым")
                                                                                                                          else:
                                                                                                                              print("данное число является простым")
                                                                                                                              aa = a ** 0.5
                                                                                                                              aaa = aa ** 2
                                                                                                                              if aaa == aa:
                                                                                                                                 print("Данное число является полным квадратом")
                                                                                                                              else:
                                                                                                                                  print("Данное число не является полным квадратом")
                                                                                                                                  bb = 1 // 3
                                                                                                                                  aa = a ** bb
                                                                                                                                  aaa = aa ** 2
                                                                                                                                  if aaa == aa:
                                                                                                                                     print("Данное число является полным кубом")
                                                                                                                                  else:
                                                                                                                                      print("Данное число не является полным кубом")
    m = input("хотите ещё")
    if n == English: 
        m = input("Hello, I'm your calculator, If you want to finish, write no")
        while m != "no":
            print("1)Sum")
            print("2)Subtraction")
            print("3)Multiplication")
            print("4)Division")
            print("5)Integer division")
            print("6)Remainder of the division")
            print("7)Exponentiation")
            print("8)Deducing the square root of a number")
            n = input("Your action")
            if n == "1" or n == "Sum" or n == "+":
               a = int(input("Enter your first number"))
               b = int(input("Enter your second number"))
               c = str(a)
               d = str(b)
               if c == 0 or d == 0:
                  print("What the hell is the number")
               else:
                   print(a, "+", b, "=", a + b)
            else:
                if n == "2" or n == "Subtraction" or n == "-":
                   a = int(input("Enter your first number"))
                   b = int(input("Enter your second number"))
                   c = str(a)
                   d = str(b)
                   if c == 0 or d == 0:
                      print("What the hell is the number")
                   else:
                       print(a, "-", b, "=", a - b)
                else:
                    if n == "3" or n == "Multiplication" or n == "*":
                       a = int(input("Enter your first number"))
                       b = int(input("Enter your second number"))
                       c = str(a)
                       d = str(b)
                       if c == 0 or d == 0:
                          print("What the hell is the number")
                       else:
                           print(a, "*", b, "=", a * b)
                    else:
                        if n == "4" or n == "Division" or n == "/":
                           a = int(input("Enter your first number"))
                           b = int(input("Enter your second number"))
                           c = str(a)
                           d = str(b)
                           if c == 0 or d == 0:
                              print("What the hell is the number")
                           else:
                               if b == 0:
                                  print("It is impossible to divide by 0 without the permission of the math teacher")
                               else:
                                   print(a, "/", b, "=", a / b)
                        else:
                            if n == "5" or n == "Integer division" or n == "//":
                               a = int(input("Enter your first number"))
                               b = int(input("Enter your second number"))
                               c = str(a)
                               d = str(b)
                               if c == 0 or d == 0:
                                  print("What the hell is the number")
                               else:
                                   if b == 0:
                                      print("It is impossible to divide by 0 without the permission of the math teacher")
                                   else:
                                       print(a, "//", b, "=", a // b)
                            else:
                                if n == "6" or n == "Remainder of the division" or n == "%":
                                   a = int(input("Enter your first number"))
                                   b = int(input("Enter your second number"))
                                   c = str(a)
                                   d = str(d)
                                   if c == 0 or d == 0:
                                      print("What the hell is the number")
                                   else:
                                       if b == 0:
                                          print("It is impossible to divide by 0 without the permission of the math teacher")
                                       else:   
                                           print(a, "%", b, "=", a % b)
                                else:
                                    if n == "7" or n == "Exponentiation" or n == "**":
                                       a = int(input("Enter your first number"))
                                       b = int(input("Enter your second number"))
                                       c = str(a)
                                       d = str(b)
                                       if c == 0 or d == 0:
                                          print("What the hell is the number")
                                       else:   
                                           print(a, "**", b, "=", a ** b)
                                    else:
                                        if n == "8" or n == "Deducing the square root of a number" or n == "**/":
                                           a = int(input("Enter a number"))
                                           b = 0.5
                                           c = str(a)
                                           if c == 0:
                                              print("What the hell is the number")
                                           else:
                                               if a < 0:
                                                  print("Is that like a negative number? You can't!")
                                               else:
                                                   print(a, "**/", "0.5", "=", a ** b)
            m = input("Do you want to continue?")               
    else:
        if n == "Deutsch":
            m = input("Hallo, ich bin dein Rechner, Wenn du fertig sein willst, schreibe nein")
        while m != "nein":
         print("1)Summe")
         print("2)Subtraktion")
         print("3)Multiplikation")
         print("4)Division")
         print("5)Ganzzahlige Division")
         print("6)Rest der Division")
         print("7)Potenzierung")
         print("8)Eine Quadratwurzel aus einer Zahl entfernen")
         n = input("Ihre Aktion")
         if n == "1" or n == "Summe" or n == "+":
            a = int(input("Geben Sie Ihre erste Nummer ein"))
            b = int(input("Geben Sie Ihre zweite Nummer ein"))
            c = str(a)
            d = str(b)
            if c == 0 or d == 0:
               print("Was zum Teufel ist die Nummer")
            else:
                print(a, "+", b, "=", a + b)
         else:
             if n == "2" or n == "Subtraction" or n == "-":
                a = int(input("Geben Sie Ihre erste Nummer ein"))
                b = int(input("Geben Sie Ihre zweite Nummer ein"))
                c = str(a)
                d = str(b)
                if c == 0 or d == 0:
                   print("Was zum Teufel ist die Nummer")
                else:
                    print(a, "-", b, "=", a - b)
             else:
                 if n == "3" or n == "Multiplication" or n == "*":
                    a = int(input("Geben Sie Ihre erste Nummer ein"))
                    b = int(input("Geben Sie Ihre zweite Nummer ein"))
                    c = str(a)
                    d = str(b)
                    if c == 0 or d == 0:
                       print("Was zum Teufel ist die Nummer") 
                    else: 
                        print(a, "*", b, "=", a * b)
                 else:
                     if n == "4" or n == "Division" or n == "/":
                        a = int(input("Geben Sie Ihre erste Nummer ein"))
                        b = int(input("Geben Sie Ihre zweite Nummer ein"))
                        c = str(a)
                        d = str(b)
                        if c == 0 or d == 0:
                           print("Was zum Teufel ist die Nummer")
                        else:
                            if b == 0:
                               print("Es ist unmöglich, ohne Erlaubnis des Mathematiklehrers durch 0 zu teilen.")
                            else:
                                print(a, "/", b, "=", a / b)
                     else:
                         if n == "5" or n == "Ganzzahlige Division" or n == "//":
                            a = int(input("Geben Sie Ihre erste Nummer ein"))
                            b = int(input("Geben Sie Ihre zweite Nummer ein"))
                            c = str(a)
                            d = str(b)
                            if c == 0 or d == 0:
                               print("Was zum Teufel ist die Nummer")
                            else:
                                if b == 0:
                                   print("Es ist unmöglich, ohne Erlaubnis des Mathematiklehrers durch 0 zu teilen.")
                                else:
                                    print(a, "//", b, "=", a // b)
                         else:
                               if n == "6" or n == "Rest der Division" or n == "%":
                                  a = int(input("Geben Sie Ihre erste Nummer ein"))
                                  b = int(input("Geben Sie Ihre zweite Nummer ein"))
                                  c = str(a)
                                  d = str(b)
                                  if c == 0 or d == 0:
                                     print("Was zum Teufel ist die Nummer")
                                  else:
                                      if b == 0:
                                         print("Es ist unmöglich, ohne Erlaubnis des Mathematiklehrers durch 0 zu teilen.")
                                      else:
                                          print(a, "%", b, "=", a % b)
                               else:
                                   if n == "7" or n == "Potenzierung" or n == "**":
                                      a = int(input("Geben Sie Ihre erste Nummer ein"))
                                      b = int(input("Geben Sie Ihre zweite Nummer ein"))
                                      c = str(a)
                                      d = str(b)
                                      if c == 0 or d == 0:
                                         print("Was zum Teufel ist die Nummer")
                                      print(a, "**", b, "=", a ** b)
                                   else:
                                       if n == "8" or n == "Eine Quadratwurzel aus einer Zahl entfernen" or n == "**/":
                                          a = int(input("Geben Sie eine Zahl ein"))
                                          b = 0.5
                                          c = str(a)
                                          if c == 0:
                                             print("Was zum Teufel ist die Nummer")
                                          else:
                                              if a < 0:
                                                 print("Ist das wie eine negative Zahl? Du kannst nicht!")
                                              else:   
                                                  print(a, "**/", "0.5", "=", a ** b)
         m = input("Möchten Sie fortfahren?")
        else:
            if n == "Français":
                m = input("Bonjour, je suis votre calculatrice, si vous voulez finir, écrivez non")
        while m != "pas":
            print("1)Resultat")
            print("2)Soustraction")
            print("3)Multiplication")
            print("4)Separation")
            print("5)Division Entiere")
            print("6)Reste de la Division")
            print("7)Potenzierung")
            print("8)Supprimer une racine carrée d'un nombre")
            n = input("Votre Action")
            if n == "1" or n == "Resultat" or n == "+":
               a = int(input("Entrez votre premier numéro"))
               b = int(input("Entrez votre deuxième numéro"))
               c = str(a)
               d = str(b)
               if c == 0 or d == 0:
                  print("Qu'est-ce que C'est que le nombre")
               else:
                   print(a, "+", b, "=", a + b)
            else:
                if n == "2" or n == "Soustraction" or n == "-":
                   a = int(input("Entrez votre premier numéro"))
                   b = int(input("Entrez votre deuxième numéro"))
                   c = str(a)
                   d = str(b)
                   if c == 0 or d == 0:
                      print("Qu'est-ce que C'est que le nombre")
                   else:   
                       print(a, "-", b, "=", a - b)
                else:
                     if n == "3" or n == "Multiplication" or n == "*":
                        a = int(input("Entrez votre premier numéro"))
                        b = int(input("Entrez votre deuxième numéro"))
                        c = str(a)
                        d = str(b)
                        if c == 0 or d == 0:
                           print("Qu'est-ce que C'est que le nombre")
                        else:   
                            print(a, "*", b, "=", a * b)
                     else:
                         if n == "4" or n == "Separation" or n == "/":
                            a = int(input("Entrez votre premier numéro"))
                            b = int(input("Entrez votre deuxième numéro"))
                            c = str(a)
                            d = str(b)
                            if c == 0 or d == 0:
                               print("Qu'est-ce que C'est que le nombre")
                            else:
                                if b == 0:
                                   print("Il est impossible de diviser par 0 sans la permission du professeur de mathématiques.")
                                else:   
                                    print(a, "/", b, "=", a / b)
                         else:
                             if n == "5" or n == "Division Entiere" or n == "//":
                                a = int(input("Entrez votre premier numéro"))
                                b = int(input("Entrez votre deuxième numéro"))
                                c = str(a)
                                d = str(b)
                                if c == 0 or d == 0:
                                   print("Qu'est-ce que C'est que le nombre")
                                else:
                                    if b == 0:
                                       print("Il est impossible de diviser par 0 sans la permission du professeur de mathématiques.")
                                    else:   
                                        print(a, "//", b, "=", a // b)
                             else:
                                 if n == "6" or n == "Reste de la Division" or n == "%":
                                    a = int(input("Entrez votre premier numéro"))
                                    b = int(input("Entrez votre deuxième numéro"))
                                    c = str(a)
                                    d = str(b)
                                    if c == 0 or d == 0:
                                       print("Qu'est-ce que C'est que le nombre")
                                    else:
                                        if b == 0:
                                           print("Il est impossible de diviser par 0 sans la permission du professeur de mathématiques.")
                                        else:   
                                            print(a, "%", b, "=", a % b)
                                 else:
                                     if n == "7" or n == "Potenzierung" or n == "**":
                                        a = int(input("Entrez votre premier numéro"))
                                        b = int(input("Entrez votre deuxième numéro"))
                                        c = str(a)
                                        d = str(b)
                                        if c == 0 or d == 0:
                                           print("Qu'est-ce que C'est que le nombre")
                                        else:
                                            print(a, "**", b, "=", a ** b)
                                     else:
                                         if n == "8" or n == "Supprimer une racine carrée d'un nombre" or n == "**/":
                                            a = int(input("Entrez un nombre"))
                                            b = 0.5
                                            c = str(a)
                                            if c == 0 or d == 0:
                                               print("Qu'est-ce que C'est que le nombre")
                                            else:
                                                if a < 0:
                                                   print("Est - ce comme un nombre négatif? Vous ne pouvez pas!")
                                                else:
                                                    print(a, "**/", "0.5", "=", a ** b)
        m = input("Voulez-vous continuer?")
