import pizza
import cliente
import pedido

pi = pizza.Pizza("calabresa", "M", 40)
pi2 = pizza.Pizza("Portuguesa", "M", 45)
prof = cliente.Cliente("Marcos", 40028922, "IFB")

pedido = pedido.Pedido(prof)

pedido.add_pizza(pi)
#pedido.remover_pizza(pi)
pedido.add_pizza(pi2)
pedido.fechar_pedido(pi, prof)

    