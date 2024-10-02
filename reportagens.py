class Reportagem:
    def __init__(self, id, nome, reporternome,categoria,resumo):
        self.id = id
        self.resumo = resumo
        self.nome= nome
        self.reporternome = reporternome
        self.categoria = categoria

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_reporternome(self):
        return self.reporternome
    
    def get_categoria(self):
        return self.categoria
    
    def get_resumo(self):
        return self.resumo