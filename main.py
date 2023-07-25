from character import Character, Marine, Pirate, Cipher_pol_0, Weapon

garp = Marine(300, 80, 1000,"Garp", "Vice-admiral")
luffy = Pirate(400, 100, 1500, "Luffy", 3000000000)
lucci = Cipher_pol_0(250, 15, 500,  "Rob Lucci")

    
lucci.set_rokusiki("Tekkay")
    
garp.attack(luffy)
luffy.attack(lucci)
lucci.attack(garp)
luffy.attack(lucci)
luffy.attack(lucci)
luffy.attack(lucci)
