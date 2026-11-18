import requests


class WeatherForecastTool:
    """Small OpenWeatherMap client used by the weather LangChain tools."""

    def __init__(self, api_key: str | None):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    def _get(self, endpoint: str, city: str):
        if not self.api_key:
            return None
        response = requests.get(
            f"{self.base_url}/{endpoint}",
            params={"q": city, "appid": self.api_key, "units": "metric"},
            timeout=15,
        )
        if response.ok:
            return response.json()
        return None

    def get_current_weather(self, city: str):
        return self._get("weather", city)

    def get_forecast_weather(self, city: str):
        return self._get("forecast", city)
