import xml.etree.ElementTree as ET

def criar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    contato = ET.Element("contato")
    nome_element = ET.SubElement(contato, "nome")
    nome_element.text = nome
    telefone_element = ET.SubElement(contato, "telefone")
    telefone_element.text = telefone
    email_element = ET.SubElement(contato, "email")
    email_element.text = email

    return contato

def salvar_contatos(contatos):
    root = ET.Element("contatos")
    for contato in contatos:
        root.append(contato)

    tree = ET.ElementTree(root)
    tree.write("contatos.xml")

def main():
    contatos = []
    while True:
        opcao = input("1 - Adicionar contato\n2 - Sair\nEscolha uma opção: ")
        if opcao == "1":
            contato = criar_contato()
            contatos.append(contato)
            print("Contato adicionado com sucesso!\n")
        elif opcao == "2":
            salvar_contatos(contatos)
            print("Contatos salvos em contatos.xml")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
