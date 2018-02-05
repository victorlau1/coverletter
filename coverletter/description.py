from textblob import TextBlob
from docx import Document

class JobDescriptionParser:
  
  def __init__(self, filepath):
    self.parse_document(filepath)

  @classmethod
  def parse_document(self, filepath):
    """
      Parses text document so that all paragraphs are accessible
    """
    with open(filepath, 'rb') as file_template:
      document = Document(file_template)
      self.top_words(document)

  @classmethod
  def top_words(self, document):
    """
      Returns the total document paragraphs
    """
    concatenate = ''
    for paragraph in document.paragraphs:
      concatenate += ' ' + paragraph.text

    total_text = TextBlob(concatenate)
    total_text.noun_phrases

if __name__ == '__main__':
  JobDescriptionParser()

