def generate_diagram_dynamic(sectors: list[str], values: list[int], title: str, color: str) -> str:
    import matplotlib.pyplot as plt
    import numpy as np
    import uuid
    import os

    if len(sectors) != len(values):
        raise ValueError("Количество секторов и значений должно совпадать")

    angles = np.linspace(0, 2 * np.pi, len(sectors), endpoint=False)
    width = 2 * np.pi / len(sectors)

    fig, ax = plt.subplots(figsize=(9, 9), subplot_kw={'projection': 'polar'})
    bars = ax.bar(angles, values, width=width, bottom=0, color=color, edgecolor='black', alpha=0.8)

    for angle, radius, sector in zip(angles, values, sectors):
        rotation = np.degrees(angle)
        ha = 'left' if 0 <= rotation <= 180 else 'right'
        if 90 < rotation < 270:
            rotation += 180
        ax.text(angle, 120, sector, ha=ha, va='center', rotation=rotation, fontsize=9)

    for angle, radius in zip(angles, values):
        ax.text(angle, radius - 5, f"{radius}%", ha='center', va='center', fontsize=9, color='white', fontweight='bold')

    ax.set_ylim(0, 130)
    ax.set_yticklabels([])
    ax.set_xticklabels([])

    plt.title(title or "Отчет", fontsize=14, pad=20)

    os.makedirs("generated", exist_ok=True)
    filename = f"{uuid.uuid4().hex}.png"
    filepath = os.path.join("generated", filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()

    return filepath