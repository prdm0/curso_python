s = "qualquer1234"

tabela = s.maketrans("1234", "@@@@")

s.translate(tabela)