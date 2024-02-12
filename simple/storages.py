from storages.backends.s3boto3 import S3Boto3Storage

class MinioStorageStatic(S3Boto3Storage):
  location = 'static'
  file_overwrite = False

class MinioStorageMedia(S3Boto3Storage):
  location = 'media'
  file_overwrite = False