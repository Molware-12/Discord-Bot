from plasma import Plasma
from scrape import Scrape

def handler(input, team_name=None) -> str:
    p = Plasma()

    # Check for specific input value
    if input.startswith("128:"):
        return f"Your 128-bit digest is: {p.hash_128(input[4:])}"
    elif input.startswith("64:"):
        return f"Your 64-bit digest is: {p.hash_64(input[3:])}"

    # Creating an instance of the Scrape class
    s = Scrape("https://www.transfermarkt.us/premier-league/marktwerteverein/wettbewerb/GB1/stichtag/2023-12-15/plus/1", "transfermarkt.sc")

    if input == "man":
        return "This is the Enzinho Bot Manual. For now, Enzinho can only produce the functions in the Plasma class, and the Scrape class, which provides data of each of the current teams playing in the Premier League. \n To look for the statistics of each team, use these flags in this format: \n -sv: Returns the squad value of a team as of a certain date, in this case at the moment it is December 15th 2023. Example Usage: -sv Chelsea FC (Also, use the full teams name, not nicknames. so Bournemouth would be AFC Bournemouth) \n -ss: Returns the squad size of a team as of a certain date, in this case at the moment it is December 15th 2023. Example Usage: -ss Chelsea FC \n -cv: Returns the current squad value as of today. Example Usage: -cv Chelsea FC \n -cs: Returns the current squad size as of today. Example Usage: -cs Chelsea FC \n -d: Returns the difference of the squad value as of 2023-12-15 and the current squad value: Example Usage: -d Chelsea FC \n -p: Returns the difference in percentage format. Example Usage: -p Chelsea FC \n \n If you want a string hashed, simply type the digest amount (either 64 or 128) followed by the string you want hashed. Example Usage: 128:hashme or 64:hashme"

    # The input format must be for example: "-p Chelsea FC"
    parts = input.split(" ", 1)
    if len(parts) == 2:
        flag, provided_team_name = parts
        team_name = provided_team_name if team_name is None else team_name  # Use provided_team_name only if team_name is not specified in the function call

        # Call the comparison method on the Scrape instance only if the flag is valid
        if flag in ["-sv", "-ss", "-cv", "-cs", "-d", "-p"]:
            result = s.comparison(flag, team_name)
            return result
        else:
            return f"Invalid flag '{flag}' for team comparison. Use '-sv', '-ss', '-cv', '-cs', '-d', or '-p' for team stats."

    return "Invalid input format."
