
from Toy import Toy
from ToyShop import ToyShop


shop = ToyShop()
shop.add_toy(Toy(1, "Мяч", 5, 30))
shop.add_toy(Toy(2, "Кукла", 5, 30))
shop.add_toy(Toy(3, "Машинка", 5, 40))


print(shop)
shop.play()
print(shop)
