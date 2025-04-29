import requests
import pathlib
import tempfile
import typing
import logging

from django.conf import settings


_logger = logging.getLogger(__name__)


class ScanServiceClient:
    """
    Client to interact with the Scanner API.
    """
    def __init__(self, chunk_size=1024):
        self.scan_files_path = pathlib.Path(settings.SCANNER_FILES_PATH)
        self.chunk_size = chunk_size

    def get_scan_results(self, file_data: typing.IO) -> typing.Optional[dict]:
        """
        Retrieves scan results from the scanner service.

        :param file_data: Raw file data to send over to the scanner via the shared scan files path.
        :returns: The scan results as a dictionary, or None if the scan failed.
        """
        try:
            with self._get_temp_file(file_data) as temp_file:
                temp_file_path = pathlib.Path(temp_file.name)
                response = requests.post(
                    self._get_scan_url(),
                    json={"storage": "local-zip", "identification": temp_file_path.name}
                )
                response.raise_for_status()
                return response.json()
        except (requests.HTTPError, ValueError, TypeError):
            _logger.exception("Error getting scan results")
            return None

    def _get_temp_file(self, file_data: typing.IO):
        """
        Writes the given file data into a temporary file in the shared scan files path.

        :param file_data: The file data to write.
        :returns: A temporary file.
        """
        temp = tempfile.NamedTemporaryFile(dir=str(self.scan_files_path))
        for data in file_data.read(self.chunk_size):
            temp.write(data)
        return temp

    @staticmethod
    def _get_scan_url() -> str:
        """
        Utility method which assembles the scanner service URL.

        :returns: The scan service URL.
        """
        return f"http://{settings.SCANNER_HOST}:{settings.SCANNER_PORT}/scan"
