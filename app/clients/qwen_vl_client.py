"""
Qwen-VL client for image analysis.
This client is currently mocked, but will be connected to real Qwen-VL API later.
"""

class QwenVLClient:
    """Client for Qwen-VL image analysis service"""

    def analyze_image(self, image_input: str, image_type: str = "file") -> dict:
        """
        Analyze image to extract elements and characters.

        Input:
            - image_input: Base64 encoded image or URL
            - image_type: "file" or "url"

        Output:
            - Analysis result dict with caption and characters
        """
        # Mock implementation
        return {
            "caption": "A small village with a brave knight and a mysterious wizard",
            "characters": [
                {"id": "char_1", "name": "Brave Knight", "type": "human", "description": "A brave knight with a silver armor"},
                {"id": "char_2", "name": "Mysterious Wizard", "type": "human", "description": "A wise wizard with a long beard"}
            ]
        }

# Singleton client instance
qwen_vl_client = QwenVLClient()
