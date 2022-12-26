from dao.model.genre import Genre

class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        return self.session.query(Genre).get(gid)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, genre_d):
        g_create = Genre(**genre_d)
        self.session.add(g_create)
        self.session.commit()
        return g_create

    def update(self, genre_d):
        genre = self.get_one(genre_d.get('id'))
        genre.name = genre_d.get('name')

        self.session.add(genre)
        self.session.commit()

    def delete(self, gid):
        genre = self.get_one(gid)
        self.session.delete(genre)
        self.session.commit()
