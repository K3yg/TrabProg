from config import *
app = Flask(__name__) 
caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "desenhos.db") 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Genero(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(254))
    historia = db.Column(db.String(254))
    popularidade = db.Column(db.Integer)
    def __str__(self):
        return self.tipo +  ", " + self.historia + ", " + str(self.popularidade)
    
    def json(self):
        return{
            "id" : self.id,
            "tipo" : self.tipo,
            "historia" : self.historia,
            "popularidade" : self.popularidade
        }

class Desenho(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    nome = db.Column(db.String(254))
    data_lancamento = db.Column(db.String(254))
    criadores = db.Column(db.String(254))
    episodios = db.Column(db.Integer)
    genero_id = db.Column(db.Integer, db.ForeignKey(Genero.id), nullable = False)
    genero = db.relationship("Genero")
    def __str__(self):
        return self.nome + ", " + self.data_lancamento + ", " + self.criadores + ", " + str(self.episodios)
        
    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "data_lancamento" : self.data_lancamento,
            "criadores" : self.criadores,
            "episodios" : self.episodios,
            "genero_id" : self.genero_id,
            "genero" : self.genero.json()
        }

class Personagem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    altura = db.Column(db.Float)
    descricao = db.Column(db.String(254))
    desenho_id = db.Column(db.Integer, db.ForeignKey(Desenho.id), nullable = False)
    desenho = db.relationship("Desenho")
    def __str__(self):
        return self.nome + ", " + str(self.altura) + ", " + self.descricao

    def json(self):
        return{
            "id" : self.id,
            "nome" : self.nome,
            "altura" : self.altura,
            "descricao" : self.descricao,
            "desenho_id" : self.desenho_id,
            "desenho" : self.desenho.json()
        }



if __name__ == "__main__":
    db.create_all()
 
    genero1 = Genero(tipo = "Ação", historia = "Historia triste e comovente" , popularidade = 10)
    db.session.add(genero1)
    db.session.commit()
    print(genero1)
    
    desenho1 = Desenho (nome = "DBZ", data_lancamento = "25/12/1543", criadores = "Macedo e Paulada", episodios = 544, genero = genero1)
    db.session.add(desenho1)
    db.session.commit()
    print(desenho1)
    
    personagem1 = Personagem(nome = "Cleiton", altura = "1.46", descricao = "muito forte", desenho = desenho1)
    db.session.add(personagem1)
    db.session.commit()
    print(personagem1)

   
    """
    novo = Desenho (nome = "DBZ", data_lancamento = "25/12/1543", criadores = "Macedo e Paulada", episodios = 544)
    db.session.add(novo)
    db.session.commit()
    print(novo.episodios)
    todos = db.session.query(Desenho).all()
    print(todos)
    for d in todos:
        print(d)
        print(d.json())


"""