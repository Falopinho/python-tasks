from classbiblioteca import biblioteca

livro01 = biblioteca("The Clean Coder")
livro02 = biblioteca("The Pragmatic Programmer")
livro03 = biblioteca("Coders at Work")
livro04 = biblioteca("The Psychology of Computer Programming")

print("Olá, aqui é Code Library, e já separei alguns livros para você...")
user = input("A propósito, Qual seu nome? \n")
print(f"Certo {user}, aqui estão os 4 livros que temos:"
'''     

[0] Clean Code (R. Martin)
[1] The Pragmatic Programmer (A. Hunt & D. Thomas)
[2] Coders at Work (P. Seibel)
[3] The Psychology of Computer Programming (G. Weinberg)

''')

choose = int(input("Escolha uma opção: "))
bookList = [livro01, livro02, livro03, livro04]

if choose <= 3:
    print(f"{user} seu livro {bookList[choose].livros} está aqui.")
    print("Volte sempre!")
else:
    print("Esta opção não está incluída em nossos livros.")