from models.contact import Contact


# Exemplo de uso
if __name__ == "__main__":
    # Criando contatos
    contact1 = Contact(1, "Ana Silva", "11999998888", "ana@exemplo.com")
    contact2 = Contact(2, "Carlos Oliveira", "21988887777", "carlos@exemplo.com", True)

    # Usando os métodos
    contact1.print_contact()
    
    print("\nAntes de alterar:")
    print(contact1.get_contact())

    # Modificando dados
    contact1.set_name("Ana Clara Silva")
    contact1.set_cellfone("11999997777")
    contact1.toggle_favorite()

    print("\nDepois de alterar:")
    contact1.print_contact()

    # Acessando propriedades
    print(f"\nE-mail do Carlos: {contact2.get_email()}")
    print(f"É favorito? {'Sim' if contact2.is_favorite() else 'Não'}")