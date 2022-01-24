import json
from pathlib import Path

def save_data_raw(recipe, directory_data_raw):
    """
    2) en otro proceso hacer actualizacion, es decir, si existe el id comparo que todo sea igual
    """

    file_recipe = Path(directory_data_raw / f"{recipe['recipe_id']}.json")

    #if the recipe is already created, don't save again
    if file_recipe.is_file():
        print("existe ya la receta guardada")
    
    #if doesn't exist, create a file and save the dict in json file
    else:
        file_recipe.touch()
        # note that output.json must already exist at this point
        with open(file_recipe, 'w+') as f:
        # this would place the entire output on one line
            json.dump(recipe, f, indent=4)
        print(f"se guardo la receta id: {recipe['recipe_id']}")

def save_recipe(recipe, NAME_FOLDER_DATA_RAW):
    """
    This function is called each time that give a recipe dict, 
    and call the functions that save the file in directory.
    """
    directory_data_raw = Path(str(Path.cwd()) + NAME_FOLDER_DATA_RAW)
    #time.sleep(SLEEP_SEC)

    if directory_data_raw.exists():
        save_data_raw(recipe, directory_data_raw)
        print("existe data_raw folder y guarde receta")
    else:
        directory_data_raw.mkdir()
        save_data_raw(recipe, directory_data_raw)
        print("se creo carpeta data_raw y se guardo receta")
