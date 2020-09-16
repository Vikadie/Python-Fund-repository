class Weapon:

    def __init__(self, bullets: int):
        self.bullets = int(bullets)

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"

    def shoot(self):
        if self.bullets > 0:
            self.bullets -= 1
            return "shooting..."
        else:
            return "no bullets left"


weapon = Weapon(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)