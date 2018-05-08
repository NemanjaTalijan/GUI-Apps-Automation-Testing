'''
 This is the sample of use for testing windows desktop apps using pywinauto python library.
 This lib is using OpenCV python lib for picture recognition, therefore this is picture recognition assisted app automation testing
  - Windows Detective and Swapy are helpers used for fetching specific app control identifiers
  - For in program app control identifiers fetching, PrintControlIdentifiers() is used like app.SaveAs.PrintControlIdentifiers()
'''

from pywinauto import *

app = application.Application()
app.start('Notepad.exe')

editField = app.Notepad.Edit.TypeKeys('Text in editor input field', with_spaces=True)
editTextField = app.Notepad.Edit.WindowText()
assert 'Text in editor input field' in editTextField
app.Notepad.MenuSelect('File-> SaveAs')
app.SaveAs.Edit.SetText('notepad.txt')
# app.SaveAs.PrintControlIdentifiers()
app.SaveAs.Save.click()
print(app.ConfirmSaveAs)
if app.ConfirmSaveAs.Edit is not None:
    saveFilePath = app.SaveAs.Toolbar4
    saveFilePath.SetFocus()
    saveFilePath.SetText('Address: C:/Users/ntalijan/Desktop/site')
    app.ConfirmSaveAs.Yes.click()
    print('In')

app.kill()
