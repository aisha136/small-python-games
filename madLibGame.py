#Mad Libs Game

#Game prompt
print("Let's make a sick note to the local school nurse!\nCredit for this game goes to madtakes.com\n")

sillyWordOne = input("Enter a silly word: ")
sillyWordTwo = input("Enter another silly word: ")
lastName = input("Enter your last name: ")
illness = input("Enter a random illness: ")
pluralNoun = input("Enter a plural noun: ")
adjectiveOne = input("Enter an adjective: ")
adjectiveTwo = input("Enter another adjective: ")
adjectiveThree = input("Enter one more adjective: ")
place = input("Enter a place: ")
number = input("Enter a number: ")

#Print the output w/ the ipnputted variables
print(f"\nDear School Nurse:\n\n{sillyWordOne} {lastName} will not be attending school today. He/She has come\n"
      f"down with a case of {illness} and has horrible {pluralNoun} and a/an {adjectiveOne} fever.\n"
      f"We have made an appointment with the {adjectiveTwo} Dr. {sillyWordTwo}, who has studied for many years\n"
      f"in {place} and has {number} degrees in pediatrics. He/She will send you all the information\n"
      f"you need. Thank you!\n\nSincerely,\nMr/Mrs. {adjectiveThree}")


