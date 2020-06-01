from repository import Repository


class PersonService:

    def get_personList(self):
        return Repository.person

    # Agrega una persona en el dicionario person, definido en Repository
    def add_person(self, person):
        print("Agregando...")
        key = len(Repository.person)
        Repository.person[key] = (person._name, person._surname,
                                  person._age)

    # Actualiza datos de una person del diccionario person
    # key clave diccionario
    # object Person
    def update_person(self, key, person):
        print("Modificando...")
        key = len(Repository.person)
        key = 0
        Repository.person[key] = (person._name, person._surname,
                                  person._age)

    # Elimina persona segun key del dic person
    def delete_person(self, key):
        print("Eliminando...")
        key = 0
        del Repository.person[key]
