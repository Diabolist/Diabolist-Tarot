import random

# Define the Tarot Card class with Yes/No interpretations
class TarotCard:
  def __init__(self, name, upright_yes_no, reversed_yes_no):
    self.name = name
    self.upright_yes_no = upright_yes_no
    self.reversed_yes_no = reversed_yes_no

# Major Arcana (find proper interpretations here https://backyardbanshee.com/tarot/which-tarot-cards-mean-yes-or-no/)
major_arcana = [
    TarotCard("The Fool", "Yes", "No"),
    TarotCard("The Magician", "Yes", "No"),
    TarotCard("The High Priestess", "Yes", "No"),
    TarotCard("The Empress", "Yes", "No"),
    TarotCard("The Emperor", "Yes", "No"),
    TarotCard("The Hierophant", "Yes", "No"),
    TarotCard("The Lovers", "Yes", "No"),
    TarotCard("The Chariot", "Yes", "No"),
    TarotCard("Strength", "Yes", "No"),
    TarotCard("The Hermit", "No", "Yes"),
    TarotCard("Wheel of Fortune", "Yes", "No"),
    TarotCard("Justice", "Yes (Upright), No (Reversed)", "No"),
    TarotCard("The Hanged Man", "Yes", "No"),
    TarotCard("Death", "No", "Yes"),
    TarotCard("Temperance", "Yes", "No"),
    TarotCard("The Devil", "No", "Yes"),
    TarotCard("The Tower", "No", "Yes"),
    TarotCard("The Star", "Yes", "No"),
    TarotCard("The Moon", "No", "Yes"),
    TarotCard("The Sun", "Yes", "No"),
    TarotCard("Judgement", "Maybe (Upright), No (Reversed)", "No"),
    TarotCard("The World", "Yes", "No"),
]

# Minor Arcana (Interpretations based on your provided meanings)
suits = ["Wands", "Cups", "Swords", "Pentacles"]
minor_arcana = []
for suit in suits:
  for number in range(1, 11):
    # Specific interpretations for individual cards, replace text in quotations with your own - keep in mind the first quotation is the card upright and the second is the card reversed.
    if suit == "Wands":
      if number == 1:
        upright_yes_no, reversed_yes_no = "Yes", "No"
      elif number == 2:
        upright_yes_no, reversed_yes_no = "Yes", "No"
      elif number == 3:
        upright_yes_no, reversed_yes_no = "Yes", "No"
      elif number == 4:
        upright_yes_no, reversed_yes_no = "Yes", "No"
      elif number == 5:
        upright_yes_no, reversed_yes_no = "No", "Yes"
      elif number == 6:
        upright_yes_no, reversed_yes_no = "Yes/Maybe", "No"
      elif number == 7:
        upright_yes_no, reversed_yes_no = "No", "Yes"
      elif number == 8:
        upright_yes_no, reversed_yes_no = "No", "Yes"
      elif number == 9:
        upright_yes_no, reversed_yes_no = "Yes", "No"
      elif number == 10:
        upright_yes_no, reversed_yes_no = "Yes", "No"
    elif suit == "Cups":
      if number == 1:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # New Relationship (Upright), Confusion (Reversed)
      elif number == 2:
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Attraction (Upright), Disharmony (Reversed)
      elif number == 3:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Joy, Celebration (Upright), Self-Indulgence (Reversed)
      elif number == 4:  
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Contentment (Upright), Isolation (Reversed)
      elif number == 5:  
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Loss, Grief (Upright), Letting Go (Reversed)
      elif number == 6:  
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Reuniting, Forgiveness (Upright), Dependence (Reversed)
      elif number == 7:  
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Illusion, Fantasy (Upright), Facing Reality (Reversed)
      elif number == 8:  
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Great Joy, Abundance (Upright), Superficiality (Reversed)
      elif number == 9:  
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Disappointment, Rejection (Upright), Release (Reversed)
      elif number == 10:  
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Contentment, Fulfillment (Upright), Stagnation (Reversed)
    elif suit == "Swords":
      if number == 1:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Victory, Triumph (Upright), Defeat (Reversed)
      elif number == 2:  
        upright_yes_no, reversed_no = "No", "No"  # Truce, Stalemate (Upright), Indecision (Reversed)
      elif number == 3:  
        upright_yes_no, reversed_no = "Yes", "No"  # Grief, Loss (Upright), Anger (Reversed)
      elif number == 4:  
        upright_yes_no, reversed_no = "Yes", "No"  # Rest, Recuperation (Upright), Delay (Reversed)
      elif number == 5:  
        upright_yes_no, reversed_no = "No", "No"  # Defeat, Betrayal (Upright), Self-Sabotage (Reversed)
      elif number == 6:  
        upright_yes_no, reversed_no = "Maybe/Yes", "No"  # Journey, Change (Upright), Resistance (Reversed)
      elif number == 7:  
        upright_yes_no, reversed_no = "No", "No"  # Deception, Lies (Upright), Self-Discovery (Reversed)
      elif number == 8:  
        upright_yes_no, reversed_no = "Yes", "No"  # Strength, Willpower (Upright), Harshness (Reversed)
      elif number == 9:  
        upright_yes_no, reversed_no = "No", "No"  # Cruelty, Violence (Upright), Awakening (Reversed)
      elif number == 10:  
        upright_yes_no, reversed_no = "No", "No"  # Ruin, Destruction (Upright), Transformation (Reversed)
    elif suit == "Pentacles":
      if number == 1:
        upright_yes_no, reversed_yes_no = "Yes", "Maybe/Yes"  # Security (Upright), Instability (Reversed)
      elif number == 2:
        upright_yes_no, reversed_yes_no = "Maybe/Yes", "No"  # Possession (Upright), Greed (Reversed)
      elif number == 3:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Abundance, Growth (Upright), Stagnation (Reversed)
      elif number == 4:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Security, Stability (Upright), Neglect (Reversed)
      elif number == 5:
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Loss, Material Concerns (Upright), Letting Go (Reversed)
      elif number == 6:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Success, Recognition (Upright), Self-Doubt (Reversed)
      elif number == 7:
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Discontent, Yearning (Upright), Contentment (Reversed)
      elif number == 8:
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Mastery, Wealth (Upright), Materialism (Reversed)
      elif number == 9:
        upright_yes_no, reversed_yes_no = "No", "Yes"  # Gains, Unexpected Windfall (Upright), Carelessness (Reversed)
      elif number == 10:  
        upright_yes_no, reversed_yes_no = "Yes", "No"  # Wealth, Fulfillment (Upright), Greed (Reversed)
  # Court Card Interpretations (Yes/No, Specific Meanings)
