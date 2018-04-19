# Just a scratch file to really drive home the point of classes and it's creation/implementation.

my_dict = {} # hehe, puns.

"""
Python is OOP, which means that it manipulates programming constructs - called OBJECTS.
You can think of an object as a single data structure that contains data, as well as functions.
The functions of a specific object, are called it's METHODS.

For example, any time that you call:
"""
len("Word")
	# Python is checking to see whether the string OBJECT you passed to it has a length. If it does,
	## return the value associated with that ATTRIBUTE. When you call:
my_dict.items()
	# Python checks to see if 'my_dict()' has an items() METHOD (which all dictionaries do) and
	## executes that method if/when it's found. A Class is essentially just a way of organizing
	### and producing objects with similar attributes and methods.

	""" Here's a class definition called 'Fruit', and then we created a 'lemon' instance of Fruit. """
class Fruit(object):
	# A class that makes various tasty fruits.
	def __init__(self, name, color, flavor, poisonous):
		self.name = name
		self.color = color
		self.flavor = flavor
		self.poisonous = poisonous

	def description(self):
		print("I'm a %s %s and I taste %s.") % (self.color, self.name, self.flavor)

	def is_edible(self):
		if not self.poisonous:
			print("Yep! I'm edible.")

		else:
			print("Don't eat me, i'll like, kill you and stuff.")

lemon = Fruit("lemon", "yellow", "sour", False)
# >>> lemon = instance of FRUIT class. Name='lemon', color='yellow', flavor='sour', poison='NOPE'
## Then we'd call the FRUIT class' METHODS.
lemon.description() #>>> Prints the description
lemon.is_edible() #>>> Prints the if/else function, depending on True or False



""" CLASS SYNTAX SO YOU CAN CREATE CLASSES GOOD AND DO OTHER THINGS GOOD TOO """
# A basic class consists only of the 'class' keyword, the name of the class, and from which the
## new class INHERITS in parentheses. For the next example or so, we'll inherit our dashing
### good looks from the OBJECT class, like so:
class NewClass(object):
	pass # This does nothing. It's useful as a placeholder in areas of code where Python expects expressions.

""" This gives them the powers and abilities of a Python OBJECT. By convention, user-defined Python
class names begin with a capital letter."""

""" LETS ACTUALLY DO SOME STUFF WITH THE THINGS """
""" You noticed earlier, that inside the class definition, we start with a function that starts off with
__init__(). This FUNCTION is required for classes; and it's used to INITIALIZE the objects it creates.
__init__() ALWAYS takes at least ONE argument, (self) - which refers to the object being created. You can
think of __init__() as the function that 'boots up' EACH OBJECT the class creates. """

# One thing that I think is important to note, when you hear 'instantiate', that means to 'create' something.

class NewNewClass(object):
	def __init__(self): # You're not special, self, you just wanna be first so you can have your sweet ID.
		self.name = name # hey stupid.function(), self.name's name is NAME. I'm not confused, you are.

# Hey neat-o. Guess what? you're ready to start creating objects. What's a 'God complex' anyway?
# We can access attributes of our objects, using dot.notation - see what I did there?
# We'll slow it down some for those of us who like picture books more than them word books.

class Earth(object): # Oi, I created an object class named EARTH. It's nice there. We like Earth.
	def __init__(self): # And on the first day, I init- sorry. *GOD* initialized THE EARTH.
		self.sides = 0 # THAT EARTH OBJECT HAS ZERO SIDES. NOPE. NONE. ZILCH.
		self.is_flat = False # Here's a variable which holds the answers to stupid question(s)

my_planet = Earth() # hey lil guy, hold this object so it doesn't float into the ether.
print my_planet.sides # >>> prints the total amount of sides of the earth. Like, all of it's sides. Added. All of them.
print my_planet.is_flat # >>> prints the answer to said stupid question that we like to still ask. Computers don't lie.

""" Now that we have a basic "understanding" of how classes and objects work - let's dive a bit more into
__init__() and self. They can be confusing. As we mentioned, __init__() is used to refer to the instance
object, and by convention - that is almost always 'self'. If you add additional arguments, like name or
age- setting each of those = to self.name and self.age in the body of __init__() will make it so that when
you create an instance object of your class, you NEED to give each instance a name and an age, and those
values will be associated with the particular instance you create. NOW LETS TRY! """

class Parents(object): # boom, we created our own parents. Wait, no. No. This is gross now.
	def __init__(self, money, has_job): # we boot up our parents, lets give 'em money, get 'em employed.
		self.money = money				# boom. Gave our parents the money object. No rosebud;; needed.
		self.has_job = has_job			# now they can hold how easy it is to get a job in their day over your head!

chad_bro_chill = Parents(0, False)		# Oh dear god, no. What have we done? Can you put it back in? Are you sure?

print(chad_bro_chill.money)				# Guess what chad? Your parent's $ isn't your $. No, I don't know who your Dad is.
print(chad_bro_chill.has_job) 			# Who knew slingin' Natty Ice's with your 'bois' WASNT an occupation? Not Chad.