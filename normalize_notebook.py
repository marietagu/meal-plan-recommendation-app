import nbformat

# Load the notebook
with open("EDA & Data modeling.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Normalize the notebook
nbformat.validate(nb, relax_add_props=True)

# Save the normalized notebook
with open("EDA & Data modeling.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
