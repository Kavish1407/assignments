from google.cloud import storage

storage_client = storage.Client()

def copy_blob(bucket_name, blob_name, new_bucket_name):
    try:
        source_bucket = storage_client.get_bucket(bucket_name)
        source_blob = source_bucket.blob(blob_name)
        destination_bucket = storage_client.get_bucket(new_bucket_name)
        new_blob = source_bucket.copy_blob(source_blob, destination_bucket, blob_name)
        print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(source_blob.name, source_bucket.name,new_blob.name, destination_bucket.name))
    except:
        print("Some error occured copying object")
def main():

    bucket_name = input("Enter Bucket name")  # this test bucket is created in project petraining
    blob_name = input("Enter object name")  # this test file is already present in k-demo-bucket-1
    new_bucket_name = input("Enter new Bucket name")  # this second test bucket is also created
    copy_blob(bucket_name, blob_name, new_bucket_name)
