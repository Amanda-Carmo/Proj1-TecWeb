import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database(object): 
    def __init__(self, banco):   
        self.conn = sqlite3.connect(banco+'.db')
        #Creating a cursor object using the cu'rsor() method      
        self.conexao = self.conn.cursor()  

        command1 = 'CREATE TABLE IF NOT EXISTS note(id INTEGER PRIMARY KEY, title TEXT, content TEXT NOT NULL);'
        # command1 = 'CREATE TABLE IF NOT EXISTS dados_pessoais (nome_da_rua TEXT NOT NULL, cpf TEXT NOT NULL UNIQUE, identificador INTEGER PRIMARY KEY);'

        self.conexao.execute(command1)

    def add(self, note):
        data_insert = "INSERT INTO note(title, content) VALUES ('{}', '{}');".format(note.title, note.content)
        self.conexao.execute(data_insert)
        self.conn.commit()

    def get_all(self):
        cursor = self.conexao.execute("SELECT id, title, content FROM note")
        lista_note = []
        for linha in cursor:
            ident = linha[0]
            title = linha[1]
            content = linha[2]

            lista_note.append(Note(linha[0], linha[1], linha[2]))  

        return lista_note

    def update(self, entry):
        self.conexao.execute("UPDATE note SET title = '{}' WHERE id = '{}'".format(entry.title, entry.id))
        self.conexao.execute("UPDATE note SET content = '{}' WHERE id = '{}'".format(entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conexao.execute("DELETE FROM note WHERE id = '{}'".format(note_id))
        self.conn.commit()
    






