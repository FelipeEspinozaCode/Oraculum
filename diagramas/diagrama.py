import os
import glob
from graphviz import Source

# Carpeta donde está este script (diagramas/)
base_dir = os.path.dirname(os.path.abspath(__file__))

# -----------------------------
# 1️⃣ Borrar imágenes antiguas (.png y .svg)
old_images = glob.glob(os.path.join(base_dir, "*.png")) + glob.glob(os.path.join(base_dir, "*.svg"))

for f in old_images:
    os.remove(f)

# -----------------------------
# 2️⃣ Generar SVGs a partir de los .gv existentes
gv_files = glob.glob(os.path.join(base_dir, "*.gv"))

for gv_path in gv_files:
    s = Source.from_file(gv_path)
    output_path = os.path.splitext(gv_path)[0]
    s.render(filename=output_path, format="svg", view=False, cleanup=True)
