from ThemesClass import Theme
from themes import write_duties_to_html   
from themes_data import duties_list 

# Testing get associated duties getter function
def test_get_associated_duties_returns_correct_duties():
    theme = Theme("Test Theme", [1, 3, 5])
    associated_duties = theme.get_associated_duties(duties_list)
    
    assert len(associated_duties) == 3
    assert "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage." in associated_duties
    assert "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review." in associated_duties
    assert "Duty 5 Build and operate a Continuous Integration (CI) capability, employing version control of source code and related artefacts." in associated_duties

    theme1 = Theme("Bootcamp", [1, 2, 3, 4, 13])
    theme1_associated_duties = theme1.get_associated_duties(duties_list)

    assert len(theme1_associated_duties) == 5
    assert "Duty 1 Script and code in at least one general purpose language and at least one domain-specific language to orchestrate infrastructure, follow test driven development and ensure appropriate test coverage." in theme1_associated_duties
    assert "Duty 2 Initiate and facilitate knowledge sharing and technical collaboration with teams and individuals, with a focus on supporting development of team members." in theme1_associated_duties
    assert "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review." in theme1_associated_duties
    assert "Duty 4 Work as part of an agile team, and explore new ways of working, rapidly responding to changing user needs and with a relentless focus on the user experience. Understand the importance of continual improvement within a blameless culture." in theme1_associated_duties
    assert "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience." in theme1_associated_duties

def test_get_associated_duties_returns_empty_list_if_no_matches():
    theme = Theme("No Match", [99])
    associated_duties = theme.get_associated_duties(duties_list)
    
    assert associated_duties == []

# Testing correct duties and theme name is written to html file for specific theme
def test_html_file_includes_correct_information(tmp_path):
    test_theme = Theme("Test Theme", [4, 6, 8, 12])
    associated_duties = test_theme.get_associated_duties(duties_list)
    test_file_path = tmp_path / "test_file.html"

    write_duties_to_html(associated_duties, file_path=test_file_path, theme_name=test_theme.name)

    test_file_content = test_file_path.read_text()

# Check html content structure 
    assert "<!DOCTYPE html>" in test_file_content
    assert "<html" in test_file_content

# Ensure unordered list has an opening and closing tag
    assert "<ul>" in test_file_content
    assert "</ul>" in test_file_content

# Test h2 tag is in html file created with the correct theme
    assert f"<h2>{test_theme.name}</h2>" in test_file_content

# Test all associated duties are written to html file and are in a list tag
    for duty in associated_duties:
        assert duty in test_file_content
        assert f"<li>{duty}</li>" in test_file_content

# Test that the number of list tags is equal to number of associated duties
    assert test_file_content.count("<li>") == 4



