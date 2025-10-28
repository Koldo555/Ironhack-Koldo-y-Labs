import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        """
        Constructor de la clase Soldier
        
        Parámetros:
        health (int): Puntos de vida del soldado
        strength (int): Fuerza de ataque del soldado
        """
        self.health = health
        self.strength = strength
    
    def attack(self):
        """
        Método que devuelve la fuerza de ataque del soldado
        
        Returns:
        int: La fuerza del soldado
        """
        return self.strength

    def receiveDamage(self, damage):
        """
        Método que aplica daño al soldado reduciendo su vida
        
        Parámetros:
        damage (int): Cantidad de daño a recibir
        
        Returns:
        None: No devuelve nada (como exige el test)
        """
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        """
        Constructor de la clase Viking que hereda de Soldier
        
        Parámetros:
        name (str): Nombre del vikingo
        health (int): Puntos de vida del vikingo
        strength (int): Fuerza de ataque del vikingo
        """
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        """
        Método que devuelve el grito de guerra del vikingo
        
        Returns:
        str: Grito de guerra exacto que espera el test
        """
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        """
        Método que aplica daño al vikingo y devuelve un mensaje personalizado
        
        Parámetros:
        damage (int): Cantidad de daño a recibir
        
        Returns:
        str: Mensaje indicando el estado del vikingo después del daño
        """
        self.health -= damage
        
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        """
        Constructor de la clase Saxon que hereda de Soldier
        
        Parámetros:
        health (int): Puntos de vida del sajón
        strength (int): Fuerza de ataque del sajón
        """
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """
        Método que aplica daño al sajón y devuelve un mensaje personalizado
        
        Parámetros:
        damage (int): Cantidad de daño a recibir
        
        Returns:
        str: Mensaje indicando el estado del sajón después del daño
        """
        self.health -= damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War():
    def __init__(self):
        """
        Constructor de la clase War
        Inicializa dos ejércitos vacíos
        """
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        """
        Método que añade un vikingo al ejército vikingo
        
        Parámetros:
        viking (Viking): Objeto Viking a añadir al ejército
        
        Returns:
        None: No devuelve nada (como exige el test)
        """
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        """
        Método que añade un sajón al ejército sajón
        
        Parámetros:
        saxon (Saxon): Objeto Saxon a añadir al ejército
        
        Returns:
        None: No devuelve nada (como exige el test)
        """
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        """
        Método que simula el ataque de un vikingo a un sajón
        
        Returns:
        str: Resultado del ataque (mensaje del método receiveDamage del sajón)

        Esta función usa random.choice() que selecciona un elemento al azar
        de una secuencia (lista, tupla, string, etc.) = su parámetro es 1 lista en este caso.
        """
        # Seleccionar un vikingo y un sajón al azar
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        
        # El sajón recibe el daño igual a la fuerza del vikingo
        result = random_saxon.receiveDamage(random_viking.strength)
        
        # Si el sajón murió (health <= 0), lo removemos del ejército
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        
        return result
    
    def saxonAttack(self):
        """
        Método que simula el ataque de un sajón a un vikingo
        
        Returns:
        str: Resultado del ataque (mensaje del método receiveDamage del vikingo)
        """
        # Seleccionar un sajón y un vikingo al azar
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        
        # El vikingo recibe el daño igual a la fuerza del sajón
        result = random_viking.receiveDamage(random_saxon.strength)
        
        # Si el vikingo murió (health <= 0), lo removemos del ejército
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        
        return result

    def showStatus(self):
        """
        Método que muestra el estado actual de la guerra
        
        Returns:
        str: Estado de la guerra basado en el tamaño de los ejércitos
        """
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."