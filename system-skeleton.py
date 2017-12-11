from random import randint


class Referee:
	def __init__(self, red_team=(battler_red1), blue_team=(battler_blue1)):
		pass


class Battler:
	def __init__(self, species=species_snorlax, level=50, gender=randint(0, 8), ability=randint(0,9), nature=randint(0, 24), ivs=(randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31), randint(0, 31)), evs=(0,0,0,0,0,0), moveset=(move_tackle, move_none, move_none, move_none), item=item_none):
		self.name = species.name
		self.level = level
		self.gender = species.gender(gender)
		self.type1 = species.type1
		self.type2 = species.type2
		self.ability = species.ability(ability)
		self.n_bonuses = [1.0, 1.0, 1.0, 1.0, 1.0]
		self.n_bonuses[int(nature/5)] += 0.1
		self.n_bonuses[nature % 5] -= 0.1
		self.maxHP = int(((2*species.HP + ivs[0] + int(evs[0]/4))*level)/100) + level + 10
		self.HP = self.maxHP
		self.attack = int((int((2 * species.attack + ivs[1] + int(evs[1] / 4)) * level / 100) + 5) * self.n_bonuses[0])
		self.defense = int((int((2 * species.defense + ivs[2] + int(evs[2] / 4)) * level / 100) + 5) * self.n_bonuses[1])
		self.sattack = int((int((2 * species.sattack + ivs[3] + int(evs[3] / 4)) * level / 100) + 5) * self.n_bonuses[2])
		self.sdefense = int((int((2 * species.sdefense + ivs[4] + int(evs[4] / 4)) * level / 100) + 5) * self.n_bonuses[3])
		self.speed = int((int((2 * species.speed + ivs[5] + int(evs[5] / 4)) * level / 100) + 5) * self.n_bonuses[4])
		self.stage_attack = 0
		self.stage_defense = 0
		self.stage_sattack = 0
		self.stage_sdefense = 0
		self.stage_speed = 0
		self.stage_dodge = 0
		self.stage_accuracy = 0
		self.maxPPs = [moveset[0].pp, moveset[1].pp, moveset[2].pp, moveset[3].pp]
		self.PPs = self.maxPPs
		self.moves = moveset

	def attack(self, move=0):
		"""Data is parsed/calculated by Referee object"""
		if self.PPs[move] < 1:
			return "No PP left!"
		else:
			self.PPs[move] -= 1
			if self.moves[move].status:
				return 0  # Remember to change to an actual effect
			else:
				if self.moves[move].type == self.type1 or self.moves[move].type == self.type2:  # Same Type Attack Bonus
					stab = 1.5
				else:
					stab = 1.0
				if self.moves[move].physical:
					stat = self.attack
					stage = self.stage_attack
					physical = True
				else:
					stat = self.sattack
					stage = self.stage_sattack
					physical = False
				damage = self.moves[move].power * stab * stat
				if stage < 0:
					damage *= 2/(2 - stage)
				elif stage > 0:
					damage += (2 + stage)/2
				print(self.name + " used " + self.moves[move].name + "!")
				return [int(damage), self.moves[move].attacktype, self.moves[move].accuracy, self.stage_accuracy, physical]

	def get_hit(self, damage, attacktype, move_accuracy, mon_accuracy, physical):
		if physical:
			stat = self.defense
			stage = self.stage_defense
		else:
			stat = self.sdefense
			stage = self.stage_sdefense
		typemult = self.type1[attacktype] * self.type2[attacktype]
		damage *= typemult
		if stage > 0:
			damage /= stat * ((2+stage)/2)
		else:
			damage /= stat * (2/(2-stage))
		if mon_accuracy >= 0:
			move_accuracy *= (1 + 0.5*mon_accuracy)
		else:
			move_accuracy *= (1 - 0.125*mon_accuracy)
		if self.stage_dodge >= 0:
			move_accuracy *= (1 - 0.125*self.stage_dodge)
		else:
			move_accuracy *= (1 + 0.5*self.stage_dodge)
		if randint(1, 100) > move_accuracy:
			print("But it missed!")
		else:
			self.HP -= max([1, int(damage)])
			if typemult > 1:
				print("It's super effective!")
			elif typemult < 1:
				print("It's not very effective...")
			# Insert critical hit code here.


class Species:
	def __init__(self):
		pass


class Move:
	def __init__(self):
		pass


class Ability:
	def __init__(self):
		pass


class Personality:
	def __init__(self):
		pass


class Status:
	def __init__(self):
		pass


class Item:
	def __init__(self):
		pass






