import shutil
from pathlib import Path

# directorio = 'val'
# directorio = 'train'
directorio = 'test'

fruits_and_products = [
    'Golden-Delicious',
    'Granny-Smith',
    'Pink-Lady',
    'Royal-Gala',
    'Avocado',
    'Banana',
    'Kiwi',
    'Lemon',
    'Lime',
    'Mango',
    'Cantaloupe',
    'Galia-Melon',
    'Honeydew-Melon',
    'Watermelon',
    'Orange',
    'Passion-Fruit',
    'Peach',
    'Conference',
    'Pineapple',
    'Pomegranate',
    'Red-Grapefruit',
    'Satsumas',
    'Bravo-Apple-Juice',
    'Bravo-Orange-Juice',
    'God-Morgon-Apple-Juice',
    'God-Morgon-Orange-Juice',
    'God-Morgon-Orange-Red-Grapefruit-Juice',
    'God-Morgon-Red-Grapefruit-Juice',
    'Arla-Ecological-Medium-Fat-Milk',
    'Arla-Medium-Fat-Milk',
    'Arla-Standard-Milk',
    'Garant-Ecological-Medium-Fat-Milk',
    'Garant-Ecological-Standard-Milk',
    'Oatly-Oat-Milk',
    'Oatly-Natural-Oatghurt',
    'Arla-Sour-Cream',
    'Alpro-Blueberry-Soyghurt',
    'Alpro-Vanilla-Soyghurt',
    'Arla-Mild-Vanilla-Yoghurt',
    'Valio-Vanilla-Yoghurt',
    'Yoggi-Strawberry-Yoghurt',
    'Yoggi-Vanilla-Yoghurt',
    'Asparagus',
    'Aubergine',
    'Brown-Cap-Mushroom',
    'Cabbage',
    'Carrots',
    'Cucumber',
    'Ginger',
    'Leek',
    'Yellow-Onion',
    'Orange-Bell-Pepper',
    'Red-Bell-Pepper',
    'Yellow-Bell-Pepper',
    'Floury-Potato',
    'Sweet-Potato',
    'Red-Beet',
    'Beef-Tomato',
    'Vine-Tomato',
    'Zucchini'
]

def copy_folder(src, dest):
    src_path = Path(src)
    dest_path = Path(dest)

    try:
        shutil.copytree(src_path, dest_path)
        print(f"Carpeta '{src}' copiada exitosamente a '{dest}'")
    except Exception as e:
        print(f"Error al copiar la carpeta: {e}")

def get_folder_names(path):
    # Convertir la ruta en un objeto Path
    path = Path(path)

    # Obtener solo los nombres de los directorios dentro de la ruta dada
    for item in path.iterdir():
        if item.is_dir():
            if item.name in fruits_and_products:
                print(item.absolute())
                src = item.absolute()
                dest = r'C:\Users\lperd\OneDrive - Universidad de los andes\MINE 2024-2\CIENCIA DE DATOS APLICADA\Talleres\Taller 2\GroceryStoreDataset\new_dataset\{}\{}'.format(directorio, item.name)
                copy_folder(src, dest)
            if not any(item.iterdir()):
                pass
            else:
                get_folder_names(item)

# Ejemplo de uso
path = r'C:\Users\lperd\OneDrive - Universidad de los andes\MINE 2024-2\CIENCIA DE DATOS APLICADA\Talleres\Taller 2\GroceryStoreDataset\dataset\{}'.format(directorio)


get_folder_names(path)