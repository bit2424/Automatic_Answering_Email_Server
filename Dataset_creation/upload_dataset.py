from datasets import Dataset
import pandas as pd

#To find the original csv file with the dataset ask permission in the following link: https://docs.google.com/spreadsheets/d/1ub1EPU4B0f4mXjyP46qH2cA9ktlZsrUU6-n0ys6i8ug/edit?usp=sharing
df = pd.read_csv("Dataset_creation/FAQ_NelsMarketplace.csv")
print(df.head())

df_dic_org = df.to_dict(orient="records")

print(df_dic_org[0])

list_instructions = []
list_questions = []
list_context = []

for record in df_dic_org:
    instruction = record['Instruction']
    questions = record['Question'].split(';')
    context = record['Context']
    for question in questions:
        list_instructions.append(instruction.strip())
        list_questions.append(question.strip())
        list_context.append(context.strip())

   
hg_dataset = Dataset.from_dict({"Instruction": list_instructions, "Question": list_questions,"Context/Answer":list_context})
hg_dataset.push_to_hub("nelson2424/FAQ_NelsMarketplace")
