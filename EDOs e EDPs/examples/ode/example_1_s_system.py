import numpy as np
from models.ode.s_system import gs_system_ode
from solvers.ode.scipy_integrate import solve_ivp
from utils.plotting import plot_lines


def solve_example_1_s_system() -> None:
    print("--- Executando Simulação do S-System Exemplo 1 ---")
    print("Este é o exemplo 3.1.1 do artigo de Liu, Wu e Zhang (2014)")
    print(
        "LIU, Li-Zhi; WU, Fang-Xiang; ZHANG, Wen-Jun. Estimating parameters of S-systems by an auxiliary function guided coordinate descent method. \nSystems Science & Control Engineering, v. 2, n. 1, p. 125–134, dez. 2014."
    )
    # Parâmetros e condições iniciais
    alpha = np.array([12, 8, 3, 2])
    beta = np.array([10, 3, 5, 6])
    g = np.array([[0, 0, -0.8, 0], [0.5, 0, 0, 0], [0, 0.75, 0, 0], [0.5, 0, 0, 0]])
    h = np.array([[0.5, 0, 0, 0], [0, 0.75, 0, 0], [0, 0, 0.5, 0.2], [0, 0, 0, 0.8]])
    X0 = np.array([10, 1, 2, 3])
    t_span = (0, 5)  # solve_ivp prefere t_span como uma tupla (início, fim)
    t_eval = np.arange(t_span[0], t_span[1] + 0.1, 0.1)

    # Chamada ao solver usando o método 'args' que é mais limpo
    sol = solve_ivp(
        fun=gs_system_ode,
        t_span=t_span,
        y0=X0,
        t_eval=t_eval,
        args=(alpha, beta, g, h),  # Passando os parâmetros extras
        method="BDF",  # Método de Runge-Kutta de ordem 4(5)
    )

    # Plotando os resultados
    if sol.success:
        print("Solução encontrada com sucesso. Plotando resultados...")
        plot_lines(
            x=sol.t,
            ys=sol.y,
            labels=[f"$X_{i + 1}$" for i in range(sol.y.shape[0])],
            title="Solução do S-System Exemplo 1",
            xlabel=r"$t$",
            ylabel=r"$X_i(t)$",
            grid=True,
            specify_y_lim=True,
            y_lim=(0, np.max(sol.y)),
            legend=True,
            linewidth=4,
        )
    else:
        print("Ocorreu um erro ao resolver a EDO:", sol.message)

    print("--- Simulação Exemplo 1 Concluída ---\n")


# Este bloco permite que o script ainda seja executável por si só
if __name__ == "__main__":
    solve_example_1_s_system()
