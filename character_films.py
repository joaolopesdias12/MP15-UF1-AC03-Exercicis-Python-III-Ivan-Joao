from character import character

class character_film(character):
    def __init__(self, character, num_of_films, first_film, alive_at_the_end):
        super().__init__(character._edited,character._name,character._created,character._gender,character._skin_color,character._hair_color,character.
                 _height,character._eye_color,character._mass,character._homeworld,character._birth_year)
        
        self._num_of_films = num_of_films
        self._first_film = first_film
        self._alive_at_the_end = alive_at_the_end
    
    def __str__(self) -> str:
        return f"{self.name}, {self.alive_at_the_end}, {self.first_film}, {self.num_of_films}"

    @property
    def num_of_films(self):
        return self._num_of_films
    
    @num_of_films.setter
    def num_of_films(self, num_of_film):
        self._num_of_films = num_of_film
    
    @property
    def first_film(self):
        return self._first_film
    
    @first_film.setter
    def first_film(self, first_film):
        self._first_film = first_film

    @property
    def alive_at_the_end(self):
        return self._alive_at_the_end
    
    @alive_at_the_end.setter
    def alive_at_the_end(self, alive_at_the_end):
        self._alive_at_the_end = alive_at_the_end

    def secondary(self,edited,name,created,gender,skin_color,hair_color,
                 height,eye_color,mass,homeworld, birth_year, num_of_films, first_film, alive_at_the_end):
        c= character(edited,name,created,gender,skin_color,hair_color,
                 height,eye_color,mass,homeworld, birth_year)
        cf = character_film(c, num_of_films, first_film, alive_at_the_end)
        cf.num_of_films = num_of_films
        cf.first_film = first_film
        cf.alive_at_the_end = alive_at_the_end
        return cf
    
    def toDict(self):
        c_dict = super().toDict()
        c_dict[self.name]["num_of_films"] = self.num_of_films
        c_dict[self.name]["first_film"] = self.first_film
        c_dict[self.name]["alive_at_the_end"] = self.alive_at_the_end
        return c_dict
