usuarios = []

while True:
    print("\n=== SISTEMA DE USUÁRIOS ===")
    print("1 - Cadastrar usuário")
    print("2 - Fazer login")
    print("3 - Listar usuários")
    print("4 - Remover usuário")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        usuario = input("Novo usuário: ")
        senha = input("Senha: ")
        usuarios.append({"usuario": usuario, "senha": senha})
        print("Usuário cadastrado!")

    elif opcao == "2":
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        encontrado = False

        for u in usuarios:
            if u["usuario"] == usuario and u["senha"] == senha:
                print("Login realizado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Usuário ou senha incorretos.")

    elif opcao == "3":
        for u in usuarios:
            print(u["usuario"])

    elif opcao == "4":
        usuario = input("Usuário para remover: ")

        for u in usuarios:
            if u["usuario"] == usuario:
                usuarios.remove(u)
                print("Usuário removido.")
                break
        else:
            print("Usuário não encontrado.")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")