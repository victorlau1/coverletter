import cmd
from docx import Document


class CoverLetterParser(cmd.Cmd):
  
  """
    Initiates an Instance of Document Parser with Template
  """
  separators = {
    1: '[]',
    2: '{}',
    3: '//'
  }


  intro = "Simple Cover Letter Parser" 

  def do_prompt(self, line):
    #Present a link to a word document
    #directory = input('Please input the absolute path to the local document: ')
    directory = '/mnt/c/Users/Victor/Downloads/Cover Letter Template.docx'
    file_template = open(directory, 'rb')
    document = Document(file_template)
    separator = self.select_separator()
    self.parse_document(document, separator)

  #Once Open Parse the Document for Separators, defaults to [];
  @classmethod
  def parse_document(self, document, separator):
    """
      Parse the document
    """

    temp = separator[0]
    tracking_text = False
    counter = 0
    print('Selector is:', separator)
    #Go through the document
    
    for paragraph in document.paragraphs:
      counter = 0
      for text in paragraph.text:
        counter += 1
        if tracking_text and text != separator[1]:
          text = ''
        if text == separator[0]:
          tracking_text = True
          text = ''
          temp = self.get_placeholder(paragraph.text, counter, separator[1])
        elif text == separator[1]:
          tracking_text = False
          print('[',temp,']')
          self.insert_overwrite(paragraph.text)
          end_length = counter + len(raw_text)
          print(paragraph.text[counter:end_length])


  #Grab placeholder
  @staticmethod
  def get_placeholder(text, temp_cnt, separator):
    full_text = False
    temp_text = ''
    while not full_text:
      if text[temp_cnt] == separator:
        return temp_text
      else: 
        temp_text += text[temp_cnt]
        temp_cnt += 1

  #Reads Inputs for Specific Headers Supported are within the list  
  @staticmethod
  def insert_overwrite(text, ):
    """
      Overwrite the separators with expected input;
    """
    text_split = text.split(' '))
    for word in text_split:
      if word[0] == separator
    new_text = input('What new text do you want to put inside?')

  @staticmethod
  def save_input_field(answer):
    """
      For same fields, save them to a database so we can reuse the same input
    """
    if not self.database:
      self.database = {}
      self.database[inputfield] = answer
    else: 
      self.database[inputfield] = answer

  @staticmethod
  def write_document(document):
    """
      Save document based on user input save location
    """

    path = input('Where would you like to save the document?')
    new_name = input('What is the filename... example [FName-LName-Date]')
    document.save(path + new_name)

  @classmethod
  def select_separator(self):
    """
      Allow user to specify selector that they will be utilizing
    """
    selected_input = False

    while not selected_input:
      for key in self.separators:
        print('Option ', key, ' :', self.separators[key])
      selected_input = input('Select an option from above or insert custom one: ') 
      if (self.separators[int(selected_input)]):
        return self.separators[int(selected_input)]
      else:
        return selected_input

if __name__ == '__main__':
  CoverLetterParser().cmdloop()