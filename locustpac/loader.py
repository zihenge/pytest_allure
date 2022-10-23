import csv
from typing import Text,List,Dict
def losd_csv_file(csv_file: Text) -> List[Dict]:
    """
    csv_file 文件格式举例：
        email,password
        62466555@qq.com,123456
        62466555@qq.com,123456s
    返回的数据格式举例：
        [
            {"email":"62466555@qq.com","password":"123456"},
            {"email":"62466555@qq.com","password":"123456"}
        ]
    :param csv_file:
    :return:
    """
    csv_content_list = []
    with open(csv_file, encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            csv_content_list.append(row)
    return csv_content_list


if __name__ == "__main__":
    csv_content_list = losd_csv_file( r"C:\Users\dyd9981\PycharmProjects\pythonProject8\data\User.csv")
    print(csv_content_list)
    print(csv_content_list)