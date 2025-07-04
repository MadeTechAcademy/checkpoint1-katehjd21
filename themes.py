from ThemesClass import Theme
from themes_data import duties_list, themes_dict


def print_duties():
    for duty in duties_list:
        print("{0}\n".format(duty))


def write_duties_to_html(duties, file_path="duties.html", theme_name=None):
    duties_html = open(file_path, "w")

    duties_html.write("""<!DOCTYPE html>
<html lang="en">
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Apprenticeship Duties</title>
</head>
<body>
<header>
<h1>Apprenticeship Duties</h1>
</header>
""")

    if theme_name:
            duties_html.write(f"<h2>{theme_name}</h2>\n")

    duties_html.write("<ul>\n")
    
    for duty in duties:
            duties_html.write(f"  <li>{duty}</li>\n")

    duties_html.write("""</ul>
</body>
</html>
""")

    print(f"Duties have been written to {file_path}.")
          

def prompt_user_choice():
    x = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties\n
              
    Or choose a theme to see it's associated duties:
              
    2) Bootcamp
    3) Automate!
    4) Houston, Prepare to Launch
    5) Going Deeper
    6) Assemble!
    7) Call Security
              
    Enter your choice:
    """)
    if x == '1':
        print_duties()
        write_duties_to_html(duties_list)
    elif x in themes_dict:
        theme = themes_dict[x]
        duties_for_theme = theme.get_associated_duties(duties_list)
        print(f"\nDuties for theme '{theme.name}':")
        for duty in duties_for_theme:
            print(f"- {duty}")
        
        theme_and_associated_duties_file = f"{theme.name.lower().replace(' ', '_')}.html"
        write_duties_to_html(duties_for_theme, theme_and_associated_duties_file, theme_name=theme.name)
            
        
         

if __name__=="__main__":
    prompt_user_choice()
   