class Game:
    def __init__(self, players):
        self.players = players
        self.is_day = True
        self.dead_players = []
        self.num_living = len(players)

    def turn_night(self):
        self.is_day = False

    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Mafioso" or killer.role.__class__.__name__ == "Godfather":
                message = f"{target.name} was killed by the mafia."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Veteran":
                message = f"{target.name} was killed by the Veteran."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Vigilante":
                message = f"{target.name} was shot by a Vigilante."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Vampire Hunter":
                message = f"{target.name} was staked by Vampire Hunter."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Arsonist":
                message = f"{target.name} was incinerated by an Arsonist."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Werewolf":
                message = f"{target.name} was mauled by the Werewolf."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Jester":
                message = f"{target.name} was haunted by the Jester."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Bodyguard":
                message = f"{target.name} was killed by a Bodyguard."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Vampire":
                message = f"{target.name} was bitten by a Vampire."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Veteran":
                message = f"{target.name} was stabbed by a Serial Killer."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Jailor":
                message = f"{target.name} was executed by the Jailor."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."
                    
    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Serial Killer":
                message = f"{target.name} was stabbed by a Serial Killer."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."

    def kill(self, target, killer):
        if target.role.defense < killer.role.attack:
            if killer.role.__class__.__name__ == "Ambusher":
                message = f"{target.name} was ambushed."
                recipient = "everyone"
                self.dead_players.append(target)
                del self.players[self.players.index(target)]
            for elem in self.players:
                if elem[2].role.__class__.__name__ == "Janitor" and elem[2].role.is_clean is True and elem[2].role.target is target:
                    message = f"{target.name} was cleaned."

        else:
            message = "Your target's defense is too high."
            recipient = killer
        return [message, recipient]

class Player:
    def __init__(self, name, role, number):
        self.name = name
