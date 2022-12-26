from dao.model.director import Director

class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, director_d):
        d_create = Director(**director_d)
        self.session.add(d_create)
        self.session.commit()
        return d_create

    def update(self, director_d):
        director = self.get_one(director_d.get('id'))
        director.name = director_d.get('name')

        self.session.add(director)
        self.session.commit()

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()
