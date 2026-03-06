import random
import time
vida = 50
print("\033[92mTU VIDA ES DE:\033[0m" +str(vida))

while True:
    time.sleep(1)
    daño = random.randint(5, 15)
    vida = vida - daño

time.sleep(1)
print("\033[91mEL JEFE GOBLIN TE HA QUITADO:\033(0M" , daño, "HP")
print("\033[92mTU VIDA ES DE:\033/(0m" ,vida)

if vida <= 0:
    print("\033[91mHAS SIDO ELIMINADO POR EL GRAN JEFE DE LA ALDEA DE LOS GOBLINS\033(0m")



