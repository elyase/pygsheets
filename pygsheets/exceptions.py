# -*- coding: utf-8 -*-

"""
pygsheets.exceptions
~~~~~~~~~~~~~~~~~~~~

Exceptions used in pygsheets.

"""


class PyGsheetsException(Exception):
    """A base class for pygsheets's exceptions."""


class AuthenticationError(PyGsheetsException):
    """An error during authentication process."""


class SpreadsheetNotFound(PyGsheetsException):
    """Trying to open non-existent or inaccessible spreadsheet."""


class WorksheetNotFound(PyGsheetsException):
    """Trying to open non-existent or inaccessible worksheet."""


class CellNotFound(PyGsheetsException):
    """Cell lookup exception."""


class RangeNotFound(PyGsheetsException):
    """Range lookup exception."""


class NoValidUrlKeyFound(PyGsheetsException):
    """No valid key found in URL."""


class IncorrectCellLabel(PyGsheetsException):
    """The cell label is incorrect."""


class RequestTimeout(PyGsheetsException):
    """Error while sending API request."""


class InvalidArgumentValue(PyGsheetsException):
    """Invalid value for argument"""


class InvalidUser(PyGsheetsException):
    """Invalid user/domain"""
