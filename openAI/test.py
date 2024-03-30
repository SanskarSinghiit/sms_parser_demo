# import openai
# openai.api_key = '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'  # Replace with your actual API key
# def get_gpt_response(message, max_tokens=200):
#    response = openai.ChatCompletion.create(
#       model="gpt-3.5-turbo",
#       messages=[{"role": "system", "content": "You are a helpful assistant."}, 
#                   {"role": "user", "content": message}],
#       max_tokens=max_tokens,
#       temperature=0.7
#    )
#    return response['choices'][0]['message']['content']

# while(True):
#    x = input("User : ")
#    print("ChatGPT : ", get_gpt_response(x), '\n')

import openai

openai.api_key = "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"

def chat_with_gpt(prompt):
   response = openai.ChatCompletion.create(  # similar to post
      model = "gpt-3.5-turbo",
      messages = [{"role" : "user", "content": prompt}]
   )
   return response['choices'][0]['message']['content']

# if __name__ == "__main__":
# def main():
   # while(True):
   user_input ="following message is a bank statement message, You have received UGX50,000 from 0771234567. Reason: Salary. Your balance is UGX120,000.  return just in format of a csv string all valuable information "
   # if(user_input.lower() in ["quit", "exit", "bye"]):
      # break
   response = chat_with_gpt(user_input)
   print(response)
   n = len(response)
   list1 = response.split(",")
   print("Printing list :=> ", list1)
   # return list1
      # for i in range(n):
      #    list1
      # print(response) 

# main()   
      
'''
the message is a bank statement message, "You have received UGX50,000 from 0771234567. Reason: Salary. Your balance is UGX120,000."  return just in format of python dictionary all valuable information

'''