---

# Object-Relational Mapping in Python

This directory contains Python scripts that demonstrate Object-Relational Mapping (ORM) concepts using MySQL databases.

## Table of Contents

1. [Description](#description)
2. [Scripts](#scripts)
3. [Usage](#usage)
4. [Dependencies](#dependencies)
5. [Author](#author)

## Description

Object-Relational Mapping (ORM) is a programming technique for converting data between incompatible type systems in object-oriented programming languages and relational databases. In this project, we explore ORM concepts using Python and MySQL databases.

## Scripts

1. `0-select_states.py`: A script that lists all states from the database.
2. `1-filter_states.py`: A script that lists states starting with a specific letter.
3. `2-my_filter_states.py`: A script that takes an argument and displays all values in the states table of a database where the name matches the argument.
4. `3-my_safe_filter_states.py`: A script that is safe from MySQL injection.
5. `4-cities_by_state.py`: A script that lists all cities from the database.
6. `5-filter_cities.py`: A script that takes the state name as an argument and lists all cities of that state.
7. `model_state.py`: A Python file that contains the definition of a State class.
8. `7-model_state_fetch_all.py`: A script that lists all State objects from the database.
9. `8-model_state_fetch_first.py`: A script that prints the first State object from the database.
10. `9-model_state_filter_a.py`: A script that lists all State objects that contain the letter 'a'.
11. `10-model_state_my_get.py`: A script that prints the State object with the name passed as an argument.
12. `11-model_state_insert.py`: A script that adds the State object 'Louisiana' to the database.
13. `12-model_state_update_id_2.py`: A script that changes the name of a State object from the database.
14. `13-model_state_delete_a.py`: A script that deletes all State objects with a name containing the letter 'a'.
15. `relationship_city.py`: A Python file that contains the definition of a City class.
16. `relationship_state.py`: A Python file that contains the definition of a State class with a relationship to City.

## Usage

To run any of the scripts in this directory, you can use the following command:

```bash
python3 <script_name>.py
```


## Dependencies

- Python 3.x
- MySQL database
- MySQLdb module

## Author

- [Sholy cul](https://github.com/Sholycul)

---

