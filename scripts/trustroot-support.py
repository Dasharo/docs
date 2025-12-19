#!/bin/bash
import sys, os, json

if len(sys.argv) < 2:
    exit(1)
repo = sys.argv[1]
configs = os.path.join(repo, "configs")

def has_eom(model):
    return "eom_path_comm_cap" in model

eom_models = list()

for file in os.listdir(configs):
    with open(os.path.join(configs, file), "r") as file:
        conf = json.load(file)
        models = conf["models"]

        eom_models.extend([(m, models[m]) for m in models if has_eom(models[m])])

        complex_models = [m for m in models if "board_models" in models[m]]
        for model in complex_models:
            submodels = models[model]["board_models"]
            eom_submodels = [(m, submodels[m]) for m in submodels if has_eom(submodels[m])]
            eom_models.extend(eom_submodels)

if "--pretty" in sys.argv:
    print('| Manufacturer |     Device      |')
    for m in eom_models:
        print(f'| {m[1]["dasharo_rel_name"].split("_")[0]} | {m[0]} |')
else:
    for m in eom_models:
        print(m)
