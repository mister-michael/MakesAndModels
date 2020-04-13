# ------------------------------------
# Practice Showroom and Junkyard     |
# ------------------------------------

# showroom = {"Lesabre", "F-150", "Avalanche", "Prius"}

# print(len(showroom))

# showroom.add("F-150")

# twomore = {"Civic", "Impala"}

# showroom.update(twomore)

# showroom.discard("Avalanche")

# junkyard = {"car1", "car2", "car3", "car4", "Prius", "Civic"}

# cars_intersection = showroom.intersection(junkyard)

# print("cars_intersection =", cars_intersection)

# showroom = showroom.union(junkyard)

# print("showroom =", showroom)

# showroom.discard("car4")

# print("new showroom =", showroom)

# -------------------------------
# Matching Makes and Models     |
# -------------------------------

makes = (
    (1, "Toyota"), (2, "Nissan"),
    (3, "Ford"), (4, "Mini"),
    (5, "Honda"), (6, "Dodge"),
)

models = (
    (1, "Altima", 2), (2, "Thunderbird", 3),
    (3, "Dart", 6), (4, "Accord", 5),
    (5, "Prius", 1), (6, "Countryman", 4),
    (7, "Camry", 1), (8, "F150", 3),
    (9, "Civic", 5), (10, "Ram", 6),
    (11, "Cooper", 4), (12, "Pilot", 5),
    (13, "Xterra", 2), (14, "Sentra", 2),
    (15, "Charger", 6)
)

colors = (
    (1, "Black"), (2, "Charcoal"), (3, "Red"), (4, "Brick"),
    (5, "Blue"), (6, "Navy"), (7, "White"), (8, "Ivory")
)

available_car_colors = (
    (1, 1), (1, 2), (1, 7),
    (2, 1), (2, 3), (2, 7),
    (3, 2), (3, 3), (3, 7),
    (4, 3), (4, 5), (4, 8),
    (5, 2), (5, 4), (5, 8),
    (6, 2), (6, 6), (6, 7),
    (7, 1), (7, 3), (7, 7),
    (8, 1), (8, 5), (8, 8),
    (9, 1), (9, 6), (9, 7),
    (10, 2), (10, 5), (10, 7),
    (11, 3), (11, 6), (11, 8),
    (12, 1), (12, 4), (12, 7),
    (13, 2), (13, 6), (13, 8),
    (14, 2), (14, 5), (14, 8),
    (15, 1), (15, 4), (15, 7)
)


cardict = {}
#for each available car in the yard, (model, color) (int, int)
for available_car in available_car_colors:
    # print(available_car) 
    availcar = available_car[0]
    availcolor = available_car[1]
    modelName = ""
    colorName = ""
    makeName = ""
    
    #match color get name
    for color in colors:
        if color[0] == availcolor:
            colorName = color[1]
    # print(colorName)
    # #match model and make
    for model in models:
        if model[0] == availcar:
            # modelinloop = model[0]
            modelName = model[1]
            model_make = model[2]
    for make in makes:
        if make[0] == model_make:
            makeName = make[1]
    # print(modelName, colorName, makeName)
    if makeName in cardict.keys():
        if modelName in cardict[makeName]:
            cardict[makeName][modelName].append(colorName)
        else:
            cardict[makeName][modelName] = [colorName]
    else:
        cardict[makeName] = {modelName: [colorName]}


for key, value in cardict.items():
    print(key)
    print("------------")
    for key, value in value.items():
        color = ", ".join(value)
        # print(color)
        print(f"{key} available in: {color}")
        print("")
    print("")
    

    
    


# advanced solve
# report = {
#     make.upper(): {
#         model: [
#             color.lower()
#             for model_id, color_id in available_car_colors
#             if model_id == model_index
#             for color_index, color in colors
#             if color_index == color_id
#         ]
#         for model_index, model, make_id in models
#         if make_index == make_id
#     }
#     for make_index, make in makes
# }
# # vvv \n is what you do when you go to next line i.e ‘Enter Key’ vvv
# output_report = "\n\n\n".join(
#     f"\n{make}\n-------------------------------"
#     + "\n\n".join(
#         [
#             f"{model}: is available in " + ", ".join(colors)
#             for model, colors in makeDetails.items()
#         ]
#     )
#     for make, makeDetails in report.items()
# )
# print(output_report)

# --------------------------------------------------------

# katie's solve

# cars = set()
# colorSet = set()
# makeSet = set()
# modelSet = set()

# for avail in available_car_colors:
#     for model in models:
#         for color in colors:
#             if avail[0] == model[0] & avail[1] == color[0]:
#                 colorSet.add(color[1])
#                 modelSet.add(model[2])
#                 for make in makes:
#                     if make[0] == model[0]:
#                         makeSet.add(make[1])
# print(colorSet)

