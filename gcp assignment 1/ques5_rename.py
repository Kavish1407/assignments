from google.cloud import storage

storage_client = storage.Client()

def rename_blob(bucket_name,blob_name,new_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        new_blob = bucket.rename_blob(blob, new_name)
        print('Blob {} has been renamed to {}'.format(blob.name, new_blob.name))
    except:
        print("Some error occured while renaming")


def main():
    bucket_name = input("Enter Bucket name")  # this test bucket is created in project petraining
    blob_name = input("Enter object name")  # this test file is already present in k-demo-bucket-1
    new_name = input("Enter new file name")  # this name will be given to file in rename_file
    rename_blob(bucket_name, blob_name, new_name)
