import cmd
from coverletter.coverletter import CoverLetterParser
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

  def do_EOF(self):
    """
      Terminate by entering this or ctrl + D
    """
    return True

if __name__ == '__main__':
  Cli().cmdloop()