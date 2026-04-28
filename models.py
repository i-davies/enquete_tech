from database import db

class TecnologiaModel(db.Model):
    __tablename__ = "tecnologia" # nome real da tabela no banco

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique=True, nullable=False)
    votos = db.Column(db.Integer, default=0)

    def to_dict(self):
        """Converte o registro do banco para dicionário Python"""
        return {
            "nome" : self.nome,
            "votos": self.votos
        }