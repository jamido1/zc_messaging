from pydantic import BaseModel


class ResponseModel(BaseModel):
    """Creates a response model for the API.

    Provides a structure for providing a response to the API.
    Provides a static method for success responses

    Attributes:
        status: The status of the response.
        message: The message of the response.
        data: The data of the response.
    """

    status: str
    message: str
    data: dict

    @staticmethod
    def success(data, message="success"):
        """Provides a success response data

        Args:
            data (dict): data to be returned
            message (str, optional): Descriptive messaged. Defaults to "success".

        Returns:
            dict: key-value pair of status, message and data
        """
        return ResponseModel(status="success", message=message, data=data).dict()
