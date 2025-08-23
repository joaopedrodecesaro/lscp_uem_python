from typing import Sequence

import matplotlib.pyplot as plt
import numpy as np


def plot_lines(
    x: np.ndarray,
    ys: np.ndarray,
    labels: Sequence[str] | None = None,
    colors: Sequence[str] | None = None,
    title: str = "",
    xlabel: str = "X-axis",
    ylabel: str = "Y-axis",
    grid: bool = False,
    linewidth: Sequence[float] | float = 2,
    legend_fontsize: int = 16,
    ticks_fontsize: int = 16,
    title_fontsize: int = 20,
    labels_fontsize: int = 18,
    specify_x_lim: bool = False,
    specify_y_lim: bool = False,
    specify_ticks: bool = False,
    legend: bool = False,
    x_lim: tuple[float, float] = (0, 1),
    y_lim: tuple[float, float] = (0, 1),
    y_step_ticks: float = 0.1,
    x_step_ticks: float = 0.1,
    legend_loc: str = "best",
    font_name: str = "Times New Roman",
):
    default_colors = [
        "#090D85",  # blue
        "#A8150F",  # red
        "#18863D",  # green
        "#820186",  # magenta
        "#FF353C",  # red_2
        "#017D86",  # dark_cyan
        "#EAC703",  # yellow
    ]

    plt.figure(figsize=(8, 8))
    num_lines = ys.shape[0]

    # Determina a lista de cores primária (a do usuário ou a padrão da função)
    primary_colors = list(colors) if colors is not None else default_colors
    # Verifica se a lista primária é suficiente
    if len(primary_colors) < num_lines:
        # Se não for, busca o ciclo de cores padrão do Matplotlib como fallback
        mpl_default_colors = plt.rcParams["axes.prop_cycle"].by_key()["color"]
        # Calcula quantas cores adicionais são necessárias
        num_fallback_colors_needed = num_lines - len(primary_colors)
        # Cria um ciclo com as cores de fallback para garantir que haja o suficiente
        fallback_cycle = mpl_default_colors * (
            num_fallback_colors_needed // len(mpl_default_colors) + 1
        )
        # Constrói a lista final de cores: primárias + fallback
        final_color_list = primary_colors + fallback_cycle[:num_fallback_colors_needed]
    else:
        # Se for suficiente, a lista final é apenas a lista primária (cortada no tamanho exato)
        final_color_list = primary_colors[:num_lines]

    for i in range(num_lines):
        y = ys[i, :]
        label = labels[i] if labels is not None else f"Linha {i + 1}"

        # Seleciona a cor apropriada para a linha atual
        color_to_use = final_color_list[i]

        plt.plot(
            x,
            y,
            label=label,
            color=color_to_use,
            # --------------------------------
            linewidth=linewidth[i] if isinstance(linewidth, Sequence) else linewidth,
        )

    plt.title(title, fontsize=title_fontsize, fontname=font_name)
    plt.xlabel(xlabel, fontsize=labels_fontsize, fontname=font_name)
    plt.ylabel(ylabel, fontsize=labels_fontsize, fontname=font_name)

    if grid:
        plt.grid(True, axis="y", linewidth=0.5, alpha=0.5)
    if not specify_x_lim:
        x_lim = (np.min(x), np.max(x))
        plt.xlim(x_lim)
    else:
        plt.xlim(x_lim)
    if not specify_y_lim:
        y_lim = (np.min(ys), np.max(ys))
        plt.ylim(y_lim)
    else:
        plt.ylim(y_lim)
    if legend:
        plt.legend(loc=legend_loc, prop={"family": font_name, "size": legend_fontsize})
    if not specify_ticks:
        x_step_ticks = (x_lim[1] - x_lim[0]) / 5
        y_min, y_max = y_lim
        y_step_ticks = (y_max - y_min) / 5

    plt.xticks(
        np.arange(x_lim[0], x_lim[1] + x_step_ticks, x_step_ticks),
        fontname=font_name,
        fontsize=ticks_fontsize,
    )
    plt.yticks(
        np.arange(y_min, y_max + y_step_ticks, y_step_ticks),
        fontname=font_name,
        fontsize=ticks_fontsize,
    )
    plt.tight_layout()
    plt.show()
