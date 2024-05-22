from database import db

class Patients(db.Model):
    __tablename__ = "patient"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    ci = db.Column(db.String(10), nullable=False)
    birth_date= db.Column(db.String(25), nullable=False)
    
    def __init__(self, name, last_name, ci,birth_date):
        self.name = name
        self.last_name=last_name
        self.ci=ci
        self.birth_date=birth_date
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get_all():
        return Patients.query.all()

    
    @staticmethod
    def get_by_id(id):
        return Patients.query.get(id)

    
    def update(self, name=None, last_name=None, ci=None, birth_date=None):
        if name is not None:
            self.name = name
        if last_name is not None:
            self.last_name=last_name
        if ci is not None:
            self.ci=ci
        if birth_date is not None:
            self.birth_date=birth_date
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()