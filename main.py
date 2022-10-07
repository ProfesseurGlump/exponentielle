import matplotlib.pyplot as plt


def intro_bo():
  bo = "https://cache.media.education.gouv.fr/file/SP1-MEN-22-1-2019/16/8/spe632_annexe_1063168.pdf"
  def_exp = """Définition de la fonction exponentielle, comme unique fonction dérivable sur ℝ vérifiant ƒ’ = ƒ et ƒ(0) = 1.\nL’existence et l’unicité sont admises.\nNotation exp(x).\n"""
  print(f"D'après le programme officiel de la classe de première disponible ici :\n{bo}\n")
  print(def_exp)

def objective():
  but = "On souhaite tracer la courbe représentative de f = exp à partir des seules informations de la définition.\nPour cela nous allons utiliser la méthode d'Euler."
  print(but)
  

def geometric_desc():
  print("Description géométrique de la méthode d'Euler\n")
  point = "La méthode d'Euler consiste à construire une suite de points P_n de coordonnées (x_n, y_n)"
  print(point)
  
  desc_0 = "P_0 est le point de la courbe dont l'abscisse vaut x_0 = 0 et dont l'ordonnée vaut y_0 = f(0) = 1.\nC'est-à-dire le seul point de la courbe dont on connait les coordonnées (0, 1) parce qu'on a admis ces valeurs."
  
  desc_1 = """Pour construire P_1, on va utiliser le fait que la tangente en P_0 est une bonne approximation de la courbe quand l'écart h = x_1 - x_0 est "petit".\nOr on connait mieux ici la tangente que la courbe puisque son coefficient directeur est f'(0) = f(0) = y_0 = 1.\nDonc en écrivant le taux de variation, on a\n\nf'(0) ~ (y_1 - y_0) / (x_1 - x_0) = (y_1 - y_0) / h.\n\nOn en déduit y_1 = f'(0) * h + y_0 = y_0 + h puisque f'(0) = f(0) = 1."""
  
  desc_2 = "Pour construire P_2, on réitère le même procédé mais en partant de P_1.\nOn a\n\tf'(1) ~ (y_2 - y_1) / (x_1 - x_0) = (y_2 - y_1) / h.\nOn en déduit\n\ty_2 = f'(1) * h + y_1 = y_1 * (1 + h) ** 2\n\tpuisque f'(1) = f(1) ~ y_1."
  
  desc_3 = "On continue ainsi la construction des points P_n dont les coordonnées sont finalement x_n = n * h et y_n = (1 + h) ** n. "
  
  description = [desc_0, desc_1, desc_2, desc_3]
  for desc in description: 
    print(f"\n{desc}\n")
    input("Taper 'Entrée' pour la suite...")

def analytical_approach():
  prop_admises = "La fonction exponentielle est l'unique fonction dérivable sur ℝ vérifiant\nƒ’ = ƒ et ƒ(0) = 1"
  print("Principe général\n")
  
  nb_deriv_step1 = (
    "Approximation du nombre dérivé", 
    "f'(x) ~ ( f(x + h) - f(x) ) / h"
  )
  
  nb_deriv_step2 = (
    "On multiplie par h", 
    "h*f'(x) ~ f(x + h) - f(x)"
  )
  
  nb_deriv_step3 = (
    "On isole f(x + h)", 
    "f(x) + h*f'(x) ~ f(x + h)"
  )
  
  exp_property1 = (
    prop_admises, 
    "f'(x) = f(x) = exp(x)"
  )
  
  nb_deriv_step4 = (
    "On utilise la relation f' = f", 
    "f(x) + h*f(x) ~ f(x + h)"
  )
  
  nb_deriv_step5 = (
    "On factorise",
    "f(x) * (1 + h) ~ f(x + h)"
  )
  
  exp_property2 = (
    prop_admises,
    "f(0) = exp(0) = 1"
  )
  
  nb_deriv_step6 = (
    prop_admises,
    "f(0 + h) ~ (1 + h) * f(0) = (1 + h)"
  )
  
  euler_prop1 = (
    "0 + h = h", 
    "f(h) ~ (1 + h)"
  )
  
  euler_prop2 = (
    "h + h = 2*h", 
    "f(2*h) ~ (1 + h) * f(h) ~ (1 + h) ** 2"
  )
  
  euler_prop3 = (
    "2*h + h = 3*h", 
    "f(3*h) ~ (1 + h) * f(2*h) ~ (1 + h) ** 3"
  )
  
  euler_propn = (
    "(n - 1)*h + h = n*h", 
    "f(n*h) ~ (1 + h) ** n"
  )
  
  steps = [
    nb_deriv_step1, nb_deriv_step2, nb_deriv_step3, 
    exp_property1, nb_deriv_step4, nb_deriv_step5,
    exp_property2, nb_deriv_step6, euler_prop1, 
    euler_prop2, euler_prop3, euler_propn
  ]
  
  print("Partons du nombre dérivé et de 2 propriétés admises")
  
  for step in steps:
    input("Taper 'Entrée' pour la suite...")
    
    if step in {exp_property1, exp_property2}:
      print("\nAttention, ceci est une propriété admise.")
      print("Cette propriété fait partie de la définition.")
      print("Elle sera démontrée au cours des études supérieures")
    elif step in {euler_prop1, euler_prop2, euler_prop3}:
      print("\nPremières formulations de la méthode d'Euler")
    
    print(f"\n{step[0]} : {step[1]}\n")


def euler_meth_exp_num():
  euler_prop = []
  points = [(0, 1)]
  n = int(input("Nombre d'itérations n = "))
  h = float(input("Taille de l'écart h = "))
  #precision = int(input("Précision (nombre de chiffres après la virgule) = "))
  if h > 1: h = 1
  for i in range(n):
    x_n, y_n = (i+1)*h, (1+h)**(1+i)
    ep = f"f({i}*h + h) = f({x_n:.4f}) ~ (1 + h) ** {i+1} = {y_n:.4f}"
    P_n = f"P_{i+1} a pour coordonnées (x_{i+1}, y_{i+1})"
    points.append((x_n, y_n))
    euler_prop.append(f"{ep}\n{P_n} = ( {x_n:.4f}, {y_n:.4f} )")
    print(f"\n{euler_prop[i]}\n")

def euler_method_exp(n, h):
  points = [(0, 1)]
  for i in range(n):
    x_n, y_n = (i+1)*h, (1+h)**(1+i)
    points.append((x_n, y_n))
  return points

def graph():
  n = int(input("n = "))
  h = float(input("h = "))
  points = euler_method_exp(n, h)
  x_list = [p[0] for p in points]
  y_list = [p[1] for p in points]
  plt.plot(x_list, y_list)
  plt.show()
  plt.close()

def menu_general():
  menu = """
  1) Extrait du programme officiel
  2) Buts de la méthode d'Euler
  3) Description géométrique de la méthode d'Euler
  4) Approche analytique de la méthode d'Euler
  5) Application numérique de la méthode d'Euler
  6) Représentation graphique de la méthode d'Euler
  Q) Quitter
  Votre choix :  """
  choix = True
  while choix:
    choix = input(menu)
    if choix == '1': intro_bo()
    elif choix == '2': objective()
    elif choix == '3': geometric_desc()
    elif choix == '4': analytical_approach()
    elif choix == '5': euler_meth_exp_num()
    elif choix == '6': graph()
    elif choix.upper() == 'Q':
      choix = False
      print("Au revoir.")
    else:
      print("Vous n'avez pas choisi une option du menu. Essayez encore.")


menu_general()