court_card_meanings = {
  # Pentacles
  "Page of Pentacles": ("Yes", "This is a card with the message 'go for it!'"),
  "Knight of Pentacles": ("Yes", "This is a card of slow progress is still progress."),
  "Queen of Pentacles": ("Yes", "This is a card of knowledge, wholeness and support."),
  "King of Pentacles": ("Yes", "This is a card of balance, honesty with yourself and wisdom of experiences."),
  "Page of Pentacles (Reversed)": ("No", ""),
  "Queen of Pentacles (Reversed)": ("No", ""),
  "King of Pentacles (Reversed)": ("No", ""),  
  # Swords
  "Page of Swords": ("No", "Be vigilant with yourself and your values."),
  "Knight of Swords": ("No", "This card has themes of recklessness and impulsiveness."),
  "Queen of Swords": ("Yes", "This card has themes of self-reliance, of balance and being guarded for protective, nurturing purposes."),
  "King of Swords": ("Yes", "Ensure that logic overrules emotion for scenarios relating to love and to work."),
  "Page of Swords (Reversed)": ("Yes", ""),
  "Knight of Swords (Reversed)": ("Yes", ""),
  "Queen of Swords (Reversed)": ("No", ""),  
  "King of Swords (Reversed)": ("No", ""),
  # Wands
  "Page of Wands": ("Yes", "This is a message of naivety but in a positive, childlike way."),
  "Knight of Wands": ("Yes", "This is a card calling you to be brave."),
  "Queen of Wands": ("Yes", "This card has themes of fierceness and passion."),
  "King of Wands": ("Yes", "This is a card with themes of never backing down, and knowing who you are."),
  "Page of Wands (Reversed)": ("No", ""),
  "Knight of Wands (Reversed)": ("No", ""),
  "Queen of Wands (Reversed)": ("No", ""),
  "King of Wands (Reversed)": ("No", ""),
  # Cups
  "Page of Cups": ("Yes", "This is a card of happiness, kindness, and friendship."),
  "Knight of Cups": ("No", "This is a card showing you you're working with your heart over your head."),
  "Queen of Cups": ("Yes", "This is a card of nourishment and support."),
  "King of Cups": ("Yes", "This is a loving card of guidance and integrity."),
  "Page of Cups (Reversed)": ("No", ""),
  "Knight of Cups (Reversed)": ("Yes", ""),
  "Queen of Cups (Reversed)": ("No", ""),
  "King of Cups (Reversed)": ("No", ""),
  }

for suit in suits:
  for court_card in ["Page", "Knight", "Queen", "King"]:
    upright_yes_no, upright_interpretation = court_card_meanings[f"{court_card} of {suit}"]
    reversed_yes_no = "No" if upright_yes_no == "Yes" else "Yes"  # Reversed meaning (opposite of upright)
    reversed_interpretation = ""
    minor_arcana.append(TarotCard(f"{court_card} of {suit} (Upright)", upright_yes_no, upright_interpretation))
      
#Combining Major and Minor Arcana into a full deck
deck = major_arcana + minor_arcana

#Function to randomly "Shuffle"" the deck
def shuffle_deck():
  random.shuffle(deck)

#Draw a single card at random
def draw_card():
  shuffle_deck()
  return deck.pop()

#Interpret a card (considering upright/reversed position)
def interpret_card(card):
  upright = random.randint(0, 1)  # Draw card in random position (Upright / Reversed)
  yes_no = card.upright_yes_no if upright else card.reversed_yes_no
  return f"{card.name} ({'Upright' if upright else 'Reversed'}): {yes_no}"

# Perform a Yes/No reading
def do_yes_no_reading():
  card = draw_card()
  interpretation = interpret_card(card)
  print(interpretation)

# Main Loop
while True:
  print("\nWelcome to Diabolist Tarot!")
  print("Write your Yes or No question here and the program will randomly give an answer.\n Remember you should try your best to keep at bay when using Tarot.")
  print("Type 'exit' to quit.")

  question = input("Your question: ")
  if question.lower() == "exit":
    break  # Exit when user types 'exit' or uses a KeyboardInterrupt

  do_yes_no_reading()  # "Completes" the Yes/No reading

print("\nThank you for using Diabolist Tarot!") #goodbye message

