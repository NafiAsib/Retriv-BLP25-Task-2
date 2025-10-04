#!/usr/bin/env python3
"""
Script to download CSV files from the BLP25 code generation task repository.
Downloads the following files into a 'data' directory:
- dev_v2.csv
- test_v1.csv
- test_full.csv
"""

import requests
from pathlib import Path
from urllib.parse import urlparse


def create_data_directory():
    """Create the data directory if it doesn't exist."""
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    return data_dir


def download_file(url, destination):
    """
    Download a file from URL to the specified destination.

    Args:
        url (str): The URL to download from
        destination (Path): The local file path to save to

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        print(f"Downloading {url}...")

        if "github.com" in url and "/blob/" in url:
            raw_url = url.replace("github.com", "raw.githubusercontent.com").replace(
                "/blob/", "/"
            )
        else:
            raw_url = url

        response = requests.get(raw_url, timeout=30)
        response.raise_for_status()

        with open(destination, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully downloaded {destination.name}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"✗ Unexpected error downloading {url}: {e}")
        return False


def main():
    """Main function to download all CSV files."""
    # URLs of the CSV files to download
    file_urls = [
        "https://github.com/NoshinUlfat/blp25_code_generation_task/blob/main/docs/assets/files/dev_v2.csv",
        "https://github.com/NoshinUlfat/blp25_code_generation_task/blob/main/docs/assets/files/test_v1.csv",
        "https://github.com/NoshinUlfat/blp25_code_generation_task/blob/main/docs/assets/files/test_full.csv",
    ]

    data_dir = create_data_directory()
    print(f"Data directory: {data_dir.absolute()}")

    success_count = 0
    total_files = len(file_urls)

    for url in file_urls:
        filename = Path(urlparse(url).path).name
        destination = data_dir / filename

        if download_file(url, destination):
            success_count += 1

    print(
        f"\nDownload complete: {success_count}/{total_files} files downloaded successfully"
    )

    if success_count == total_files:
        print("All files downloaded successfully!")
    else:
        print(f"Warning: {total_files - success_count} files failed to download")


if __name__ == "__main__":
    main()
