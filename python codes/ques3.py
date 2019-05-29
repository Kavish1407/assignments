import json
with open('ques3.json','r') as myfile:
    jsondata=json.load(myfile)
print(jsondata["Records"][0]["s3"]["bucket"]["arn"])