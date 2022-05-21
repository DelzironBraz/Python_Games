correct_answers = ['a', 'd', 'c']
user_answers = []
score = 0

print("1 - What is one of the big differences between traditional media and social media? ")
print("a. participatory production")
print("b. social media reaches only a few people at a time")
print("c. the management structure of the companies")
print("d. traditional media offers no way for audiences to communicate with media producers\n")
user_answers.append(input(("What is your choice ? (A), (B), (C) or (D): \n")))
if user_answers[0] == correct_answers[0]:
    score +=1

print("2 - Which of the following is NOT a fundamental area of change regarding people's media habits?")
print("a. conversation")
print("b. collaboration")
print("c. choice")
print("d. communication\n")
user_answers.append(input(("What is your choice ? (A), (B), (C) or (D): \n")))
if user_answers[1] == correct_answers[1]:
    score +=1

print("3 - An important lesson learned in online political campaigns in recent \
years and other collaborative efforts that had online components is")
print("a. people much prefer to do their own thing and not work in groups")
print("b. there is always a couple people who disrupt the work of others in the group")
print("c. people need to be able to meet face to face at times as well as online")
print("d. social media has still not lived up to its promise of helping people collaborate\n")
user_answers.append(input(("What is your choice ? (A), (B), (C) or (D): \n")))
if user_answers[2] == correct_answers[2]:
    score +=1

print(f"Score: {score}")

