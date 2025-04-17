import requests

class HAAPI:
    def __init__(self, token: str, base_url: str):
        self.token = token
        self.base_url = base_url.rstrip("/")

    def _call(self, method: str, path: str, data: dict = None):
        url = f"{self.base_url}{path}"
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }
        response = requests.request(method, url, headers=headers, json=data)
        return response

    def toggle_device(self, entity_id: str) -> str:
        res = self._call("POST", "/api/services/homeassistant/toggle", {"entity_id": entity_id})
        return f"Toggled {entity_id}." if res.ok else f"Failed to toggle {entity_id}."

    def move_temi(self, location: str) -> str:
        res = self._call("POST", "/api/services/mqtt/publish", {
            "topic": "RoboConnect/Temi_Robot/serviceHandler/Location/set",
            "payload": location.lower(),
            "qos": 0,
            "retain": False,
        })
        return f"Temi is moving to {location}." if res.ok else f"Failed to move Temi to {location}."
