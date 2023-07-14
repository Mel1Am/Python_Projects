def prompt_and_get_response(message):
    print(message)
    return input()

def main():
    print("A post has been made in the Platform Integration Field Support Channel")
    print("Team member responsible should read the posts from the Teams Channel that may have been made the day before or within the day.")
    print("Add post to issue tracker spreadsheet.")

    while True:
        response = prompt_and_get_response("24 hours have past since the post was made?")
        if response == "Yes":
            break
        else:
            print("Wait for at least 24 hrs before reaching out with a response.")

    while True:
        response = prompt_and_get_response("Has a resolution been provided?")
        if response == "Yes":
            break
        else:
            while True:
                response = prompt_and_get_response("Research for any possible solution you might find. Did you find a resolution?")
                if response == "Yes":
                    print("Provide the Resolution with any added resource page they might need.")
                    break
                else:
                    print("Default Answer 2: Try to point in the right direction and request the post owner to raise a Support Jira Ticket. Provide with any resource or template they might need.")
            
            while True:
                response = prompt_and_get_response("Have you answered with any of the default replies?")
                if response == "Yes":
                    break

    response = prompt_and_get_response("Is a reply required for the post owner?")
    if response == "Yes":
        print("Reply with best solution found.")

    print("Document the Problem/Solution in the Wiki Spreadsheet.")
    print("Update Issue Tracker spreadsheet.")

if __name__ == "__main__":
    main()
