class Pedido():
    def __init__(self, cliente, fechado=False, pizza=[]):
        self.cliente = cliente
        self.fechado = fechado
        self.pizza = pizza
        
    def add_pizza(self, pizza):
        self.pizza.append(pizza)
        print(f"Pizza {pizza.nome} adicionada com sucesso")
    
    def remover_pizza(self, pizza):
        self.pizza.remove(pizza)
        print(f"Pizza {pizza.nome} removida com sucesso")

    def fechar_pedido(self, pizza, cliente):
        self.fechado = True
        print("Detalhes do pedido:")
        print(f"cliente:{cliente.nome} | contato:{cliente.contato} | endereco:{cliente.endereco}")
        print(f"Pizzas do pedido:")
        total=0
        for pizza in self.pizza:
            print(f"Nome: {pizza.nome} |",
                      f"Tamanho: {pizza.tamanho}",
                      f" | Valor: {pizza.valor}")
            total+= pizza.valor
        print(f"Valor total: R${total}")              
                      