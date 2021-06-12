import pandas as pd
import csv
import plotly.express as px
df=pd.read_csv("data.csv")
student_df=df.loc[df["student_id"]=="TRL_xsl"]
print(student_df.groupby("level")["attempt"].mean())
with open("data.csv") as csv_file :
     df=csv.DictReader(csv_file)
     fig=px.scatter(
         df,
         x=("student_id"),
         y=("level")
         )
     fig.show()
