class Detalhes:
    def __init__(self, id, titulo, resumo, reporter_responsavel):
        self.id = id
        self.titulo = titulo
        self.resumo = resumo
        self.reporter_responsavel = reporter_responsavel

    def get_id(self):
        return self.id
    
    def get_titulo(self):
        return self.titulo
    
    def get_resumo(self):
        return self.resumo
    
    def get_reporter_responsavel(self):
        return self.reporter_responsavel