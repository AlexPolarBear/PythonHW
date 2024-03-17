from generator.tex_generator import TEXdocument, TEXtable, TEXimage

table_data = [
    ["buttermilk", 1.25, "cups"],
    ["vegetable oil", 0.25, "cups"],
    ["vanilla extract", 0.5, "teaspoon"],
    ["white sugar", 0.5, "cups"],
    ["all-purpose flour", 1.25, "cups"],
    ["baking powder", 1.5, "teaspoon"],
    ["baking soda", 1, "teaspoon"],
    ["salt", 1, "dash"],
    ["egg", 1, "piece"],
    ["lemon juice", 1, "teaspoon"],
    ["butter", 1, "tablespoon"]
]

image_path = "example.png"

# complete_doc = TEXdocument(image_path=image_path)

with open("artifacts/hw2_1.tex", "w") as file:
    file.write("\\documentclass[12pt]{article}\n\\usepackage{graphicx}\n\n")
    file.write("\\begin{document}\n\\centering\n\n")
    file.write(TEXtable(table_data) + "\n\n")
    # file.write(TEXimage(image_path) + "\n\n")
    file.write("\\end{document}")
