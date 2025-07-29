class Contact:
    def __init__(self, id, name, cellfone, email, favority=False):
        self.id = id
        self.name = name
        self.cellfone = cellfone
        self.email = email
        self.favority = favority

    def get_contact(self):
        """Retorna os dados do contato como dicionário"""
        return {
            "id": self.id,
            "name": self.name,
            "cellfone": self.cellfone,
            "email": self.email,
            "favority": self.favority
        }

    def print_contact(self):
        """Exibe os dados do contato formatados"""
        print(f"\nID: {self.id}")
        print(f"Nome: {self.name}")
        print(f"Celular: {self.cellfone}")
        print(f"E-mail: {self.email}")
        print(f"Favorito: {'Sim' if self.favority else 'Não'}")

    # Getters
    def get_name(self):
        return self.name

    def get_cellfone(self):
        return self.cellfone

    def get_email(self):
        return self.email

    def is_favorite(self):
        return self.favority

    # Setters
    def set_name(self, name):
        self.name = name

    def set_cellfone(self, cellfone):
        self.cellfone = cellfone

    def set_email(self, email):
        self.email = email

    def toggle_favorite(self):
        """Alterna o status de favorito"""
        self.favority = not self.favority
        return self.favority