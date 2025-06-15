# Atividade 1
class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        if ano_publicacao <= 0:
            raise ValueError("Ano de publicação deve ser maior que 0")
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            raise Exception("Item já está emprestado")
        self.disponivel = False

    def devolver(self):
        if self.disponivel:
            raise Exception("Item já está disponível")
        self.disponivel = True

    def obter_info(self):
        return f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {'Sim' if self.disponivel else 'Não'}"


# Atividade 2
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao):
        super().__init__(titulo, ano_publicacao)
        self.livros = []

    def adicionar_livro(self, livro):
        if not isinstance(livro, ItemBiblioteca):
            raise TypeError("Apenas objetos do tipo ItemBiblioteca podem ser adicionados")
        self.livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        return all(livro.disponivel for livro in self.livros)

    def obter_info(self):
        titulos = ", ".join(livro.titulo for livro in self.livros)
        return f"Coleção: {self.titulo} - Livros: {titulos}"


# Atividade 3
class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, numero_edicao):
        super().__init__(titulo, ano_publicacao)
        if numero_edicao <= 0:
            raise ValueError("Número da edição deve ser maior que 0")
        self.numero_edicao = numero_edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Nova edição deve ser maior que 0")
        self.numero_edicao = nova_edicao

    def revista_antiga(self, dias_max):
        idade_em_dias = (2025 - self.ano_publicacao) * 365
        return idade_em_dias > dias_max

    def obter_info(self):
        base_info = super().obter_info()
        return f"{base_info}, Edição: {self.numero_edicao}"


# Atividade 4
class Biblioteca:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, item):
        if item.titulo in self.itens:
            raise Exception("Item com esse título já existe")
        self.itens[item.titulo] = item

    def emprestar_item(self, titulo):
        if titulo not in self.itens:
            raise Exception("Item não encontrado")
        self.itens[titulo].emprestar()

    def devolver_item(self, titulo):
        if titulo not in self.itens:
            raise Exception("Item não encontrado")
        self.itens[titulo].devolver()

    def obter_info_geral(self):
        return [item.obter_info() for item in self.itens.values()]
