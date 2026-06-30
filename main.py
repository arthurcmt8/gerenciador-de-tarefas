import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, indent=4)


def adicionar_tarefa(tarefas):
    nome = input("Digite a tarefa: ")

    tarefa = {
        "nome": nome,
        "concluida": False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

    print("Tarefa adicionada!\n")


def listar_tarefas(tarefas):
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.\n")
        return

    print("\n===== TAREFAS =====")

    for i in range(len(tarefas)):
        status = "✓" if tarefas[i]["concluida"] else " "
        print(f"{i + 1}. [{status}] {tarefas[i]['nome']}")

    print()


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    numero = int(input("Número da tarefa: "))

    if numero >= 1 and numero <= len(tarefas):
        tarefas[numero - 1]["concluida"] = True
        salvar_tarefas(tarefas)
        print("Tarefa concluída!\n")
    else:
        print("Número inválido.\n")


def remover_tarefa(tarefas):
    listar_tarefas(tarefas)

    if len(tarefas) == 0:
        return

    numero = int(input("Número da tarefa: "))

    if numero >= 1 and numero <= len(tarefas):
        tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)
        print("Tarefa removida!\n")
    else:
        print("Número inválido.\n")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("===== GERENCIADOR DE TAREFAS =====")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Remover tarefa")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_tarefa(tarefas)

        elif opcao == "2":
            listar_tarefas(tarefas)

        elif opcao == "3":
            concluir_tarefa(tarefas)

        elif opcao == "4":
            remover_tarefa(tarefas)

        elif opcao == "5":
            print("Até mais!")
            break

        else:
            print("Opção inválida.\n")


menu()