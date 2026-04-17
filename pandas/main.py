import pandas as pd
from typing import List

# def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
#     return pd.DataFrame(student_data, columns=["student_id", "age"])

# df = createDataframe([[1, 15], [2, 11], [3, 11], [4, 20]])
# print(df)

# def getDataframeSize(players: pd.DataFrame) -> List[int]:
#     return [players.shape[0], players.shape[1]]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    print(employees)
    return employees.head(3)

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"]= [2*i for i in employees["salary"].tolist()]
    return employees

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates("email")
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=['name'])

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']=employees["salary"] * 2
    return employees


def renameColumns(students: pd.DataFrame) -> pd.DataFrame:    
    return students.rename(columns={'id': 'student_id', 'first': 'first_name','last': 'last_name','age': 'age_in_years'})

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade']= students['grade'].astype(int)
    return students
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity']=products['quantity'].fillna(0)
    return products

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2])


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index="month",values="temperature",columns="city")
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    # Filter for weight > 100, sort descending, and return only the 'name' column
    return animals[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return report.melt(id_vars='product',var_name='quarter',value_name='sales')
