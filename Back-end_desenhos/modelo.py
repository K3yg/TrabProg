from config import *
app = Flask(__name__) 
caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "desenhos.db") 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Desenho (db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254))
    data_lancamento = db.Column(db.String(254))
    criadores = db.Column(db.String(254))
    episodios = db.Column(db.Integer) 
    def __str__(self):
        return self.nome + ", " + self.data_lancamento + ", " + self.criadores + ", " + str(self.episodios)
        
    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "data_lancamento" : self.data_lancamento,
            "criadores" : self.criadores,
            "episodios" : self.episodios
        }

if __name__ == "__main__":
    db.create_all()
    novo = Desenho (nome = "DBZ", data_lancamento = "25/12/1543", criadores = "Macedo e Paulada", episodios = 544)
    db.session.add(novo)
    db.session.commit()
    print(novo.episodios)
    todos = db.session.query(Desenho).all()
    print(todos)
    for d in todos:
        print(d)
        print(d.json())


