from random import randint

prop_alg_exp = [
  ('exp(x + y)', 'exp(x) * exp(y)'),
  ('exp(x - y)', 'exp(x) / exp(y)'),
  ('exp(-x)', '1 / exp(x)'),
  ('exp(0)', '1'),
  ('exp(n * x)', '[exp(x)] ** n'),
]

cond = True
def continuer(cond):
  choix = input("Continuer ? 1) Oui\t0) Non\nVotre choix = ")
  if choix == '1': return True
  elif choix == '0': return False 
  else: return continuer(cond)
    
while cond:
  alea = randint(0, len(prop_alg_exp) - 1)
  print("Ecrivez la bonne réponse")
  if alea % 4 == 0:
    question, bonne_reponse = prop_alg_exp[alea]
  elif alea % 4 == 1:
    bonne_reponse, question = prop_alg_exp[alea]
  elif alea % 4 == 2:
    bonne_reponse, question = prop_alg_exp[alea]
  elif alea % 4 == 3:
    question, bonne_reponse = prop_alg_exp[alea]  
  user_response = input(f"{question} = ")
  if user_response == bonne_reponse:
    print("Bravo c'est la bonne réponse !")
  else:
    print(f"Dommage ! La bonne réponse est : {bonne_reponse}")
  cond = continuer(cond)
