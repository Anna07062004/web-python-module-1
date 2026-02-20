players = {}

def add_player(name, height):
    if name in players:
        print(f"Игрок {name} уже есть в базе.")
    else:
        players[name] = height
        print(f"Добавлен игрок: {name} с ростом {height} см.")

def delete_player(name):
    if name in players:
        del players[name]
        print(f"Игрок {name} удален.")
    else:
        print(f"Игрок {name} не найден.")

def find_player(name):
    if name in players:
        print(f"{name}: рост {players[name]} см.")
    else:
        print(f"Игрок {name} не найден.")

def replace_player(name, new_height):
    if name in players:
        players[name] = new_height
        print(f"Рост игрока {name} изменен на {new_height} см.")
    else:
        print(f"Игрок {name} не найден.")

add_player("Мэджик Джонсон", 206)
add_player("Майкл Джордан", 198)
find_player("Майкл Джордан")
replace_player("Майкл Джордан", 200)
find_player("Майкл Джордан")
delete_player("Мэджик Джонсон")