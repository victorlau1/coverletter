import cmd
from coverletter.coverletter import CoverLetterParser
from coverletter.description import JobDescriptionParser
from docx import Document

class Cli(cmd.Cmd):
  """
    Initiates cmd loop 
  """

  intro = "Command Line Parser"
  
  def do_prompt(self, words=None):
    """
      Prompts to initiate coverletter template
    """
    directory = input('Please input the absolute path to the local document: ')
    with open(directory, 'rb') as file_template:
      document = Document(file_template)
      CoverLetterParser(document, words)

  def do_analysis(self, default='Main'):
    """
      Analysis to initiate the NLP module TextBlob
    """
    directory = input('Please input the absolute path to the local job document: ')
    top_words = JobDescriptionParser(directory).output
    self.do_prompt(top_words)

  @staticmethod
  def do_EOF(self):
    """
      Terminate by entering this or ctrl + D
    """
    return True

if __name__ == '__main__':
  Cli().cmdloop()