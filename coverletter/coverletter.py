import os

class CoverLetterParser:

  separators = {
    1: '[]',
    2: '{}',
    3: '//'
  }

  def __init__(self, document, words):
    self.words = words
    separator = self.select_separator()
    self.parse_document(document, separator)

  def parse_document(self, document, separator):
    """
      Parse the document iterating through all the body paragraph
    """
    for paragraph in document.paragraphs:
      place_counter = 0
      for text in paragraph.text:
        place_counter += 1
        if text == separator[0]:
          variable_text = self.get_placeholder(paragraph.text, place_counter, separator[1])
          variable_text = separator[0] + variable_text + separator[1]
          text_object = self.insert_overwrite(paragraph.text, variable_text)
          place_counter = place_counter + text_object['counter'] - len(variable_text)
          paragraph.text = text_object['new_text']
          print(paragraph.text)

    accepted = self.verify_document(document)
    if accepted:
      self.save_document(document)
    else:
      self.parse_document(document, separator)
    
    
  @staticmethod
  def get_placeholder(text, temp_cnt, separator):
    """
      Grabs placeholder variable and returns the text inbetween
    """
    full_text = False
    temp_text = ''
    while not full_text:
      if temp_cnt == len(text): 
        return text
      elif text[temp_cnt] == separator:
        return temp_text
      else:
        temp_text += text[temp_cnt]
        temp_cnt += 1

  def insert_overwrite(self, old_text, prompt_text):
    """
      Overwrite the separators with expected input
    """
    print('Variable Text is: ', prompt_text)
    text_object = {
      'counter': 0,
      'new_text': 'string'
    }

    if self.words:
      print(self.words)

    new_text = input('What would you like the new text to be? ')
    text_object['counter'] = len(new_text)
    text_object['new_text'] = old_text.replace(prompt_text, new_text, 1)
    return text_object

  def verify_document(self, document):
    for paragraph in document.paragraphs:
      print(paragraph.text)

    verify = input('Does this look like the output you would like (Y/N)? ')
    return bool(verify)

  def save_input_field(self, answer):
    """
      For same fields, save them to this session so we can reuse the same input
    """
    if not self.database:
      self.database = {}
      self.database[inputfield] = answer
    else: 
      self.database[inputfield] = answer

  @staticmethod
  def save_document(document):
    """
      Save document based on user input save location
    """
    path = input('Where would you like to save the document? ')
    new_name = input('What is the filename... example [FName-LName-Date] ')
    document.save(os.path.join(path + new_name))


  def select_separator(self):
    """
      Allow user to specify selector that they will be utilizing
    """
    selected_input = False

    while not selected_input:
      for key in self.separators:
        print('Option ', key, ' :', self.separators[key])
      selected_input = input('Select an option from above or insert custom one: ')
      
      try: 
        if int(selected_input):
          return self.separators[int(selected_input)]
      except ValueError:
        print('Did not find option within default parameters')
        return selected_input
      except KeyError:
        print('Range was outside of default values')
        self.select_separator()
      except:
        print('Unknown error')
        self.select_separator()



if __name__ == '__main__':
  CoverLetterParser()