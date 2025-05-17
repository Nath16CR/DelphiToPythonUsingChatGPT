import sys
import os

sys.path.append(os.path.abspath('../src'))
from CodeProcessor import ExecuteProcessor, GetGitTreeStructure,RelayMessageToGPT



#ExecuteProcessor()
#{self.config.source_repo_name}/contents/{folder_name}'
#https://github.com/josecascanteGL/DelphiToPythonUsingChatGPT/contents
#GetGitTreeStructure("josecascanteGL", "DelphiToPythonUsingChatGPT")
response = RelayMessageToGPT("Hola mi nombre es Pedro", "")
print(response)
response = RelayMessageToGPT("Como me llamo?", "")
print(response)