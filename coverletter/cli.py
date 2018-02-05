import cmd
from coverletter.coverletter import CoverLetterParser
<<<<<<< Updated upstream
=======
from coverletter.description import JobDescriptionParser
>>>>>>> Stashed changes
from docx import Document

class Cli(cmd.Cmd):
  """
    Initiates cmd loop 
  """

  intro = "Command Line Parser"
  
  def do_prompt(self, line='Initial'):
    """
      Prompts to initiate coverletter template
    """
    directory = input('Please input the absolute path to the local document: ')
    with open(directory, 'rb') as file_template:
      document = Document(file_template)
      separator = CoverLetterParser.select_separator()
      CoverLetterParser.parse_document(document, separator)

  def do_analysis(self, arg):
    """
      Analysis to initiate the NLP modulue TextBlob
    """
    directory = input('Please input the absolute path to the local job document: ')
    JobDescriptionParser(directory)

  def do_EOF(self):
    """
      Terminate by entering this or ctrl + D
    """
    return True

if __name__ == '__main__':
  Cli().cmdloop()