from pathlib import Path
import matplotlib.pyplot as plt


def savefig(path: str | Path, **kwargs) -> Path:
    """Save the current matplotlib figure, creating parent directories."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)

    plt.tight_layout()
    plt.savefig(path, **kwargs)
    plt.close()

    return path
