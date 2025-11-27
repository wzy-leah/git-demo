"""
Wen-v2.2 client for video generation from keyframes.
This client is currently mocked, but will be connected to real Wen API later.
"""

class WenClient:
    """Client for Wen-v2.2 video generation service"""

    def generate_video(self, keyframes: list, duration: int = 60, rhythm: str = "medium") -> str:
        """
        Generate video from list of keyframe images.

        Input:
            - keyframes: List of keyframe image URLs
            - duration: Total video duration in seconds
            - rhythm: Video rhythm ("fast", "medium", "slow")

        Output:
            - URL of generated video
        """
        # Mock implementation
        return "https://example.com/mock-wen-video.mp4"

# Singleton client instance
wen_client = WenClient()
