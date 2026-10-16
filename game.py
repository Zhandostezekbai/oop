class Player:
    def __init__(self, name: str, health: int):
        # Private variables (prefixed with '_') to protect them from direct access
        self._name = name
        self._health = health

    # --- NAME GETTER & SETTER ---
    @property
    def name(self) -> str:
        """Getter for player name."""
        return self._name

    @name.setter
    def name(self, value: str):
        """Setter for player name with basic validation."""
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    # --- HEALTH GETTER & SETTER ---
    @property
    def health(self) -> int:
        """Getter for player health."""
        return self._health

    @health.setter
    def health(self, value: int):
        """Setter for player health (prevents health from dropping below 0)."""
        self._health = max(0, value)


class Wizard(Player):
    def __init__(self, name: str, health: int, mana: int):
        # super().__init__() passes name and health to the Player class constructor
        super().__init__(name, health)
        self._mana = mana

    # --- MANA GETTER & SETTER ---
    @property
    def mana(self) -> int:
        return self._mana

    @mana.setter
    def mana(self, value: int):
        if value < 0:
            raise ValueError("Mana cannot be negative.")
        self._mana = value

    def cast_spell(self):
        print(f"Wizard {self.name} is casting a spell!")


class Warrior(Player):
    def __init__(self, name: str, health: int, armor: int):
        # super().__init__() passes name and health to the Player class constructor
        super().__init__(name, health)
        self._armor = armor

    # --- ARMOR GETTER & SETTER ---
    @property
    def armor(self) -> int:
        return self._armor

    @armor.setter
    def armor(self, value: int):
        if value < 0:
            raise ValueError("Armor cannot be negative.")
        self._armor = value

    def shield_bash(self):
        print(f"Warrior {self.name} is performing a shield bash!")


# ==========================================
# TESTING THE CODE
# ==========================================
if __name__ == "__main__":
    # Create instances of subclasses
    gandalf = Wizard(name="Gandalf", health=100, mana=150)
    conan = Warrior(name="Conan", health=200, armor=50)

    # 1. Accessing fields via Getters (inherited and subclass-specific)
    print(f"Character: {gandalf.name} | HP: {gandalf.health} | Mana: {gandalf.mana}")
    print(f"Character: {conan.name} | HP: {conan.health} | Armor: {conan.armor}")

    # 2. Modifying fields via Setters
    gandalf.health -= 30  # Uses Player health setter
    gandalf.mana = 120    # Uses Wizard mana setter
    
    conan.name = "Conan the Destroyer"  # Uses Player name setter
    conan.armor = 65                    # Uses Warrior armor setter

    print("\n--- After updates ---")
    print(f"Updated Wizard: {gandalf.name} | HP: {gandalf.health} | Mana: {gandalf.mana}")
    print(f"Updated Warrior: {conan.name} | HP: {conan.health} | Armor: {conan.armor}")
