from google.cloud import storage

storage_client = storage.Client()

def upload_blob(bucket_name,source_file_name,destination_blob_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print('File {} uploaded to {}.'.format(source_file_name,destination_blob_name))
    except:
        print("Some error occured while uploading object")


def main():
    bucket_name = input("Enter Bucket name")  # this test bucket is created in project petraining
    source_file_name = input("Enter source file name to upload file")
    upload_name = input("Enter name to be uploaded")  # this test file is already present in k-demo-bucket-1
    upload_blob(bucket_name, source_file_name, upload_name)
