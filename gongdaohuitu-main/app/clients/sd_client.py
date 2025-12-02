"""
Stable Diffusion client for image generation.
This client is currently mocked, but will be connected to real SD API later.
"""

class SDClient:
    """Client for Stable Diffusion image generation service"""

    def generate_image(self, prompt: str, base_image: str = None) -> str:
        """
        Generate image based on prompt, optionally using a base image.

        Input:
            - prompt: Image generation prompt
            - base_image: Optional base image (URL or base64)

        Output:
            - URL of generated image
        """
        # Mock implementation
        return "https://example.com/mock-sd-image.jpg"

    def regenerate_image(self, prompt: str, image: str, feedback: str) -> str:
        """
        Regenerate image with specific feedback.

        Input:
            - prompt: Original generation prompt
            - image: Image to regenerate (URL or base64)
            - feedback: User's improvement suggestions

        Output:
            - URL of regenerated image
        """
        # Mock implementation
        return "https://example.com/mock-sd-image-regenerated.jpg"

# Singleton client instance
sd_client = SDClient()
