import os
import pandas as pd
from dotenv import load_dotenv
import cohere

load_dotenv()

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'catalog.csv')
output_file_path = os.path.join(base_dir, 'output.html')

df = pd.read_csv(csv_file_path)
csv_content = df.to_string(index=False)

mymessage = f"Here is the catalog data:\n{csv_content}\n\nMake a list of 5 things to plant this month in Carpinteria, CA. from catalog data. Use HTML table format with columns: Name, Catalog_ID, Instructions. Output just the table."

co = cohere.Client(api_key=os.environ["COHERE_API_KEY"])
response = co.chat(
  message=mymessage,
  preamble="You are a talented and experienced gardener and a helpful assistant to other gardeners, answering questions about product and services for the Hansel and Petal company."
  )

with open(output_file_path, 'w') as file:
  file.write(response.text)

print(f"Response saved to {output_file_path}")