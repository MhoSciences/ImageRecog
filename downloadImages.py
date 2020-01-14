from google_images_download import google_images_download as gid

response = gid.googleimagesdownload()

words = ["minifridge", "oven", "dining table", "kitchen cabinets", "kitchen garbage can"]

for word in words:
    arguments = {"keywords":word, "limit":100, "output_directory":"/Users/rodrigoestrella/Mho/Img/images/"}
    response.download(arguments)
