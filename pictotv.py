import sys
import logging
import os
from samsungtvws import SamsungTVWS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    if len(sys.argv) != 2:
        logger.error("Usage: python scriptname.py image.jpg")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.isfile(image_path):
        logger.error(f"Error: File '{image_path}' not found.")
        sys.exit(1)

    try:
        logger.info("Connecting to Samsung TV at 192.168.1.122")
        tv = SamsungTVWS('192.168.1.122')

        logger.info(f"Opening file '{image_path}'")
        with open(image_path, 'rb') as file:
            data = file.read()
            logger.info(f"File '{image_path}' read successfully.")
        
        logger.info("Uploading image...")
        ZZ = tv.art().upload(data, file_type='JPEG')
        logger.info(f"Image uploaded successfully with ID: {ZZ}")

        logger.info("Selecting image...")
        tv.art().select_image(ZZ)
        logger.info("Image selected successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
