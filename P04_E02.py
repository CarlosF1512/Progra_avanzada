#Implemente una clase Playlist que tenga una lista de sus canciones favoritas. 
class Playlist():
    def __init__(self,canciones):
        self.canciones = canciones

# Use el método __len__ para devolver el número de canciones
    def __len__(self):
        return len(self.canciones)

# Utilice el método __getitem__ para devolver una canción de la lista
    def __getitem__(self,llave):
        return self.canciones[llave]

# Utilice __setitem__ para establecer una nueva cancion
    def __setitem__(self,llave,valor):
        if llave < len(self.canciones):
            self.canciones[llave] = valor
        elif llave == len(self.canciones):
            self.canciones.append(valor)


Playlist1 = Playlist(["unendlichkeit - CRO", "Circles - Post Malone", "Sanctuary - Joji"])
print(f'Número de canciones en Playlist:', len(Playlist1))
print(Playlist1[2])
Playlist1[3] = 'Nights - Frank Ocean'
print(f'Número de canciones en Playlist:', len(Playlist1))
print(Playlist1[3])