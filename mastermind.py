import random

def mastermind():

    colour1 = ['R', 'B', 'G', 'W', 'B', 'P']
    colour2 = ['R', 'B', 'G', 'W', 'B', 'P']
    colour3 = ['R', 'B', 'G', 'W', 'B', 'P']
    colour4 = ['R', 'B', 'G', 'W', 'B', 'P']

    c1 = random.choice(colour1)
    c2 = random.choice(colour2)
    c3 = random.choice(colour3)
    c4 = random.choice(colour4)

    count = 1

    name = input("Hello. Please Enter Your Name: ")

    print()
    print("Hi", name, "and Welcome to Mastermind! Your job is to guess a four colour combination (either Red, Blue, Green, White, or Pink) that randomly generates every time you play.")
    print()

    ready = input("Are you ready? [y/n] ")

    if ready in ['y']:

        while True:
        
            print()

            guess1 = input("Enter your First colour [R/B/G/W/P]: ")
            guess2 = input("Enter your Second colour [R/B/G/W/P]: ")
            guess3 = input("Enter your Third colour [R/B/G/W/P]: ")
            guess4 = input("Enter your Fourth colour [R/B/G/W/P]: ")

            colourswrong = 0

            if guess1 and guess2 and guess3 and guess4 in ['R', 'B', 'G', 'W', 'P']:

                if guess1 != c1:

                    colourswrong += 1

                if guess2 != c2:

                    colourswrong += 1

                if guess3 != c3:

                    colourswrong += 1

                if guess4 != c4:

                    colourswrong += 1

                if colourswrong == 0:

                    print()
                    print('You Got It!')
                    print('It took you ' + str(count) + ' trie(s) to guess the colour combinaton!')

                    break

                else:

                    print()
                    print('You got ' + str(4-colourswrong) + ' colour(s) right.')
                    print()

                count += 1

            else:

                print()
                print("Please enter one of colours")

                if guess1 and guess2 and guess3 and guess4 in ['R', 'B', 'G', 'W', 'P']:

                    if guess1 != c1:

                        colourswrong += 1

                    if guess2 != c2:

                        colourswrong += 1

                    if guess3 != c3:

                        colourswrong += 1

                    if guess4 != c4:

                        colourswrong += 1

                    if colourswrong == 0:

                        print()
                        print('You Got It!')
                        print('It took you ' + str(count) + ' trie(s) to guess the colour combinaton!')

                        break

                    else:

                        print()
                        print('You got ' + str(4-colourswrong) + ' colour(s) right.')
                        print()

                    count += 1

            

    if ready in ['n']:

        print()
        print("Okay. Come back when your ready.")

mastermind()
