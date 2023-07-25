from exceptions import KillingDeadError, LowHakiError
#Character classes with child classes - Marine, Pirate, Cipher_pol_0

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
        try:
            self.target_alive(target)
            self.haki_comprahasion(target)
            if self.haki < target.haki:
                print("{} cannot defeat {} cause his haki weaker".format(self.name, target.name))
            else:
                target.receive_damage(self.damage)
            if target.get_health() <= 0:
                print("{} defeated the {}".format(self.name, target.name))
        except KillingDeadError:
            print("You cannot attack dead targets!")
        except LowHakiError:
            print("{}'s haki more powerful then yours you cannot attack".format(target.name))
    def receive_damage(self, damage):
        self.__health -= damage
    
    def __eq__(self, other):
        return self.get_health == other.get_health()
    def target_alive(self, target):
        if target.get_health() <= 0:
            raise KillingDeadError("{} is dead, you cannot attack dead".format(target.name))
    def haki_comprahasion(self, target):
        if target.haki > self.haki:
            raise LowHakiError("{}'s haki more powerful then yours you cannot attack".format(target.name))


class Marine(Character):
    def __init__(self, health, damage, haki, name, rank):
        super().__init__(health, damage, haki, name)
        self.rank = rank


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