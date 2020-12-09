from config import *
from modelo import Desenho, Genero, Personagem 
from flask_cors import CORS
app = Flask(__name__) 
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__))    
arquivobd = os.path.join(caminho, "desenhos.db") 
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+arquivobd 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
db = SQLAlchemy(app)

@app.route("/")
def padrao():
    return "Salve"

@app.route("/listar_desenhos")
def listar_desenhos():
    desenhos = db.session.query(Desenho).all()
    retorno = [ d.json() for d in desenhos ]
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta
    
def listar_personagens():
    personagens = db.session.query(Personagem).all()
    retorno = [ d.json() for d in personagens ]
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

@app.route("/listar_generos")
def listar_generos():
    generos = db.session.query(Genero).all()
    retorno = [ d.json() for d in generos ]
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

@app.route("/listar_personagens")
def listar_personagens():
    personagens = db.session.query(Personagem).all()
    retorno = [ d.json() for d in personagens ]
    resposta = jsonify(retorno)
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

@app.route('/incluir_desenho', methods=['post'])
def incluir_desenho():
    resposta = jsonify({"resultado": "bele", "detalhes": "supimpa, vc conseguiu"})
    dados = request.get_json(force=True)
    try:
        novo_desenho = Desenho(**dados)
        db.session.add(novo_desenho)
        db.session.commit()
    except Exception as e: 
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)}) 
    resposta.headers.add("Access-Control-Allow-Origin", "*") 
    return resposta

@app.route("/excluir_desenho/<int:desenho_id>", methods=['DELETE'])
def remover_paciente(desenho_id):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    try:
        Desenho.query.filter(Desenho.id == desenho_id).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta


app.run(debug=True)

