import cmd
from .coverletter import CoverLetterParser
from docx import Document

class Cli(cmd.Cmd):
  
  """
    Initiates cmd loop 
  """
  intro = "Simple Cover Letter Parser" 

  def do_prompt(self):
    """
      Prompts to initiate the prompt to create from a template
    """
    directory = input('Please input the absolute path to the local document: ')
    with open(directory, 'rb') as file_template:
      document = Document(file_template)
      separator = CoverLetterParser.select_separator()
      CoverLetterParser.parse_document(document, separator)

  def do_EOF(self):
    return True

if __name__ == '__main__':
  Cli().cmdloop()