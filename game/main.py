from enemy import Enemy, Troll, Vampire

ugly_troll = Troll("Grah")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

# monster = Enemy("Basic enemy")
# monster.grunt() .grunt() jest funkcją opisaną dla Troll nie dla Enemy. Klasa nadrzędna nie może korzystać zklasy podrzędnej.

brother.take_damage(5)
print(brother)

vampire1 = Vampire("Vlad")
print(vampire1)
vampire1.take_damage(13)
print(vampire1)

print("-" * 40)
another_troll.take_damage(30)
print(another_troll)

# while vampire1.alive:
#     vampire1.take_damage(1)
#     print(vampire1)

vampire1.lives = 0
vampire1.hit_points = 1
print(vampire1)
