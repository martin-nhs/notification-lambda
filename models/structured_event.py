class StructuredEvent:
    def __init__(self, message: str, nhs_environment: str, service_name: str):
        self._message = message
        self._nhs_environment = nhs_environment
        self._service_name = service_name

    @property
    def message(self):
        return self._message

    @property
    def nhs_environment(self):
        return self._nhs_environment

    @property
    def service_name(self):
        return self._service_name
