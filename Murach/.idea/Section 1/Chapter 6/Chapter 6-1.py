#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return  scores
        else:
            score = int(score)
            if score >= 0 and score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")

def process_scores(scores):
    # calculate average score
    score_total = 0
    for num in scores:
        score_total += num
    average = score_total / len(scores)

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", round(average))
    print("Low Score:          ", min(scores))
    print("High Score:          ", max(scores))

def main():
    display_welcome()
    final_scores = get_scores()
    process_scores(final_scores)
    print("")
    print("Bye!")

# if started as the main module, call the main function
if __name__ == "__main__":
    main()


