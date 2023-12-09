import bcrypt

from store import Store
from user import Client, Administrator

store = Store()

while True:
    print("---------------------------------------------------------------------------\nЧтобы войти в reStore, вам необходимо авторизоваться или зарегистрироваться\n---------------------------------------------------------------------------")

    print("1 - Авторизоваться")
    print("2 - Зарегистрироваться")
    print("3 - Выйти")
    choice = input("\nВыберите действие: ")

    if choice == '1':
        print("------------\nАвторизация\n------------")
        print("1 - Авторизоваться как клиент")
        print("2 - Авторизоваться как сотрудник")
        print("3 - Вернуться назад")
        auth_choice = input("\nВыберите действие: ")

        if auth_choice == '1':
            client = Client(store)

            while True:
                login_client = input("\nВведите логин: ")
                password_client = input("Введите пароль: ")

                if login_client.strip() and password_client.strip():
                    break
                else:
                    print("-------------------------------------------------------------------\nЛогин и пароль не могут быть пустыми. Пожалуйста, попробуйте снова.\n-------------------------------------------------------------------")

            if client.authenticate(login_client, password_client):
                print("\nАвторизация прошла успешно!")
            else:
                continue

            while True:
                print("---------------------------\nДобро пожаловать в reStore!\n---------------------------")
                print("1 - Товары")
                print("2 - Корзина")
                print("3 - Выйти")

                client_action = input("\nВыберите действие: ")

                if client_action == '1':
                    client.display_products()
                    add_to_cart = input("\nВведите номер товара для добавления в корзину (или '0' для возвращения назад): ")

                    if add_to_cart == '0':
                        continue

                    try:
                        product_id = int(add_to_cart)
                        products = client.display_products()
                        if 1 <= product_id <= len(products):
                            client.add_to_cart(product_id)
                            print(f"----------------------------------------------------------\nТовар '{products[product_id - 1][1]}' добавлен в корзину.\n----------------------------------------------------------")
                        else:
                            print("----------------------------------------------------\nНеверный номер товара. Пожалуйста, попробуйте снова.\n----------------------------------------------------")
                    except ValueError:
                        print("-----------------------------------------\nНеверный ввод. Пожалуйста, введите число.\n-----------------------------------------")

                elif client_action == '2':
                    client.display_cart()

                    print("\n1 - Оформить заказ")
                    print("2 - Вернуться назад")
                    cart_choice = input("\nВыберите действие: ")

                    if cart_choice == '1':
                        print("-----------------\nОформление заказа\n-----------------")

                        address = input("\nВведите адрес доставки: ")
                        client.checkout(address)
                        break

                    elif cart_choice == '2':
                        continue

                elif client_action == '3':
                    print("-----------------------------------------\nДо свидания, будем рады снова видеть вас!\n-----------------------------------------")
                    break

        elif auth_choice == '2':
            administrator = Administrator(store)

            while True:
                administrator_login = input("\nВведите логин: ")
                administrator_password = input("Введите пароль: ")

                if administrator_login.strip() and administrator_password.strip():
                    break
                else:
                    print("-------------------------------------------------------------------\nЛогин и пароль не могут быть пустыми. Пожалуйста, попробуйте снова.\n-------------------------------------------------------------------")

            if administrator.authenticate(administrator_login, administrator_password):
                print("\nАвторизация прошла успешно!")

                while True:
                    print("------------------------------------\nЧто бы вы хотели изменить в reStore?\n------------------------------------")
                    print("\n1 - Добавить товар")
                    print("2 - Удалить товар")
                    print("3 - Изменить название товара")
                    print("4 - Выйти")

                    administrator_action = input("\nВыберите действие: ")

                    if administrator_action == '1':
                        print("-----------------\nПроцесс добавления товара...\n-----------------")
                        while True:
                            product_name = input("\nВведите название товара: ")
                            product_price = input("Введите цену товара: ")
                            try:
                                product_price = float(product_price)
                                if product_name.strip() and product_price >= 0:
                                    administrator.add_product(product_name, product_price)
                                    print(f"----------------------------------------------------------\nТовар '{product_name}' успешно добавлен.\n----------------------------------------------------------")
                                    break
                                else:
                                    print("--------------------------------------------------------------------\nНазвание товара не может быть пустым, а цена должна быть неотрицательной.\n--------------------------------------------------------------------")
                            except ValueError:
                                print("---------------------------------------------------------\nНеверный формат цены. Пожалуйста, введите число.\n---------------------------------------------------------")

                    elif administrator_action == '2':
                        print("--------------------------\nПроцесс удаления товара...\n--------------------------")
                        while True:
                            product_name_to_delete = input("\nВведите название товара для удаления (или '0' для возвращения назад): ")

                            if product_name_to_delete == '0':
                                break

                            administrator.remove_product(product_name_to_delete)
                            print(f"----------------------------------------------------------\nТовар '{product_name_to_delete}' успешно удален.\n----------------------------------------------------------")
                            break

                    elif administrator_action == '3':
                        print("--------------------------\nПроцесс изменения названия товара...\n--------------------------")
                        while True:
                            product_name_to_change = input("\nВведите название товара для изменения (или '0' для возвращения назад): ")

                            if product_name_to_change == '0':
                                break

                            new_product_name = input("Введите новое название товара: ")
                            administrator.change_product_name(product_name_to_change, new_product_name)
                            print(f"----------------------------------------------------------\nНазвание товара успешно изменено на '{new_product_name}'.\n----------------------------------------------------------")
                            break

                    elif administrator_action == '4':
                        print("-----------------\nВы успешно вышли!\n-----------------")
                        break
            else:
                print("------------------------------------------------------------\nНеправильный логин или пароль. Пожалуйста, попробуйте снова.\n------------------------------------------------------------")

    elif choice == '2':
        print("-----------\nРегистрация\n-----------")
        print("Логин должен быть не менее 4 символов")

        while True:
            login_client = input("\nПридумайте логин: ")

            if len(login_client) >= 4:
                break
            else:
                print("-------------------------------------------------------------------------------------------------\nЛогин должен содержать не менее 4 символов и не должен быть пустым. Пожалуйста, попробуйте снова.\n-------------------------------------------------------------------------------------------------")

        while True:
            password_client = input("Придумайте пароль: ")

            if len(password_client) > 0:
                break
            else:
                print("----------------------------------------------------------\nПароль не может быть пустым. Пожалуйста, попробуйте снова.\n----------------------------------------------------------")

        store.cursor.execute('SELECT * FROM users WHERE login = ?', (login_client,))
        existing_user = store.cursor.fetchone()

        if existing_user:
            print("-------------------------------------------------------------------------------\nПользователь с таким логином уже существует. Пожалуйста, выберите другой логин.\n-------------------------------------------------------------------------------")


        else:

            hashed_password = bcrypt.hashpw(password_client.encode('utf-8'), bcrypt.gensalt())

            store.cursor.execute('INSERT INTO users (login, password) VALUES (?, ?)', (login_client, hashed_password))

            store.conn.commit()

            print("\nРегистрация прошла успешно!")

    elif choice == '3':
        print("----------------------------\nВы успешно вышли из reStore!\n----------------------------")
        break

    else:
        print("------------------------------------------------\nНеправильный ввод. Пожалуйста, попробуйте снова.\n------------------------------------------------")

store.close_connection()