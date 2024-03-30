import os.path
import openai
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

openai.api_key = "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"

def chat_with_gpt(prompt):
   response = openai.ChatCompletion.create(  # similar to post
      model = "gpt-3.5-turbo",
      # model = "text-davinci-003",
      messages = [{"role" : "user", "content": prompt}]
   )
   return response['choices'][0]['message']['content'].split(",")
 
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1DhixKHVj_RUSpiqoydnTgYjbDnbVDOPpcYwu4p3uNRk"
SAMPLE_RANGE_NAME = "Sheet1!A1:Z10"  # sheet 1 is a placeholder name representing the default sheet name in a Google Sheets document.

valueData = None
li=[]
# the function is for updating to google sheets
def m(li):
  creds = None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "google sheets\credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=3000)
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)
    sms_content = "7/1/2022 10:00::00 PM|Jared|04/12/1978|Frankton|Orange"
    sheet = service.spreadsheets()
    sheet_data = [li]
    
    # print("This is sheet data", sheet_data)
    # print(type(sheet_data))
    # print("size of list:  ", len(li))
    result = (
        sheet.values()
        .update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME, valueInputOption="USER_ENTERED", body={"values":sheet_data})
        .execute()
    )
  except HttpError as err:
    print(err)

if __name__ == "__main__":
  various_messages = ["Mr. sINGH payment made for 34000 to KKL(0905347293). Your Balance is 1200000. Thank you, for using KKL MobileMoney."]
  # while(True):
  #   x = input()
  #   if(x=="break" or x=="stop" or x=="b"):
  #     break
  #   various_messages.append(x)
  # input_message = input()
  # n = len(various_messages)
  # for i in range(n):
  input_message = various_messages
  user_input = f"the message is a bank statement message, {input_message}.You have to extract relevant information from it, only numbers, id, bank namme, etc,  if it is mentioned in it, just give me a csv value, nothing else, no double quotes as well, also if the number is in decimal form, don't remove the decimal give the original number. If any information is not mentioned, don't output it. For example iff "
  # print("HI")
  response = chat_with_gpt(user_input)
  # print(response)
  messages = []
  # li = [1, 2, 3]
  li=response
  print("This is the list", li)
  m(li)
    
# print(valueData)
# ADDING BACKEND TO IT
# USING MORE TRUSTABLE METHODS
