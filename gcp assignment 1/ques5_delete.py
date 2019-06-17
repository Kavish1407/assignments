from google.cloud import storage

storage_client = storage.Client()

def delete_blob(bucket_name, blob_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.delete()
        print('Blob {} deleted.'.format(blob_name))
    except:
        print("Some error occured while deleting object")
def main():

    bucket_name = input("Enter Bucket name")  # this test bucket is created in project petraining
    blob_name = input("Enter object name")  # this test file is already present in k-demo-bucket-1
    delete_blob(bucket_name,blob_name)