from tex_generator import TEXdocument

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

with open("artifacts/hw2_2.tex", "w") as file:
    doc = TEXdocument(table_data, image_path)
    file.write(doc)
