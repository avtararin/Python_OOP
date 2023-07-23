class Character:
    def __init__(self, health, damage, haki, name):
        self.__health = health
        self.damage = damage
        self.haki = haki
        self.name = name
    
    def get_health(self):
        return self.__health
    
    def set_health(self, health):
        self.__health = health
    
    def attack(self, target):
        if self.haki < target.haki:
            print("{} cannot defeat {} cause his haki weaker".format(self.name, target.name))
        else:
            target.receive_damage(self.damage)
        if target.get_health() <= 0:
                print("{} defeated the {}".format(self.name, target.name))
    
    def receive_damage(self, damage):
        self.__health -= damage
    
    def __eq__(self, other):
        return self.__health == other.get_health()


class Marine(Character):
    def __init__(self, health, damage, haki, name, rank):
        super().__init__(health, damage, haki, name)
        self.rank = rank
    def attack(self, target):
        super().attack(target)


class Pirate(Character):
    def __init__(self, health, damage, haki, name, bounty):
        super().__init__(health, damage, haki, name)
        self.bounty = bounty
        self.weapon = None
    
    def set_weapon(self, weapon):
        self.weapon = weapon
    
    def attack(self, target):
        if self.weapon is not None:
            target.receive_damage(self.weapon.damage)
            print("{} attacked {} with sword and caused {} damage".format(self.name, target.name, self.damage))
        else:
            super().attack(target)


class Cipher_pol_0(Character):
    def __init__(self, health, damage, haki, name):
        super().__init__(health, damage, haki, name)
        self.rokusiki = None
    
    def set_rokusiki(self, rokusiki):
        self.rokusiki = rokusiki
        self.damage += 50
    
    def attack(self, target):
        if self.rokusiki is not None and self.haki > target.haki:
            target.receive_damage(self.damage)
            print(self.name, " attacked with", self.rokusiki, "and caused", self.damage, "damage")
        else:
            super().attack(target)


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Singleton(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        
        return cls._instances[cls]


if __name__ == "__main__":
    Garp = Marine(300, 80, 1000,"Garp", "Vice-admiral")
    Luffy = Pirate(400, 100, 1500, "Luffy", 3000000000)
    Lucci = Cipher_pol_0(250, 15, 500,  "Rob Lucci")
    
    sword = Weapon("Sword", 10)
    Luffy.set_weapon(sword)
    
    Lucci.set_rokusiki("Tekkay")
    
    Garp.attack(Luffy)
    Luffy.attack(Lucci)
    Lucci.attack(Garp)