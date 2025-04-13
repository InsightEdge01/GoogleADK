import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.tools import google_search

def search_airbnb_listings(city: str) -> dict:
    """Simulates searching for Airbnb listings in a given city with details.

    Args:
        city (str): The city to search for Airbnb listings.

    Returns:
        dict: status and listings or an error message.
    """
    sample_listings = {
        "new york": [
            {
                "title": "Cozy Studio in Manhattan",
                "price_per_night": "$150",
                "location_highlights": "Close to Central Park and subway stations",
            },
            {
                "title": "Modern Loft in Brooklyn",
                "price_per_night": "$120",
                "location_highlights": "Great nightlife and cafes nearby",
            },
        ],
        "san francisco": [
            {
                "title": "Chic Apartment near Golden Gate Park",
                "price_per_night": "$180",
                "location_highlights": "Quiet neighborhood, walkable to park",
            },
            {
                "title": "Sunny Mission District Flat",
                "price_per_night": "$140",
                "location_highlights": "Vibrant area with restaurants and shops",
            },
        ],
    }

    city_key = city.lower()
    if city_key in sample_listings:
        return {"status": "success", "listings": sample_listings[city_key]}
    else:
        return {
            "status": "error",
            "error_message": f"No Airbnb data available for '{city}'.",
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: status and time info or error.
    """
    tz_map = {
        "new york": "America/New_York",
        "san francisco": "America/Los_Angeles",
        "london": "Europe/London",
        "tokyo": "Asia/Tokyo",
    }

    city_key = city.lower()
    if city_key not in tz_map:
        return {
            "status": "error",
            "error_message": f"No timezone data available for '{city}'.",
        }

    tz = ZoneInfo(tz_map[city_key])
    now = datetime.datetime.now(tz)
    return {
        "status": "success",
        "report": f"The current time in {city.title()} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    }

def get_weather(city: str) -> dict:
    """Simulates retrieving the weather for a given city.

    Args:
        city (str): The name of the city.

    Returns:
        dict: status and weather info or error.
    """
    sample_weather = {
        "new york": "Sunny, 25°C (77°F)",
        "san francisco": "Foggy, 18°C (64°F)",
        "london": "Cloudy, 16°C (61°F)",
        "tokyo": "Rainy, 22°C (72°F)",
    }

    city_key = city.lower()
    if city_key not in sample_weather:
        return {
            "status": "error",
            "error_message": f"No weather data available for '{city}'.",
        }

    return {
        "status": "success",
        "report": f"The weather in {city.title()} is {sample_weather[city_key]}."
    }

# Register all tools in the root agent
root_agent = Agent(
    name="travel_info_agent",
    model="gemini-2.0-flash-exp",
    description="Agent to help users with Airbnb listings, weather, and time info for any city.",
    instruction="Respond with Airbnb listings, current weather, or time based on user queries.",
    tools=[search_airbnb_listings, get_current_time, get_weather],
)
