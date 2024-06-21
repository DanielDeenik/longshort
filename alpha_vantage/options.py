from .alphavantage import AlphaVantage as av


class Options(av):

    """This class implements all the api calls to provide realtime and historical
    US options data
    """

    @av._output_format
    @av._call_api_on_func
    def get_historical_options(self, symbol: str, date:str=None, datatype:str='json'):
        """ Return historical options in two json objects as data and
        meta_data. It raises ValueError when problems arise

        Keyword Arguments:
            symbol:  the symbol for the equity we want to get its data
            date: date from which to retrieve data, by default date is 
                not set and returns data from previous trading session
            datatype: strings 'json' and 'csv' are accepted,
                by default, datatype='json'
        """
        _FUNCTION_KEY = "HISTORICAL_OPTIONS"
        return _FUNCTION_KEY, "data", None