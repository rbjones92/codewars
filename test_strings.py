a_string = "A string is mroe than its parts!"
matches = "more"

if any(x in a_string for x in matches):
    print('found')