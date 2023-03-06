nome = "Matue"

# Escopo Global
if 'nome' in globals():
    print("a variável está no escopo global!")

if 'idade' in globals():
    print("a variável idade está no escopo global!")
# Escopo local
if 'nome' in locals():
    print("a variável está no escopo local!")

if 'idade' in locals():
    print("a variável idade está no escopo local!")

def teste():
    idade = 18

if 'idade' in locals():
    print("a variável idade está no escopo local!")

if 'nome' in globals():
    print("a variável está no escopo global!")

teste()