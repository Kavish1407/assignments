import boto3

def downloadsecondlatestversion(bucket_name,file_path):
            try:
                s3=boto3.client('s3')
                versions = s3.list_object_versions(Bucket = bucket_name, Prefix = file_path)
                s3.download_file(bucket_name, file_path ,"C://Users//Kavish Mehta//Downloads//aa", ExtraArgs={'VersionId':versions['Versions'][1]['VersionId']})
                print("File DOwnloaded")
            except:
                print("Some error occured")

def main():
    bucket_name = input("Enter bucket name: ")
    file_path = input("Enter file name: ")
    downloadsecondlatestversion(bucket_name,file_path)

if __name__ == '__main__':
    main()

