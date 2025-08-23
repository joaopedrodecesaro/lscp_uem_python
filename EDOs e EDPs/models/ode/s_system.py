import numpy as np


def gs_system_ode(t, X, alpha, beta, g, h):
    r"""
    Autor: Pedro Siscato

    Define o modelo dinâmico de um S-system genérico.

    Esta função calcula as derivadas temporais das concentrações para um
    sistema de N espécies moleculares interagindo, governado pelo formalismo
    do S-system — uma representação não linear em lei de potência comumente
    usada em teoria de sistemas bioquímicos.

    O sistema de EDOs modelado é:

        dX_i/dt = α_i * ∏_j X_j**(g_ij) - β_i * ∏_j X_j**(h_ij),   para i = 1,...,N

    onde:
    - X_i: concentração da espécie i no tempo t;
    - dX_i/dt: taxa líquida de mudança de X_i (produção menos degradação);
    - alpha_i, beta_i: constantes de taxa não-negativas para produção e degradação, respectivamente;
    - g_ij: ordens cinéticas reais descrevendo a influência de X_j sobre X_i na produção;
    - h_ij: ordens cinéticas reais descrevendo a influência de X_j sobre X_i na degradação.

    Interpretação dos parâmetros:
    - Se g_ij > 0, a espécie j ativa a produção de i;
    - Se g_ij < 0, a espécie j inibe a produção de i;
    - Se g_ij = 0, a espécie j não tem efeito sobre a produção de i;
    - A mesma interpretação se aplica para h_ij em termos de degradação.

    Parâmetros de entrada:
    t     - Tempo atual (escalar). Não usado explicitamente, incluído para compatibilidade com solvers de EDOs.
    X     - Vetor coluna (N×1) das concentrações das espécies em t.
    alpha - Vetor coluna (N×1) das constantes de taxa de produção.
    beta  - Vetor coluna (N×1) das constantes de taxa de degradação.
    g     - Matriz (N×N) das ordens cinéticas para produção.
    h     - Matriz (N×N) das ordens cinéticas para degradação.

    Saída:
    dXdt  - Vetor coluna (N×1) com as derivadas temporais das concentrações.
    """

    N = len(X)
    dXdt = np.zeros(N)
    for i in range(N):
        prod_term = np.prod(X ** g[i, :])
        degr_term = np.prod(X ** h[i, :])
        dXdt[i] = alpha[i] * prod_term - beta[i] * degr_term
        # print(f"t={t:.2f}, X={X}, dXdt[{i}]={dXdt[i]:.4f}")
    return dXdt
