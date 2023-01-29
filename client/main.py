import psycopg2
from config import host, user, password, db_name

def decompose(n):
  i = 2 # Первоначальный множитель
  primeFactors = [] # Массив с найдеными простыми множителями
  while i * i <= n:
      while n % i == 0:
          primeFactors.append(i)
          n = int(n / i)
      i = i + 1
  if n > 1:
      primeFactors.append(n)
  return primeFactors

try:
    # Соединение с БД
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name
    )
    connection.autocommit = True

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE EnteredNumbers(
    #             ID serial PRIMARY KEY,
    #             Number int NOT NULL);"""
    #         )

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE PrimeFactors(
    #             ID serial PRIMARY KEY,
    #             prfactors varchar(50) NOT NULL);"""
    #         )

    #     print("[INFO] Таблица успешно создана.")

    task = 0
    while True:
        task = int(input("\nВыберите действие:\n " +
        "1.Ввод числа для расчёта простых множителей.\n " +
        "2.Просмотр множителей для числа.\n " +
        "3.Завершение работы.\n " +
        "Действие №"))
        print()

        if task == 1: # Расчёт простых множителей для введённого числа, и внесение данных в БД
            number = int(input("Введите число: "))
            array = decompose(number)

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO enterednumbers (number) VALUES (%s);
                    INSERT INTO primefactors (prfactors) VALUES (%s)""", (number, array)
                )

        elif task == 2: # Вывод расчитанных простых множителей для УЖЕ СУЩЕСТВУЮЩЕГО числа
            number = int(input("Введите число: "))

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT prfactors FROM enterednumbers, primefactors WHERE enterednumbers.number = (%s) AND enterednumbers.id = primefactors.id;""", ([number])
                )
                pf = cursor.fetchone()
                if pf != None:
                    print(str(pf)[3:-4])
                else:
                    print("Число не найдено!")


        elif task == 3: # Выход из цикла
            break

        else:
            print("Ошибка!\n")


except Exception as ex:
    print("[INFO] Ошибка работы с БД.", ex)

finally:
    if connection:
        connection.close()
        print("[INFO] Соединение закрыто.")
