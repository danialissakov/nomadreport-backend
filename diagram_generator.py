import matplotlib.pyplot as plt
import numpy as np

def generate_diagram_dynamic(sectors, completion, title="Отчет", color="#9b5de5"):
    num_sectors = len(sectors)
    angles = np.linspace(0, 2 * np.pi, num_sectors, endpoint=False)
    width = 2 * np.pi / num_sectors

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={'projection': 'polar'})

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 100)

    # Основные лепестки
    bars = ax.bar(
        angles, completion,
        width=width, bottom=0,
        color=color, edgecolor='black', linewidth=1.5,
        alpha=0.85, zorder=3
    )

    ax.set_xticks([])
    ax.set_yticklabels([])

    # Серые линии по границам лепестков
    for angle, value in zip(angles, completion):
        left_edge = angle - width / 2
        right_edge = angle + width / 2
        if value < 100:
            ax.plot([left_edge, left_edge], [value, 100], color='lightgray', linewidth=1.2, zorder=4)
            ax.plot([right_edge, right_edge], [value, 100], color='lightgray', linewidth=1.2, zorder=4)

    # Значения внутри лепестков
    for angle, radius in zip(angles, completion):
        ax.text(
            angle, radius - 5, f"{radius}%",
            ha='center', va='center',
            fontsize=9, color='white', fontweight='bold', zorder=5
        )

    # Подписи лепестков — всегда горизонтальные
    for angle, label in zip(angles, sectors):
        label_radius = 115 + len(label) * 0.8  # Отодвигаем в зависимости от длины текста

        ax.text(
            angle, label_radius, label,
            ha='center', va='center',
            rotation=0,
            fontsize=9,
            zorder=6
        )

    # Заголовок — по центру
    plt.title(title, fontsize=16, y=1.13, ha='center')

    # Добавим нижний отступ, чтобы не слипалось
    fig.subplots_adjust(bottom=0.2)

    file_path = "diagram.png"
    plt.savefig(file_path, dpi=300)
    plt.close()
    return file_path
