from examples.ode.example_1_s_system import solve_example_1_s_system


def main():
    """
    Função principal (orquestrador) do projeto.
    Decide quais simulações executar.
    """

    # Chama a primeira simulação de exemplo do S-system
    print("Iniciando a simulação do exemplo 1 do S-System...")
    solve_example_1_s_system()


if __name__ == "__main__":
    main()
