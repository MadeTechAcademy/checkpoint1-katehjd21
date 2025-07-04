from themes import print_duties, write_duties_to_html, prompt_user_choice
from themes_data import duties_list
# Test number of duties is correct
def test_length_of_duties():
    assert len(duties_list)>10, f"Expected more than 10 duties in x2, but got {len(duties_list)}"
    assert len(duties_list) == 13, f"Expected 13 duties in x2, but got {len(duties_list)}"

# Test each duty is of type string
def test_duties_are_of_type_string():
    for duty in duties_list:
        assert isinstance(duty, str), f"Expected each Duty to be of type string, but got {type(duty)}"

# Test each duty says what it is supposed to
def test_duties_are_correct():

    expected_duties = [
        "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.", 
        "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.", 
        "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review.", 
        "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture.",
        "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts.",
        "Duty 6 Implement and improve release automation & orchestration, often using Application Programming Interfaces (API), as part of a continuous delivery and continuous deployment pipeline, ensuring that team(s) are able to deploy new code rapidly and safely.",
        "Duty 7 Provision cloud infrastructure using APIs, continually improve infrastructure-as-code, considering use of industry leading technologies as they become available (e.g. Serverless, Containers).",
        "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance.",
        "Duty 9 Apply leading security practices throughout the Software Development Lifecycle (SDLC).",
        "Duty 10 Implement a good coverage of monitoring (metrics, logs), ensuring that alerts are visible, tuneable and actionable.",
        "Duty 11 Keep up with cutting edge by committing to continual training and development - utilise web resources for self-learning; horizon scanning; active membership of professional bodies such as Meetup Groups; subscribe to relevant publications.",
        "Duty 12 Look to automate any manual tasks that are repeated, often using APIs.",
        "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
        ]
    
    assert duties_list == expected_duties

# Test that the whole list of duties is displayed in the terminal

def test_prints_all_duties_to_terminal(capsys):
    print_duties()
    result = capsys.readouterr()
    all_duties_output = result.out

    for duty in duties_list:
        assert duty in all_duties_output

# Test that when user presses '1', the whole list of duties are displayed 

def test_input_one_prints_duties(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: '1')

    prompt_user_choice()

    printed_output = capsys.readouterr().out

    for duty in duties_list:
        assert duty in printed_output

# Test that when user presses any other key, nothing is displayed

def test_input_not_one_does_not_print_duties(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: '9')

    prompt_user_choice()

    printed_output = capsys.readouterr().out

    for duty in duties_list:
        assert duty not in printed_output


# Tests all duties are printed to duties.html file 

def test_all_duties_written_in_html_file(tmp_path):
    test_duties_file = tmp_path / "test_duties.html"

    write_duties_to_html(duties_list, file_path=test_duties_file)

    duties_file_content = test_duties_file.read_text()

    for duty in duties_list:
        assert duty in duties_file_content

def test_write_duties_creates_correct_html_file(tmp_path):
     
    test_duties_list = ["Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage.", 
        "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members.", 
        "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review."]
     
    test_duties_file = tmp_path / "test_duties.html"

    write_duties_to_html(test_duties_list, file_path=test_duties_file)

    duties_html_content = test_duties_file.read_text()

# Check html content structure 
    assert "<!DOCTYPE html>" in duties_html_content
    assert "<html" in duties_html_content

# Ensure unordered list has an opening and closing tag
    assert "<ul>" in duties_html_content
    assert "</ul>" in duties_html_content

# Check each duty appears in a list tag
    for duty in test_duties_list:
        assert f"<li>{duty}</li>" in duties_html_content
        
# Ensure number of list tags is equal to number of duties 
    assert duties_html_content.count("<li>") == len(test_duties_list)







  








   


    

    
    

        
    

    
    
