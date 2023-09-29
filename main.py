import requests

# List of image URLs you want to download
image_urls = [
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fi0.wp.com%2Fneptune.ai%2Fwp-content%2Fuploads%2F2022%2F10%2FHOG-object-detection-algorithm.png%3Fssl%3D1&tbnid=tyR1qlYh67l-FM&vet=12ahUKEwiMy6LTmM2BAxUgl2MGHbqcAuAQMyhhegUIARCxAg..i&imgrefurl=https%3A%2F%2Fneptune.ai%2Fblog%2Fobject-detection-algorithms-and-libraries&docid=pAR131qgfyr1UM&w=1600&h=553&q=opencv%20in%20person%20detection%20with%20date%20and%20time%20images&ved=2ahUKEwiMy6LTmM2BAxUgl2MGHbqcAuAQMyhhegUIARCxAg",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcamo.githubusercontent.com%2Fe6d0b5442be4244cf57185e8e9f1e337671ed1d59e8cc34f21a567204f3bc166%2F68747470733a2f2f692e7974696d672e636f6d2f76692f54544638586f4f574444772f6d617872657364656661756c742e6a7067&tbnid=r5YLJu7CSBQDZM&vet=10CAYQMyhqahcKEwjg47eyn82BAxUAAAAAHQAAAAAQAw..i&imgrefurl=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FGSoC_2022&docid=xWfjU6dT3m9eCM&w=1280&h=720&q=opencv%20in%20person%20detection%20with%20date%20and%20time%20images&ved=0CAYQMyhqahcKEwjg47eyn82BAxUAAAAAHQAAAAAQAw",
    "https://www.google.com/imgres?imgurl=https%3A%2F%2Fcamo.githubusercontent.com%2Fe6d0b5442be4244cf57185e8e9f1e337671ed1d59e8cc34f21a567204f3bc166%2F68747470733a2f2f692e7974696d672e636f6d2f76692f54544638586f4f574444772f6d617872657364656661756c742e6a7067&tbnid=r5YLJu7CSBQDZM&vet=10CAYQMyhqahcKEwjg47eyn82BAxUAAAAAHQAAAAAQAw..i&imgrefurl=https%3A%2F%2Fgithub.com%2Fopencv%2Fopencv%2Fwiki%2FGSoC_2022&docid=xWfjU6dT3m9eCM&w=1280&h=720&q=opencv%20in%20person%20detection%20with%20date%20and%20time%20images&ved=0CAYQMyhqahcKEwjg47eyn82BAxUAAAAAHQAAAAAQAw",
    # Add more image URLs as needed
]

try:
    for idx, image_url in enumerate(image_urls, start=1):
        # Send an HTTP GET request to the image URL
        response = requests.get(image_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Get the content of the response (image binary data)
            image_data = response.content

            # Specify the local file path where you want to save the image
            local_file_path = f"downloaded_image_{idx}.jpg"

            # Write the image data to the local file
            with open(local_file_path, "wb") as file:
                file.write(image_data)

            print(f"Image {idx} downloaded successfully as {local_file_path}")
        else:
            print(f"Failed to download image {idx}. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {str(e)}")
