from google.cloud import storage

storage_client = storage.Client()

def download_blob(bucket_name,source_blob_name,destination_file_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print('Blob {} downloaded to {}.'.format(source_blob_name,destination_file_name))
    except:
        print("Some error occured while downloading object")


def main():
    bucket_name = input("Enter Bucket name")  # this test bucket is created in project petraining
    blob_name = input("Enter object name")  # this test file is already present in k-demo-bucket-1
    destination_file_name = input("Enter destination file name to download file")
    download_blob(bucket_name, blob_name, destination_file_name)
